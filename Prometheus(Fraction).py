def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction():
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
        if self.den == 0:
            raise ZeroDivisionError
        else:
            pass
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __sub__(self,otherfraction):
        newnum = self.num*otherfraction.den - \
                    self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    def __mul__(self, otherfraction):
        newnum = self.num*otherfraction.num
        newden = self.den*otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum//common,newden//common)
    def __truediv__(self, otherfraction):
        # if self.den == 0:
        #     raise Exception(ZeroDivisionError)
        # else: 
        #     pass
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num
        common = gcd(newnum, newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum



if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 3)
    x / y == Fraction(3, 4)
    print(x, y)