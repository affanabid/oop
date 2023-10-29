from datetime import datetime

# ----------------------------------------------------customer.py
# Class for the customer details
class Customer:

    def __init__(self, customer_name, customer_address):
        self.__name = customer_name
        self.address = customer_address

    def get_name(self):
        return self.__name
# -----------------------------------------------------itemslist.py
# Class for the list of items bought and their properties
class ItemsList:

    def __init__(self, particular, rate, quantity):
        self.__particular = particular
        self.__unitprice = rate
        self.__quantity = quantity
        self.amount = self.__unitprice*self.__quantity

    def __str__(self):
        return f"{self.__particular}\t\t{self.__unitprice}\t\t{self.__quantity}\t\t{self.amount}"

# ------------------------------------------------------address.py
# A class for the address of the shop
class Address:

    def __init__(self, shop_number, floor, building, city, country) -> None:
        self.shop_no = shop_number
        self.floor = floor
        self.building = building
        self.city = city
        self.country = country

    def __str__(self) -> str:
        return f'Shop # {self.shop_no}, Floor {self.floor}, {self.building}, {self.city}, {self.country}'

# -------------------------------------------------------bill.py
# Class for the bill characterisitcs
class Bill:

    def __init__(self, bill_number, customer_name, customer_address):
        self.__no = str(bill_number)
        date = datetime.now()
        self.date = date.strftime("%d/%m/%Y")
        self.customer = Customer(customer_name, customer_address) 
        self.customer_name = self.customer.get_name()
        self.customer_address = self.customer.address
        
    def __str__(self) -> str:
        return f'''Mobile Shop\nCell_no: 0300-1234567\n\nNo: {self.__no}\nDate: {self.date}\nCustomer Name: {self.customer_name}\nCustomer Address: {self.customer_address}'''

def main():
    bill = Bill(bill_number=1,customer_name='Mike', customer_address='Manchester, UK')
    print(bill)
    print()
    items = [
        ItemsList('Egg', 20, 12),
        ItemsList('Noodles', 50, 2),
        ItemsList('Water', 15, 6),
        ItemsList('Candy', 50, 10),
    ]
    print('Particulars\tRate\t\tQuantity\tAmount')
    total = 0
    for item in items:
        total += item.amount
        print(item)
    print('\t\t\t\t\tTotal:', total) #printing total amount
    print('Signature: _________________')
    address = Address(shop_number=5, floor=2, building='Clock Tower',city='Manchester', country='UK')
    print('Address: ',address)

if __name__ == '__main__':
    main()