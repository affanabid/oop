from random import randint

class Teenda:

    def __init__(self, c, d):
        self.category = c
        self.data = d
        self.alive = True

    @property
    def category(self):  # 3 or 5
        return self.__cat

    @category.setter
    def category(self, c):
        self.__cat = c
    
    def  __str__(self):
        string = '<'
        for i in range(int(self.category)):
            string += str(self.data[i])
            if i != (self.category-1):
                string += ','
        string += '>'
        return string

    def valid(self):
        valid = False
        if self.category == 3 and self.data[1] > self.data[0] and self.data[0] > self.data[2]:
            valid = True
        elif self.category == 5 and self.data[2] > self.data[1] and self.data[1] > self.data[3] and self.data[0] > self.data[4]:
            valid = True
        return valid

    def die(self):
        self.alive = False

    def mutate(self):
        choice = randint(0, 1)
        if choice == 1:
            if self.category == 3:
                self.grow()
            else:
                print('growth mutation not posssible')
        else:
            if self.category == 5:
                self.split()
            else:
                print('split mutation not possible')

    def grow(self):
        if self.category == 3:
            print(f'Growing... ', end='')
            
            self.data.insert(1, 0)
            self.data.insert(3, 0)
            self.data[1] = (self.data[0] + self.data[2]) // 2
            self.data[3] = (self.data[2] + self.data[4]) // 2
            grown_teenda = Teenda(5,self.data)
            if grown_teenda.valid():
                
                print(grown_teenda)
            else:
                grown_teenda.die()
                print('growth requirements not fulfilled')
        else:
            pass
        
    def split(self):
        if self.category == 5:
            print(f'Splitting... ', end='')
            half_of_middle = self.data[2] // 2
            splitted_t1 = Teenda(3, [self.data[0], self.data[1], half_of_middle])
            splitted_t2 = Teenda(3, [half_of_middle, self.data[3], self.data[4]])
            if splitted_t1.valid() == False:
                splitted_t1.die()
            if splitted_t2.valid() == False:
                splitted_t2.die()
            
            if splitted_t1.alive and splitted_t2.alive:
                print(f'{splitted_t1} and {splitted_t2}')
            elif splitted_t1.alive and not splitted_t2.alive:
                print(splitted_t1)
            elif not splitted_t1.alive and splitted_t2.alive:
                print(splitted_t2)
            else:
                print('split requirements not fulfilled')
            
        else:
            return []

def main():
    teendas = []
    t1 = Teenda(3, [4,10,2])
    t2 = Teenda(5, [23, 35, 40, 30, 21])
    teendas.append(t1)
    teendas.append(t2)
    n = 1
    while n <= 1:
        print(f'Iteration no. {n}')
        for teenda in teendas:
            print(f'T{teenda.category}: {teenda}')
            teenda.mutate()
        print()
        
        n += 1
main()