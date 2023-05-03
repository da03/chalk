import chalk
from chalk.transform import (
    P2,
    V2,
    Affine,
    BoundingBox,
    from_radians,
    origin,
    to_radians,
    unit_x,
    unit_y,
)
from colour import Color
from math import cos, sin

black = Color("black")
lightgrey = Color("lightgrey")
white = Color("white")
blue = Color("blue")
orange = Color("orange")

def radians(ang):
    return ang * ( math.pi) / 180

def height(d):
  return d.get_envelope().height

def width(d):
  return d.get_envelope().width

def triangle(width, height=None):
    if height is None:
        return chalk.equilateral_triangle(width)
    return chalk.equilateral_triangle(1).scale_x(width).scale_y(height)

def prealign(args, align=None, subdiagram_name=None):
    if align is None or align=="c":
        if subdiagram_name is not None:
            envelope = args[0].get_subdiagram(subdiagram_name).get_envelope()
            t = Affine.translation(-envelope.center)
            args[0] = args[0].apply_transform(t)
        return args
    else:
        v = {"t": -unit_y, "b": unit_y, "l": -unit_x, "r": unit_x,
            "tl": -unit_y -unit_x, "bl": unit_y - unit_x, "tr": -unit_y-unit_x, "br": unit_y +unit_x}[align]
        
        return [args[0].align(v, subdiagram_name)] + [a.align(v) for a in args[1:]]

def inside(back, front, align=None):
    return chalk.concat(prealign([back, front], align)).center_xy()

def overlap(objects, align=None):
    return chalk.concat(prealign(objects, align)).center_xy()

def nextto(left, right, sep=None, align=None, subdiagram_name=None):
    return chalk.hcat(prealign([left, right], align, subdiagram_name), sep=sep, subdiagram_name=subdiagram_name).center_xy()

def nextto_in(diagram, left, right, sep=0, align=None):
    return nextto(diagram, right, sep=sep, align=align, subdiagram_name=left)

def above(top, bottom, sep=None, align=None, subdiagram_name=None):
    return chalk.vcat(prealign([top, bottom], align, subdiagram_name), sep=sep, subdiagram_name=subdiagram_name).center_xy()

def above_in(diagram, top, bottom, sep=0, align=None):
    return above(diagram, bottom, sep=sep, align=align, subdiagram_name=top)
