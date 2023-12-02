# TASK 1
def main():
    tx=2
    ty=1
    tz=5
    mx=3
    my=-2
    mz=4
    bx=4
    by=-1
    bz=-2
    print(f't: ({tx},{ty},{tz})')
    print(f'm: ({mx},{my},{mz})')
    print(f'b: ({bx},{by},{bz})')
    print(f't+b: ({tx+bx},{ty+by},{tz+bz})')
def stp_calculate(tx,ty,tz,mx,my,mz,bx,by,bz):
    stp=tx*(my*bz-by*mz)-ty*(mx*bz-bx*mz)+tz*(mx*by-bx*my)
    print(f'stp:{stp}')
    print()

#TASK 2

def unit_vector(x,y,z):
    magnitude=(x**2+y**2+z**2)*0.5
    UnitVector=(x+y+z)/magnitude
    print(f'Unit Vector:{UnitVector}')

# TASK 3
def scalar_multiple(x,y,z):
    num=int(input('Number:'))
    scalarMultiple=x*num,y*num,z*num
    print(f'Scalar Multiple:{scalarMultiple}')

# TASK 4
def cross_product(ax,ay,az,bx,by,bz):
    x=(ay*bz-az*by)
    y=(ax*by-ay*bx)
    z=(ax*by-ay*bx)
    print(f'Cross Product:{x},{y},{z}')

# TASK 5
def equality_vector(x,y,z,X,Y,Z):
    if x==X and y==Y and z==Z:
        print('Vectors are equal')
    else:
        print('Vectors are not equal')


