#receipt system
#collect customer's name
#collect order
#show orders
#show total order price
import json
from datetime import datetime


try:
    def save_to(file_o, filepath):
        with open(filepath, 'w') as file:
            json.dump(file_o,file)

    def read_from(filepath):
        with open (filepath) as file:
            customers_ = json.load(file)
            return customers_

    def take_orders():
        with open ("customer_orders.json", 'r') as file:
            customers_ = json.load(file)
            print(type(customers_))

            customer_ = {}
            orders = []
            name = input("Enter your name: ")
            while True:
                order = input ("Enter item or 'done' when you finish: ")
                if order == 'done':
                    break
                item_name = order
                quantity = input ("Enter quantity: ")
                price = input ("Enter price: ")
                time = datetime.now().time().strftime("%H:%M:%S")
                order = {'item_name': item_name, 'quantity': quantity, 'price': price, 'time':str(time)}
                orders.append(order)
                customer_[name] = orders
                customers_.append(customer_)
            print(customers_)
            save_to(customers_, "customer_orders.json")
                

    def show_order():
        try:
            customers_ = read_from("customer_orders.json")
        except Exception:
            print("No customers yet")
        else:
            name = input("Enter customer name: ")
            for customer in customers_:
                if customer.get(name):
                    customer = customer.get(name)
                    print(f"Hello {name}, here is your order receipt: ")
                    x = 0
                    total_order = []
                    for orders in customer:
                        item_name = orders["item_name"]
                        quantity = int(orders["quantity"])
                        price = float(orders["price"])
                        total = price * quantity
                        time = orders["time"]
                        total_order.append(total)
                        print(f"-" * 10)
                        print(f"item: {item_name}")
                        print(f"quantity: {quantity}")
                        print(f"Unit price: {price}")
                        print(f"Total: {total}")
                        print(f"Time of order: {time}")
                        x += 1
                    print(f"You have {x} item(s) in cart and the total is: N{sum(total_order)}")
                    break
            else:
                    print ("Name not found")

            """for customer in customers_:
                for name , orders in customer.items():
                    print(name, orders)"""

    def main():
        print("Welcome to our amazing store")
        choice = input("Enter: \n 1 to take order \n 2 to see orders \n")
        if choice == "1":
            if read_from("customer_orders.json"):
                take_orders()
            else:
                with open('customer_orders.json', 'w') as file:
                    file.write("[]")
                    take_orders()
        elif choice == "2":
            show_order()

    try:
        main()
    except:
        pass
except Exception as e:
    print(e)