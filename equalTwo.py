# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a

# a[0] = 5

# print(a)
# print(b)
# #print(c)
class Electronic:
    def _init_(self, name, brand, price, quantity):
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity


    electronic1 = Electronic("Laptop","Dell",1200,5)
    electronic2 = Electronic("Smartphone","Samsung",800,10)
    electronic3 = Electronic("Headphones","Apple",200,30)


    print(electronic1)
    print(electronic2)
    print(electronic3)
