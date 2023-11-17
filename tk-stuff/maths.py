from math import (
    sin, cos, tan, acos,
    asin, atan, pi, log,
    radians, degrees, pow,
    sqrt
)
def sine(degree):
    return sin(radians(degree))

def coss(degree):
    return cos(radians(degree))

def tann(degree):
    return tan(radians(degree))

def _snn(val):
    return degrees(asin(val))

def _css(val):
    return degrees(acos(val))

def _tnn(val):
    return degrees(atan(val))

def _lgg(val):
    return log(val, 10)

def alog(val):
    return pow(10, val)

def parse(string, ans):
    res = string
    to_change = {'sin-1': '_snn', 'cos-1': '_css',
                 'log-1': 'alog', 'tan-1': '_tnn',
                 'log': '_lgg', 'sin': 'sine',
                 'cos-1': 'coss', 'tan-1': 'tann',
                 'π': 'pi', 'mod': '%', 'x': '*',
                 '^': '**', '÷': '/', "Ans": 'ans',
                 '√': 'sqrt'}
    special = {}
    for k, v in to_change.items():
        res = res.replace(k, v)
    x = None
    try:
        x = eval(res)
    except:
        pass
    finally:
        return x
    return res
