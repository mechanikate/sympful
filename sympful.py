import math
def dm(a,b):
  d=0
  for i in range(len(str(a))):
    if(int(a*(10**i))==int(b*(10**i))):
      d+=1
  return d
class Symbolic:
  def __init__(self, floatv, strval=-1):
    self.value=floatv
    if(strval == -1):
      self.strval = str(floatv)
    if(dm(floatv,math.pi)>15):
      self.strval="pi"
    if(dm(floatv,math.e)>15):
      self.strval="e"
    if(strval!=-1):
      self.strval = strval
  def sqrt(self):
    return Symbolic(math.sqrt(self.value), "("+self.strval+"^(1/2))")
  def nrt(self,n):
    return Symbolic(self.value ** (1/n),"("+self.strval+")^(1/"+str(n)+")")    
  def plus(self, b):
    if(b.value==0):
      return self
    elif(self.value==0):
      return b
    elif(self.value==b.value):
      return Symbolic(self.value*2, self.strval+"+"+b.strval)
    return Symbolic(self.value + b.value, self.strval+"+"+b.strval)
  def minus(self, b):
    return Symbolic(self.value - b.value, self.strval+"-"+b.strval)
  def times(self, b):
    if(isinstance(b,int)):
      b=sym(b)
    if(dm(b.value,self.value)>16):
      return self.pow(sym(2))
    if(self.value==0 or b.value==0):
      return Symbolic(0)
    return Symbolic(self.value * b.value, self.strval+"("+b.strval+")")
  def divided_by(self, b):
    return Symbolic(self.value / b.value, self.strval+"/"+b.strval)
  def to_the_power_of(self, b):
    if(b.value==0):
      return sym(1)
    elif(b.value==1):
      return sym(self.value)
    return Symbolic(self.value ** b.value, "("+self.strval+")^"+b.strval)
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
def sum(f,s,e):
  r=0
  for x in range(s,e):
    r+=f(x)
  return r
    
def sym(v,x=-1):
  return Symbolic(v,x)
def reimann(f,a,b,n):
  p=0
  for i in range(1,n):
    p+=f((a+(i-1))*((b-a)/n))*((b-a)/n)
  return p
def integrate(f,a,b):
  return reimann(f,a,b,Symp.iter)
def sqrt(v):
  return sym(v).sqrt()
def exp(v):
  return sym(math.e).pow(sym(v))
def sin(v):
  return sym(math.sin(v),"sin("+str(v)+")")
def cos(v):
  return sym(math.cos(v),"cos("+str(v)+")")
def tan(v):
  return sym(math.tan(v),"tan("+str(v)+")")
  
def sq(v):
  return v.pow(sym(2))
square=sq
squared=sq
def cb(v):
  return v.pow(sym(3))
cube=cb
cubed=cb
class Symp:
  def __init__(self):
    pass
  def ultesta(self):
    ta = tan((5)).pow(sym(3))
    def tst(self):
      return "test"
    self.plugin(tst,"tst")
    return ta
  def plugin(self,f,n):
    for i in n:
      setattr(Symbolic,i,f)

def zero(self):
  self.value=0
  self.strval="0"
  return self

setattr(Symp,"iter", 5000)  
Symp().plugin(zero,["zero","z"])
