#Task-01
def main():
    t_x = 2
    t_y = 1
    t_z = 5
    m_x = 3
    m_y = -2
    m_z = 4
    b_x = 4
    b_y = -1
    b_z = -2
    print(f't: ({t_x},{t_y},{t_z})')
    print(f'm: ({m_x},{m_y},{m_z})')
    print(f'b: ({b_x},{b_y},{b_z})')
    print(f't+b: ({t_x+b_x},{t_y+b_y},{t_z+b_z})')

def stp_calculate(t_x,t_y,t_z,m_x,m_y,m_z,b_x,b_y,b_z):
    stp = t_x * (m_y * b_z - b_y * m_z) - t_y * (m_x * b_z - b_x * m_z) + t_z * (m_x * b_y - b_x * m_y)
    print(f'Scalar Triple Product:{stp}')

#Task-02
def unit_vector(x,y,z):
    d = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    print(f'Unit Vector: {x/d + y/d + z/d}')

#Task-03
def scalar_multiple(x,y,z):
    num=int(input('Scalar Multiple : '))
    print(f'{x * num} , {y * num} , {z * num}')

#Task-04
def cross_product(ax,ay,az,bx,by,bz):
    x = (ay * bz - az * by)
    y = (ax * by - ay * bx)
    z = (ax * by - ay * bx)
    print(f'Cross Product: {x}, {y}, {z}')

#Task-05
def equality_of_vectors(a_x,a_y,a_z,b_x,b_y,b_z):
    if a_x == b_x and a_y == b_y and a_z == b_z:
        print('Vectors are equal')
    else:
        print('Vectors are not equal')

main()
stp_calculate(t_x = 2, t_y = 1, t_z = 5, m_x = 3, m_y = -2, m_z = 4, b_x = 4, b_y = -1, b_z = -2)
scalar_multiple(4, 8, 2)
unit_vector(x=5, y=2, z=8)
cross_product(2, 5, 3, 1, 8, 5)
equality_of_vectors(2, 1, 4, 2, 1, 4)