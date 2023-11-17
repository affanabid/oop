#-----------------------------------poly.py-----------------------------------------------
class Polynomial:
    
    def __init__(self, var, degree, coeff):
        self.__var = var
        self.__degree = degree
        self.__coeff = coeff

    @property
    def var(self):
        return self.__var
    
    @var.setter
    def var(self, value):
        self.__var = value  

    @property
    def degree(self):
        return self.__degree
    
    @degree.setter
    def degree(self, value):
        self.__degree = value

    @property
    def coeff(self):
        return self.__coeff  

    @coeff.setter
    def coeff(self, value):
        self.__coeff = value

    def __str__(self):
        string = f'{self.coeff[0]}{self.__var}^{self.degree }'
        for degree in range(self.degree-1, 0, -1):
            coefficient = self.coeff[self.degree - degree]
            if coefficient >= 0:
                string += f' + {coefficient}{self.__var}^{degree} '
            else:
                string += f' {coefficient}{self.__var}^{degree} '
        if self.coeff[self.degree] >= 0:
            string += f'+ {self.coeff[self.degree]}'
        else:
            string += f'{self.coeff[self.degree]}'
        return string
    
    @staticmethod
    def add_polynomials(p1, p2):
        max_degree = max(p1.degree, p2.degree)
        result = [0] * (max_degree + 1)
        for i in range(p1.degree+1):
            result[max_degree - p1.degree + i] += p1.coeff[i]
        for i in range(p2.degree + 1):
            result[max_degree - p2.degree + i] += p2.coeff[i]
        return Polynomial('x', max_degree, result)
    
    def add(self, p2):
        max_degree = max(self.degree, p2.degree)
        result_coeff = [0] * (max_degree + 1)
    
        for i in range(self.degree + 1):
            result_coeff[max_degree - self.degree + i] += self.coeff[i]
    
        for i in range(p2.degree + 1):
            result_coeff[max_degree - p2.degree + i] += p2.coeff[i]

        return Polynomial(self.var, max_degree, result_coeff)
    
    def subtract(self, p2):
        max_degree = max(self.degree, p2.degree)
        result_coeff = [0] * (max_degree + 1)
        
        for i in range(self.degree + 1):
            result_coeff[max_degree - self.degree + i] += self.coeff[i]
        
        for i in range(p2.degree + 1):
            if max_degree - p2.degree + i < len(result_coeff):
                result_coeff[max_degree - p2.degree + i] -= p2.coeff[i]

        return Polynomial(self.var, max_degree, result_coeff)
    
    def multiply(self, p2):
        max_degree = self.degree + p2.degree
        result_coeff = [0] * (max_degree + 1)
        
        for i in range(self.degree + 1):
            for j in range(p2.degree + 1):
                result_coeff[i + j] += self.coeff[i] * p2.coeff[j]

        return Polynomial(self.var, max_degree, result_coeff)

    def evaluate(self, x):
        result = 0
        for i, coeff in enumerate(self.coeff):
            result += coeff * (x ** i)
        return result
    
    @staticmethod
    def equal_polynomials(p1, p2):
        if len(p1.coeff) == len(p2.coeff):
            check = 0
            for i in range(len(p1.coeff)):
                if p1.coeff[i] == p2.coeff[i]:
                    check += 1
            if check == len(p1.coeff):
                return f'Both polynomials are equal.'
            else:
                return f'{p1} and {p2} are unequal.'
        else:
            return 'Equality check not possible due to different number of coefficients'

    def divide(self, p2):
        pass

#---------------------------------polytest.py-----------------------------------------------------
polynomials = []
poly1 = Polynomial('x', degree=4, coeff=[4, 1, 2, 3, 4])
poly2 = Polynomial('x', degree=3, coeff=[1, 1, 1, 1])
poly3 = Polynomial('x', degree=2, coeff=[2, 1, 3])
poly4 = Polynomial('x', degree=3, coeff=[1, 1, 1, 1])

print("Polynomial1: ", poly1)
print("Polynomial2: ", poly2)
# print('P1 + P2: ', poly1.add(poly2))
# print('P1 - P2: ', poly1.subtract(poly2))
# print('P1 * P2: ',poly2.multiply(poly2))
# x_value = 2
# print(f'Evaluation of polynomial1({poly1}) when x={x_value}: {poly1.evaluate(x_value)}\n')
# print('--------------------------------------------------------------')
# print("Polynomial4: ", poly4)
# print("Polynomial3: ", poly3)
# print('P4 + P3: ', poly4.add(poly3))
# print('P4 - P3: ', poly4.subtract(poly3))
# print('P4 * P3: ',poly4.multiply(poly3))
# x_value = 2
# print(f'Evaluation of polynomial3({poly3}) when x={x_value}: {poly3.evaluate(x_value)}\n')
# print('\nUsing static method: ')
# print(f'P1 + P1: {Polynomial.add_polynomials(poly1, poly1)}')
# print(f'P1 + P2: {Polynomial.add_polynomials(poly1, poly2)}')
# print(f'P1 + P3: {Polynomial.add_polynomials(poly1, poly3)}')
# print('\nChecking equality:')
# print(f'P1 and P1: {Polynomial.equal_polynomials(poly1, poly1)}')
# print(f'P1 and P2: {Polynomial.equal_polynomials(poly1, poly2)}')