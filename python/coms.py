import json
try:
    orders = {}

    def save_to(file, filepath):
        with open(filepath,'w') as fileobj:
            json_string = json.dumps(file)
            fileobj.write(json_string)

    def customer_orders():
        with open('orders.json', 'r') as file:
            orders_data = json.load(file)
            customer_name = input("Enter your name: ")
            while True:
                item = input("Enter the item you want to order or 'done' if you have finished: ")
                if item == "done":
                    break
                quantity = int(input("Enter the quantity: "))
                price = int(input("Enter the price: "))
            order_details = {"name": customer_name, "item": item, "quantity": quantity, "price": price}
            orders_data.append(order_details)
            save_to(orders_data, 'orders.json')
            print("Order placed successfully")

    def view_orders():
        with open('orders.json', 'r') as file:
            orders = json.load(file)
            print(orders)

    def total_price():
        with open('orders.json', 'r') as file:
            orders = json.load(file)
            total = 0
            for order in orders:
                total += order['price'] * order['quantity']
            print(total)

    def main():
        with open('orders.json', 'w') as file:
            file.write("[]")
        customer_orders()
        view_orders()
        total_price()
    main()
except Exception as e:
    print(f"You have encountered an error: {e}")


