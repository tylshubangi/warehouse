import time
class warehouse:
    def __init__(self):
        self.items={}
        self.quantity = {"book": 5, "pen":5, "pencil": 5}
    def register(self, item_name, r_quantity):
        if self.quantity[item_name] <=0:
            print("Out of stock. Refilling in 3 seconds")
            time.sleep(3)
            self.quantity[item_name] = 5
            print("added "+ str(self.quantity[item_name]) +" "+ item_name+"s")
            self.items[item_name]+=r_quantity
        elif item_name not in self.items:
            if r_quantity > 5:
                self.items[item_name] = 5
                self.quantity[item_name] -= 5
                print("Out of stock. Refilling in 3 seconds")
                time.sleep(3)
                self.quantity[item_name] = 5
                self.items[item_name]+=(r_quantity-5)
            print("registering " + str(r_quantity)+ " " +item_name+"s"+ " in 1s")
            time.sleep(1)
            self.items[item_name] = r_quantity
            self.quantity[item_name] -= r_quantity
        else:
            print("registering " + str(r_quantity)+ " " +item_name+"s"+ " in 1s")
            time.sleep(1)
            self.items[item_name] += r_quantity
            self.quantity[item_name] -=r_quantity
        
        
    def get_cart_items(self):
        cart_items = self.items
        print(cart_items)
house = warehouse()
house.register('book',3)
house.register('book',2)
house.register('book',1)
house.register('book',1)
house.register('pen',7)
house.register('pen',2)
house.get_cart_items()

        