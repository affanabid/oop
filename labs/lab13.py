class NUMBERS:

    def __init__(self):
        self.numbers = []
        self.even_numbers = []
        self.odd_numbers = [] 

    def add_number(self, number):
        if type(number) == int or type(number) == float:
            self.numbers.append(number)
            if number % 2 == 0:
                self.even_numbers.append(number)
            else:
                self.odd_numbers.append(number)
        else:
            print("Please enter a valid number (int or float).")

    def delete_number(self, number):
        if number in self.even_numbers:
            self.even_numbers.remove(number)
            self.numbers.remove(number)
        elif number in self.odd_numbers:
            self.odd_numbers.remove(number)
            self.numbers.remove(number)

        else:
            print("Number not found.")

    def alter_number(self, old_number, new_number):
        if old_number in self.numbers:
            index = self.numbers.index(old_number)
            self.numbers[index] = new_number
            if old_number in self.even_numbers:
                if new_number % 2 == 0:
                    index = self.even_numbers.index(old_number)
                    self.even_numbers[index] = new_number
                else:
                    print('You can change an even number with an even number and not with any odd number.')
            elif old_number in self.odd_numbers:
                if new_number % 2 != 0:
                    index = self.odd_numbers.index(old_number)
                    self.odd_numbers[index] = new_number
                else:
                    print('You can change an odd number with an odd number and not with any even number.')
        else:
            print("Number not found.")

    def search_number(self, number):
        fail = True
        for i in range(len(self.numbers)):
            if self.numbers[i] == number:
                print(f"Number {number} found at {i}th index.")
                fail = False
        if fail:
            print(f"Number {number} not found.")

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.even_numbers):
            result = self.even_numbers[self.current_index]
            self.current_index += 1
            return result
        elif self.current_index < len(self.odd_numbers) + len(self.even_numbers):
            result = self.odd_numbers[self.current_index - len(self.even_numbers)]
            self.current_index += 1
            return result
        else:
            raise StopIteration
        
    def __getitem__(self, index):
        if index < len(self.numbers):
            return self.numbers[index]
        else:
            raise IndexError

    def __setitem__(self, index, value):
        if index < len(self.numbers):
            self.numbers[index] = value
        else:
            raise IndexError
        
    def print_numbers(self):
        print('Numbers: ',self.numbers)

    def show_even_numbers(self):
        print('Even Numbers: ', self.even_numbers)
    
    def show_odd_numbers(self):
        print('Odd numbers: ',self.odd_numbers)

def main():
    numbers = NUMBERS()

    numbers.add_number(3)
    numbers.add_number(1)
    numbers.add_number(9)
    numbers.add_number(7)
    numbers.add_number(5)
    numbers.add_number(4)
    numbers.add_number(8)
    numbers.add_number(0)

    numbers.delete_number(0)
    numbers.delete_number(3)
    numbers.delete_number(4)

    numbers.search_number(2)
    numbers.search_number(6)
    numbers.search_number(8)

    numbers.alter_number(7, 1)
    numbers.alter_number(4, 6)
    numbers.alter_number(9, 2)

    print(numbers.__getitem__(2))
    print(numbers.__getitem__(5))
    print(numbers.__getitem__(9))

    numbers.__setitem__(2, 2)
    numbers.__setitem__(0, 8)
    numbers.__setitem__(9, 0)

    numbers.print_numbers()
    numbers.show_even_numbers()
    numbers.show_odd_numbers()

if __name__ == "__main__":
    main()
