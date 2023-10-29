class Mat2by2:
    
    def __init__(self, a11=0, a12 = 0, a21 = 0, a22 = 0):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22
    
    def add_matrix(self, matrix2):
        added_matrix = Mat2by2()
        added_matrix.a11 = self.a11 + matrix2.a11
        added_matrix.a12 = self.a12 + matrix2.a12
        added_matrix.a21 = self.a21 + matrix2.a21
        added_matrix.a22 = self.a22 + matrix2.a22
        print(f'Added Matrix: [{added_matrix.a11}, {added_matrix.a12}, {added_matrix.a21}, {added_matrix.a22}]')
    
    def subtract_matrix(self, matrix2):
        subtracted_matrix = Mat2by2()
        subtracted_matrix.a11 = self.a11 - matrix2.a11
        subtracted_matrix.a12 = self.a12 - matrix2.a12
        subtracted_matrix.a21 = self.a21 - matrix2.a21
        subtracted_matrix.a22 = self.a22 - matrix2.a22
        print(f'Subtracted Matrix: [{subtracted_matrix.a11}, {subtracted_matrix.a12}, {subtracted_matrix.a21}, {subtracted_matrix.a22}]')
    
    def scalar_multiple(self, number):
        matrix = Mat2by2()
        matrix.a11 = self.a11 * number
        matrix.a12 = self.a12 * number
        matrix.a21 = self.a21 * number
        matrix.a22 = self.a22 * number
        print(f'Scalar Multiple: [{matrix.a11}, {matrix.a12}, {matrix.a21}, {matrix.a22}]')
    
    def transpose(self):
        matrix1 = Mat2by2()
        matrix1.a11 = self.a11
        matrix1.a12 = self.a21
        matrix1.a21 = self.a12
        matrix1.a22 = self.a22
        print(f'Transpose: [{matrix1.a11}, {matrix1.a12}, {matrix1.a21}, {matrix1.a22}]')
    
    def determinant(self):
        determinant = ((self.a11 * self.a22) - (self.a21 * self.a12))
        print(f'Determinant = {determinant}')
    
    def multiply(self, matrix2):
        multiplied_matrix = Mat2by2()
        multiplied_matrix.a11 = self.a11 * matrix2.a11 + self.a12 * matrix2.a21
        multiplied_matrix.a12 = self.a11 * matrix2.a12 + self.a12 * matrix2.a22
        multiplied_matrix.a21 = self.a21 * matrix2.a11 + self.a22 * matrix2.a21
        multiplied_matrix.a22 = self.a21 * matrix2.a12 + self.a22 * matrix2.a22
        print(f'Multiplied : [{multiplied_matrix.a11}, {multiplied_matrix.a12}, {multiplied_matrix.a21}, {multiplied_matrix.a22}]')
    
    def divide(self, matrix2):
        det_matrix2 = ((matrix2.a11 * matrix2.a22) - (matrix2.a12 * matrix2.a21))
        inverse_matrix2 = Mat2by2()
        inverse_matrix2.a11 = matrix2.a22 // det_matrix2
        inverse_matrix2.a12 = -(matrix2.a12) // det_matrix2
        inverse_matrix2.a21 = -(matrix2.a21) // det_matrix2
        inverse_matrix2.a22 = matrix2.a11 // det_matrix2
        result_matrix = Mat2by2()
        result_matrix.a11 = self.a11 * inverse_matrix2.a11 + self.a12 * inverse_matrix2.a21
        result_matrix.a11 = self.a11 * inverse_matrix2.a12 + self.a12 * inverse_matrix2.a22
        result_matrix.a21 = self.a21 * inverse_matrix2.a11 + self.a22 * inverse_matrix2.a21
        result_matrix.a22 = self.a21 * inverse_matrix2.a12 + self.a22 * inverse_matrix2.a22
        print(f'Divided: [{result_matrix.a11}, {result_matrix.a12}, {result_matrix.a21}, {result_matrix.a22}]')

    def inverse(self):
        determinant = ((self.a11 * self.a22) - (self.a21 * self.a12))
        adjoint_matrix = Mat2by2()
        adjoint_matrix.a11 = self.a22 // determinant
        adjoint_matrix.a12 = -(self.a12) // determinant
        adjoint_matrix.a21 = -(self.a21) // determinant
        adjoint_matrix.a22 = self.a11 // determinant
        print(f'Inverse of a Matrix: [{adjoint_matrix.a11}, {adjoint_matrix.a12}, {adjoint_matrix.a21}, {adjoint_matrix.a22}]')

    def singular(self):
        determinant = ((self.a11 * self.a22) - (self.a21 * self.a12))
        if determinant == 0:
            print('It is singular Matrix')
        else:
            print('It is non-singular matrix')

    def null_matrix(self):
        if self.a11 == 0 and self.a12 == 0 and self.a21 == 0 and self.a22 == 0:
            print('It is a null matrix')
        else:
            print('It is not a null matrix')

    def identity_matrix(self):
        if self.a11 == 1 and self.a22 == 1 and self.a12 == 0 and self.a21 == 0:
            print('It is an identity matrix')
        else:
            print('It is not an identity matrix')

matrix1 = Mat2by2(1, 3, 5, 7)
matrix2 = Mat2by2(2, 4, 6, 8)
matrix1.add_matrix(matrix2)
matrix1.subtract_matrix(matrix2)
matrix1.scalar_multiple(4)
matrix1.transpose()
matrix1.determinant()
matrix1.multiply(matrix2)
matrix1.divide(matrix2)
matrix1.inverse()
matrix1.singular()
matrix1.identity_matrix()
matrix1.null_matrix()
