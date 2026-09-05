#!/usr/bin/env python3
"""Convert a trusted legacy Google credential pickle without arbitrary class loading."""
import argparse
import datetime
import io
import json
import os
from pathlib import Path
import pickle

class CredentialState:
    def __setstate__(self, state):
        if not isinstance(state, dict):
            raise ValueError('Unsupported credential state')
        self.state = state

class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        allowed = {
            ('google.oauth2.credentials', 'Credentials'): CredentialState,
            ('datetime', 'datetime'): datetime.datetime,
            ('datetime', 'timezone'): datetime.timezone,
            ('datetime', 'timedelta'): datetime.timedelta,
        }
        if (module, name) not in allowed:
            raise ValueError(f'Unsupported pickle class: {module}.{name}')
        return allowed[module, name]

def convert(source):
    value = RestrictedUnpickler(io.BytesIO(source)).load()
    if not isinstance(value, CredentialState):
        raise ValueError('Expected Google OAuth credentials')
    state = value.state
    result = {key: state.get('_'+key) for key in ('refresh_token','token_uri','client_id','client_secret','scopes')}
    result['token'] = state.get('token', state.get('_token'))
    expiry = state.get('expiry', state.get('_expiry'))
    if expiry is not None:
        result['expiry'] = expiry.isoformat().replace('+00:00','Z')
    if not all(result.get(k) for k in ('refresh_token','client_id','client_secret','token_uri')):
        raise ValueError('Legacy credentials lack refresh fields')
    return {k:v for k,v in result.items() if v is not None}

def main():
    p=argparse.ArgumentParser();p.add_argument('--source',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    output=Path(a.output).expanduser()
    if output.exists():raise SystemExit('Output exists; refusing to overwrite')
    data=convert(Path(a.source).expanduser().read_bytes())
    output.parent.mkdir(parents=True,exist_ok=True)
    with os.fdopen(os.open(output,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600),'w') as stream:
        json.dump(data,stream)
    print('Converted credential file with mode 0600; no credential values displayed.')
if __name__=='__main__':main()
