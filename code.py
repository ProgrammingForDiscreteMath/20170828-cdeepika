from math import sqrt
class ComplexNumber:
    """
    The class of complex numbers.
    """
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary part.
        """
        self.real = real_part
        self.imaginary = imaginary_part
    def __repr__(self):
        """
        Return the string representation of self.
        """
        return "%s + %s i"%(self.real, self.imaginary)
    def __eq__(self, other):
        """
        Test if ``self`` equals ``other``.
        
        Two complex numbers are equal if their real parts are equal and
        their imaginary parts are equal.
        """
        return self.real == other.real and self.imaginary == other.imaginary
    def modulus(self):
        """
        Return the modulus of self.
        
        The modulus (or absolute value) of a complex number is the square
        root of the sum of squares of its real and imaginary parts.
        """
        return sqrt(self.real**2 + self.imaginary**2)
    def sum(self, other):
        """
        Return the sum of ``self`` and ``other``.
        """
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
    
#Question No.- 1    
    def product(self,other):
        """
        Returns the product of two complex numbers ``self`` and ``other``.
        
        General formula for product of two complex numbers is given here:
        https://www2.clarku.edu/~djoyce/complex/mult.html
        """
        x = self.real
        y = self.imaginary
        u = other.real
        v = other.imaginary
        
        w = x*u - y*v
        z = x*v + y*u
        return ComplexNumber(w,z)
##TEST : from the same URL:https://www2.clarku.edu/~djoyce/complex/mult.html

#a = ComplexNumber(3, 2) 
#b = ComplexNumber(1,4)
#x = a.product(b) = -5 + 14 

#Question No.-2    
    def complex_conjugate(self):
        """Replace the number with it's complex conjugate"""
        self.real = self.real
        self.imaginary = (-1)*self.imaginary
        #prints conjugated self.imaginary
    
class NonZeroComplexNumber(ComplexNumber):
    def __init__(self, real_part, imaginary_part):
        """
        Initialize ``self`` with real and imaginary parts after checking validity.
        """
        if real_part == 0 and imaginary_part == 0:
            raise ValueError("Real or imaginary part should be nonzero.")
        return ComplexNumber.__init__(self, real_part, imaginary_part)
    def inverse(self):
        """
        Return the multiplicative inverse of ``self``.
        """
        den = self.real**2 + self.imaginary**2
        return NonZeroComplexNumber(self.real/den, -self.imaginary/den)
#Question No.- 3
    def polar_coordinates(self):
        """
        return polar coordinate from given cartesian coordinates ``a``, ``b``.
        """
        a = self.real
        b = self.imaginary
        r = sqrt(a**2 + b**2)
        try:
            theta = atan(a/b)
        except ZeroDivisionError:
            if b!=0:
                theta = pi/2
            else:
                raise OriginError("origin does not have well defined polar coordinates")
        return (r, theta)
    def logarithm(self):
        """
        Returns logarithm of the non zero complex number.
        
        For given complex number ``z `` in a polar form ``(``r, theta ``)``, log z = ln``(``r``)`` + i theta.
        """
        z = self.polar_coordinates()
        ln = log(z[0])
        t = z[1]
        
        return NonZeroComplexNumber(ln,t)