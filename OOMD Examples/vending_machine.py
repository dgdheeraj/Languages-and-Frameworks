class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: {self.price}"

class VendingMachine:
    def __init__(self, pwd):
        self.pwd = pwd
        self.balance = 0
        self.items = []

    def add_item(self, name, price, pwd):
        if pwd != self.pwd:
            print("Wrong Password!")
            return 

        item = Item(name, price)
        self.items.append(item)
        print(f"{name} item added!")

    def purchase_item(self, index, pay):
        if not 0<=index<len(self.items):
            print("Enter Valid Index")
            return
        
        item = self.items[index]
        total = item.price
        if pay < total:
            print(f"Insufficient Funds. Input Funds: {pay}, Expected Funds for {item.name}:{item.price}")
            return

        self.balance += pay
        self.items.pop(index)
        print(f"{item.name} bought!")

    def display_items(self):
        print("-------------------INVENTORY----------------------------")
        for i,item in enumerate(self.items):
            print(f"Number: {i}, Name: {item.name}, Price: {item.price}")
        print("--------------------------------------------------------")
    
    

machine = VendingMachine("password")
machine.add_item("Banana", 20, "password")
machine.add_item("Banana", 30, "password")
machine.display_items()
machine.purchase_item(1, 30)
machine.display_items()