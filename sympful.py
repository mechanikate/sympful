import math


def decimals_matching(decimal_a, decimal_b):
    d = 0
    for i in range(len(str(decimal_a))):
        if (int(decimal_a * (10**i)) == int(decimal_b * (10**i))):
            d += 1
    if (str(float(decimal_a)).split(".") == str(float(decimal_b)).split(".")
            and str(int(decimal_a)) == str(int(decimal_b))):
        return 128
    return d


class Symbolic:
    def __init__(self, float_value, string_value=-1):
        self.value = float_value
        if (strval == -1):
            self.strval = str(float_value)
        if (dm(float_value, math.pi) > 15):
            self.strval = "pi"
        if (dm(float_value, math.e) > 15):
            self.strval = "e"
        if (string_value != -1):
            self.strval = string_value

    def sqrt(self):
        return Symbolic(math.sqrt(self.value), "(" + self.strval + "^(1/2))")

    def nrt(self, n):
        return Symbolic(self.value**(1 / n),
                        "(" + self.strval + ")^(1/" + str(n) + ")")

    def plus(self, b):
        if (b.value == 0):
            return self
        elif (self.value == 0):
            return b
        elif (self.value == b.value):
            return Symbolic(self.value * 2, self.strval + "+" + b.strval)
        return Symbolic(self.value + b.value, self.strval + "+" + b.strval)

    def minus(self, b):
        return Symbolic(self.value - b.value, self.strval + "-" + b.strval)

    def times(self, b):
        if (isinstance(b, int)):
            b = sym(b)
        if (dm(float(b.value), float(self.value)) > 16):
            return self.pow(sym(2))
        if (self.value == 0 or b.value == 0):
            return Symbolic(0)
        if (b.value == 1):
            return self
        if (self.value == 1):
            return b
        return Symbolic(self.value * b.value,
                        b.strval + "(" + self.strval + ")")

    def divided_by(self, b):
        if (dm(self.value, b.value) > 16):
            return Symbolic(1)
        if (self.value == 1 and (str(b.value) * 10)[-1] != "0"):
            return b.pow(sym(-1))
        if (b.value == 1):
            return self
        return Symbolic(self.value / b.value, self.strval + "/" + b.strval)

    def to_the_power_of(self, b):
        if (b.value == 0):
            return sym(1)
        elif (b.value == 1):
            return self
        return Symbolic(self.value**b.value,
                        "(" + self.strval + ")^" + b.strval)

    def __str__(self):
        return self.strval

    __repr__ = __str__
    add = plus
    __add__ = add
    sub = minus
    __sub__ = sub
    mul = times
    __mul__ = mul
    __rmul__ = mul
    div = divided_by
    __truediv__ = div
    pow = to_the_power_of
    __pow__ = pow


def sum(f, s, e):
    r = 0
    for x in range(s, e):
        r += f(x)
    return r


def sym(v, x=-1):
    return Symbolic(v, x)


def reimann(f, a, b, n):
    dx = ((b - a) / n)
    return dx * (f(a) + sum(lambda v: f(a + (v * dx)), 0, n - 1))


def integrate(f, a, b):
    return reimann(f, a, b, Symp.iter)


def sqrt(v):
    return sym(v).sqrt()


def exp(v):
    return sym(math.e).pow(sym(v))


def sin(v):
    return sym(math.sin(v), "sin(" + str(v) + ")")


def cos(v):
    return sym(math.cos(v), "cos(" + str(v) + ")")


def tan(v):
    return sym(math.tan(v), "tan(" + str(v) + ")")


def sq(v):
    return v.pow(sym(2))


square = sq
squared = sq


def cb(v):
    return v.pow(sym(3))


cube = cb
cubed = cb


class Symp:
    def __init__(self):
        pass

    def ultesta(self):
        ta = tan((5)).pow(sym(3))

        def tst(self):
            return "test"

        self.plugin(tst, "tst")
        return ta

    def plugin(self, f, n):
        for i in n:
            setattr(Symbolic, i, f)


def zero(self):
    self.value = 0
    self.strval = "0"
    return self


setattr(Symp, "iter", 5000)
Symp().plugin(zero, ["zero", "z"])
e = sym(math.e)
pi = sym(math.pi)
sqrt2 = sym(2).sqrt()
