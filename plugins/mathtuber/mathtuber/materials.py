"""Optional vector material cues; deliberately stylized, not a light simulation."""
import math
from manim import Circle, VGroup, interpolate_color, ManimColor

def painted_bead(radius=1.0, color='#8EAFAA', shade='#243944', highlight='#F3ECDD', layers=18):
    """A circular silhouette with nested translucent-looking color washes.

    The highlight is offset toward upper left. Every layer remains inside the
    silhouette; the object can move/scale as a normal VGroup. This is an artistic
    depth cue, not a measurement of irradiance or a physically based material.
    """
    if isinstance(radius,bool) or not isinstance(radius,(int,float)) or not math.isfinite(radius) or radius<=0:
        raise ValueError('radius must be finite and positive')
    if isinstance(layers,bool) or not isinstance(layers,int) or not 2<=layers<=64:
        raise ValueError('layers must be an integer from 2 to 64')
    base=ManimColor(color);dark=interpolate_color(base,ManimColor(shade),.28);light=interpolate_color(base,ManimColor(highlight),.52)
    group=VGroup(Circle(radius=radius,stroke_width=0,fill_color=dark,fill_opacity=1))
    for i in range(1,layers+1):
        t=i/layers;r=radius*(1-.78*t)
        # Offset norm <= .32*r_original*t; shrink .78*r_original*t.
        disk=Circle(radius=r,stroke_width=0,fill_color=interpolate_color(dark,light,t),fill_opacity=1)
        disk.shift([-radius*.22*t,radius*.22*t,0]);group.add(disk)
    return group
