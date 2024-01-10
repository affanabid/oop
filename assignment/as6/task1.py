import math

class Vector:
    def __init__(self, components):
        self.components = tuple(components)

    def __len__(self):
        return len(self.components)

    def __getitem__(self, index):
        return self.components[index]

    def __repr__(self):
        return f"Vector{self.components}"

    def __eq__(self, other):
        for i in range(len(self.components)):
            if self.components[i] != other.components[i]:
                return 'Unequal'
        return 'Equal'
        # e = 0
        # for i in range(len(self.components)):
        #     if self.components[i] == other.components[i]:
        #         e += 1
        # if e == len(self.components):
        #     print('Both vectors are equal')
        # else:
        #     print('Both vectors are unequal')

    def magnitude(self):
        mag = 0
        for comp in self.components:
            mag += comp ** 2
        magnitude = round(math.sqrt(mag),2)
        return magnitude

    def dot_product(self, other):
        dp = 0
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for dot product calculation.")
        for i in range(len(self.components)):
            dp += self.components[i] * other.components[i]
        return dp

    def scalar_multiply(self, scalar):
        sm = []
        for comp in self.components:
            sm.append(comp * scalar)
        return tuple(sm)

    def add(self, other):
        sum = []
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition.")
        for i in range(len(self.components)):
            sum.append(self.components[i] + other.components[i])
        return sum

    def subtract(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        diff = []
        for i in range(len(self.components)):
            diff.append(self.components[i] - other.components[i])
        return diff
    
    def cross_product(self, other):
        if len(self.components) != 3 or len(other.components) != 3:
            raise ValueError("Cross product is defined for 3D vectors only.")
        i = self.components[1] * other.components[2] - self.components[2] * other.components[1]
        j = self.components[2] * other.components[0] - self.components[0] * other.components[2]
        k = self.components[0] * other.components[1] - self.components[1] * other.components[0]
        return Vector([i, j, k])

v1 = Vector([1, 2, 3])
v2 = Vector([1, 2, 3])
print(v1.__eq__(v2))
# v1.__eq__(v2)

# print("Magnitude of v1:", v1.magnitude()) 

# print("Dot product of v1 and v2:", v1.dot_product(v2))

# print("Scalar multiplication of v1 by 2:", v1.scalar_multiply(2)) 

# print("Addition of v1 and v2:", v1.add(v2))

# print("Subtraction of v1 from v2:", v2.subtract(v1))  

# print(v2.cross_product(v1))


# Testing for different dimensional vectors
def test_2d_vector():
    v1 = Vector([3, 4])
    v2 = Vector([5, 6])

    if v1.magnitude() == 5.0 and v1.dot_product(v2) == 39:
        return True
    else:
        return False

def test_3d_vector():
    v1 = Vector([1, 2, 3])  

    if v1.magnitude() == round(math.sqrt(14), 2) and v1.dot_product(v1) == 14:
        return True
    else:
        return False

def test_4d_vector():
    v1 = Vector([1, 2, 3, 4])
    v2 = Vector([5, 6, 7, 8])

    if v1.magnitude() == round(math.sqrt(30), 2) and v1.dot_product(v2) == 70:
        return True
    else:
        return False
    
def test_5d_vector():
    v1 = Vector([1, 2, 3, 4, 5])
    v2 = Vector([6, 7, 8, 9, 10])

    if v1.magnitude() == round(math.sqrt(55), 2) and v1.dot_product(v2) == 130:
        return True
    else:
        return False

def run_tests():
    test = 0
    fail = 4
    
    if test_2d_vector():
        test += 1
        fail -= 1
    if test_3d_vector():
        test += 1
        fail -= 1
    if test_4d_vector():
        test += 1
        fail -= 1
    if test_5d_vector():
        test += 1
        fail -= 1

    if test == 4:
        print("All tests passed!")
    elif test == 0:
        print('All Tests failed!')
    else:
        print(f'{test} Tests passed and {fail} failed!')
    
# run_tests()
