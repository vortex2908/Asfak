# importing the required libraries

from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime


#connecting to database

mongoUrl = MongoClient("mongodb+srv://mohamedasfak2908_db_user:29082008@cluster0.angp8m0.mongodb.net/?appName=Cluster0")

#creating a database

db = mongoUrl["Ecommerce"]

#creating collections

userCollection = db["Users"]
productCollection = db["Products"]
orderCollection = db["Orders"]
adminCollection = db["Admins"]

#inserting new users with unique email 

def add_user(name, email, password,mobile,address):
    try:
        if userCollection.find_one({"email": email}):
            return "Email already exists"
        else:
            userCollection.insert_one(
                {
                    "name": name,
                    "email": email,
                    "password": password,
                    "mobile": mobile,
                    "address": address,
                    "created_at": datetime.now()
                }
            )
            return ""
    except Exception as e:
        return str(e)

def login_user(email, password):
    try:
        user = userCollection.find_one({"email": email, "password": password})
        if user:
            print("Login successful")
            options_after_Login(email)
        else:
            return "Invalid email or password"
    except FileNotFoundError as e:
        return str(e)
    except Exception as e:
        return str(e)

def options_after_Login(email):
    while True:
        choice = input("Enter what you want to do :\n "
        "1.Get all products\n " \
        "2.Order product \n " \
        "3.edit account \n " \
        "4.delete account \n " \
        "5.My Orders \n " \
        "6.Cancel Order \n " \
        "7.Logout \n \n ")
        if choice == "1":
            products = productCollection.find()
            for product in products:
                print(f"Product ID: {product['_id']}\n Name:{product['name']} \n Price : {product['price']} \n Model: {product['model']} \n Color: {product['color']} \n  Stock: {product['stock']} \n Discount: {product['discount']} \n \n")
        elif choice == "2":
            order_product(email)
        elif choice == "3":
            details = userCollection.find_one({"email": email})
            print(f"Name: {details['name']}\nEmail: {details['email']}\nMobile: {details['mobile']}\nAddress: {details['address']}")
            choose = input("Enter what you want to edit :\n 1.Name \n 2.Password \n 3.Mobile \n 4.Address")
            if choose == "1":
                new_name = input("Enter new name: ")
                userCollection.find_one_and_update({"email":email},{"$set":{"name":new_name}})
                print("Name updated successfully")
            elif choose == "2":
                new_password = input("Enter new password: ")
                userCollection.find_one_and_update({"email":email},{"$set":{"password":new_password}})
                print("Password updated successfully")
            elif choose == "3":
                new_mobile = input("Enter new mobile number: ")
                userCollection.find_one_and_update({"email":email},{"$set":{"mobile":new_mobile}})
                print("Mobile number updated successfully")
            elif choose == "4":
                new_address = input("Enter new address: ")
                userCollection.find_one_and_update({"email":email},{"$set":{"address":new_address}})
                print("Address updated successfully")
        elif choice == "4":
            userCollection.find_one_and_delete({"email": email})
            print("Account deleted successfully")
            break
        elif choice == "5":
            view_my_orders(email)
        elif choice == "6":
            cancel_order(email)
        elif choice == "7":
            print("Logged out successfully")
            break

def cancel_order(email):
    order_id_input = input("Enter the Order ID you want to cancel: ")
    try:
        order_id = ObjectId(order_id_input)
    except Exception:
        print("Invalid Order ID")
        return

    order = orderCollection.find_one({"_id": order_id, "user_email": email})
    if not order:
        print("Order not found or you don't have permission to cancel this order")
        return

    if order['status'] != "Pending":
        print("Only pending orders can be cancelled")
        return

    productCollection.update_one({"_id": order["product_id"]}, {"$inc": {"stock": order["quantity"]}})
    orderCollection.find_one_and_delete({"_id": order_id})
    print("Order cancelled successfully")

def view_my_orders(email):
    """Shows the order history for the currently logged-in user."""
    orders = orderCollection.find({"user_email": email})
    found = False
    for order in orders:
        found = True
        print_order(order)
    if not found:
        print("You haven't placed any orders yet")


def order_product(email):
    """Lets a logged-in user place an order for a product."""
    products = list(productCollection.find())
    if not products:
        print("No products available right now")
        return

    for product in products:
        print(f"Product ID: {product['_id']}\n Name:{product['name']} \n Price : {product['price']} \n Model: {product['model']} \n Color: {product['color']} \n  Stock: {product['stock']} \n Discount: {product['discount']} \n \n")

    product_id_input = input("Enter the Product ID you want to order: ")
    try:
        product_id = ObjectId(product_id_input)
    except Exception:
        print("Invalid Product ID")
        return

    product = productCollection.find_one({"_id": product_id})
    if not product:
        print("Product not found")
        return

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Quantity must be a number")
        return

    if quantity <= 0:
        print("Quantity must be at least 1")
        return

    try:
        stock = int(product.get("stock", 0))
    except (TypeError, ValueError):
        stock = 0

    if quantity > stock:
        print(f"Only {stock} unit(s) in stock")
        return

    try:
        price = float(product.get("price", 0))
    except (TypeError, ValueError):
        print("This product has an invalid price and can't be ordered. Please contact support.")
        return
    try:
        discount = float(product.get("discount", 0) or 0)
    except (TypeError, ValueError):
        discount = 0.0

    unit_price = round(price - (price * discount / 100), 2)
    total_price = round(unit_price * quantity, 2)

    user = userCollection.find_one({"email": email})
    shipping_address = user.get("address", "") if user else ""

    order = {
        "user_email": email,
        "product_id": product["_id"],
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": unit_price,
        "total_price": total_price,
        "status": "Pending",
        "shipping_address": shipping_address,
        "order_date": datetime.now()
    }

    result = orderCollection.insert_one(order)
    productCollection.update_one({"_id": product["_id"]}, {"$inc": {"stock": -quantity}})

    print(f"\nOrder placed successfully!\n Order ID: {result.inserted_id}\n Product: {product['name']}\n Quantity: {quantity}\n Total Price: {total_price}\n Status: Pending\n")


def print_order(order):
    print(f"Order ID: {order['_id']}\n User: {order['user_email']}\n Product: {order['product_name']}\n Quantity: {order['quantity']}\n Unit Price: {order.get('unit_price', '')}\n Total Price: {order['total_price']}\n Status: {order['status']}\n Shipping Address: {order['shipping_address']}\n Order Date: {order['order_date']}\n \n")


def view_all_orders():
    orders = orderCollection.find()
    found = False
    for order in orders:
        found = True
        print_order(order)
    if not found:
        print("No orders found")


def view_orders_by_user():
    user_email = input("Enter the user email: ")
    orders = orderCollection.find({"user_email": user_email})
    found = False
    for order in orders:
        found = True
        print_order(order)
    if not found:
        print("No orders found for this user")


def view_orders_by_product():
    product_id_input = input("Enter the Product ID: ")
    try:
        product_id = ObjectId(product_id_input)
    except Exception:
        print("Invalid Product ID")
        return
    orders = orderCollection.find({"product_id": product_id})
    found = False
    for order in orders:
        found = True
        print_order(order)
    if not found:
        print("No orders found for this product")


def update_order_status():
    order_id_input = input("Enter the Order ID: ")
    try:
        order_id = ObjectId(order_id_input)
    except Exception:
        print("Invalid Order ID")
        return

    order = orderCollection.find_one({"_id": order_id})
    if not order:
        print("Order not found")
        return

    print(f"Current status: {order['status']}")
    new_status = input("Enter new status (Pending/Shipped/Delivered/Cancelled): ")
    orderCollection.find_one_and_update({"_id": order_id}, {"$set": {"status": new_status}})
    print("Order status updated successfully")


def admin_options():
    while True:
        choice = input("Enter what you want to do :\n "
                        "1.Add product\n " \
                        "2.Update product \n " \
                        "3.Delete product \n " \
                        "4.view all Products \n " \
                        "5.view specific product \n " \
                        "6.view all users \n " \
                        "7.view specific user \n " \
                        "8.Remove user \n " \
                        "9.view all orders \n " \
                        "10.view specific order by user \n "\
                        "11.view specific order by product \n "\
                        "12.Update order status \n"\
                        "13.logout \n" )
        if choice == "1":
            print("Adding product")
            name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: "))
            except ValueError:
                print("Price must be a number. Product not added.")
                continue
            model = input("Enter product model: ")
            color = input("Enter product color: ")
            try:
                stock = int(input("Enter product stock: "))
            except ValueError:
                print("Stock must be a whole number. Product not added.")
                continue
            discount_input = input("Enter product discount (%) [leave blank for 0]: ").strip()
            try:
                discount = float(discount_input) if discount_input else 0.0
            except ValueError:
                print("Discount must be a number. Product not added.")
                continue
            productCollection.insert_one({
                "name": name,
                "price": price,
                "model": model,
                "color": color,
                "stock": stock,
                "discount": discount,
            })
            print("Product added successfully")
        elif choice == "2":
            print("Updating product")
            product_id_input = input("Enter the product id you want to update: ")
            try:
                product_id = ObjectId(product_id_input)
            except Exception:
                print("Invalid Product ID")
                continue
            details = productCollection.find_one({"_id": product_id})
            if not details:
                print("Product not found")
                continue
            print(f"Name: {details['name']}\n Price: {details['price']}\n Model: {details['model']}\n Color: {details['color']}\n Stock: {details['stock']}\n Discount: {details['discount']}")
            while True:
                choose = input("Enter what you want to edit :\n 1.Name \n 2.Price \n 3.Model \n 4.Color \n 5.Stock \n 6.Discount \n 7.Done \n")
                if choose == "1":
                    new_name = input("Enter new name: ")
                    productCollection.find_one_and_update({"_id": product_id}, {"$set":{"name": new_name}})
                    print("Name updated successfully")
                elif choose == "2":
                    try:
                        new_Price = float(input("Enter new Price: "))
                    except ValueError:
                        print("Price must be a number")
                        continue
                    productCollection.find_one_and_update({"_id":product_id},{"$set":{"price":new_Price}})
                    print("Price updated successfully")
                elif choose == "3":
                    new_model = input("Enter new model: ")
                    productCollection.find_one_and_update({"_id": product_id},{"$set":{"model":new_model}})
                    print("Model updated successfully")
                elif choose == "4":
                    new_color = input("Enter new color: ")
                    productCollection.find_one_and_update({"_id": product_id},{"$set":{"color":new_color}})
                    print("Color updated successfully")
                elif choose == "5":
                    try:
                        new_stock = int(input("Enter new stock: "))
                    except ValueError:
                        print("Stock must be a whole number")
                        continue
                    productCollection.find_one_and_update({"_id": product_id},{"$set":{"stock":new_stock}})
                    print("Stock updated successfully")
                elif choose == "6":
                    try:
                        new_discount = float(input("Enter new discount (%): "))
                    except ValueError:
                        print("Discount must be a number")
                        continue
                    productCollection.find_one_and_update({"_id": product_id},{"$set":{"discount":new_discount}})
                    print("Discount updated successfully")
                elif choose == "7":
                    break
        elif choice == "3":
            print("Deleting product")
            product_id_input = input("Enter the product id you want to delete: ")
            try:
                product_id = ObjectId(product_id_input)
            except Exception:
                print("Invalid Product ID")
                continue
            productCollection.find_one_and_delete({"_id": product_id})
            print("Product deleted successfully")
        elif choice == "4":
            products = productCollection.find()
            for product in products:
                print(f"Product ID: {product['_id']}\n Name:{product['name']} \n Price : {product['price']} \n Model: {product['model']} \n Color: {product['color']} \n  Stock: {product['stock']} \n Discount: {product['discount']} \n \n")
        elif choice == "5":
            product_id_input = input("Enter the product id you want to view: ")
            try:
                product_id = ObjectId(product_id_input)
            except Exception:
                print("Invalid Product ID")
                continue
            details = productCollection.find_one({"_id": product_id})
            if not details:
                print("Product not found")
                continue
            print(f"Name: {details['name']}\n Price: {details['price']}\n Model: {details['model']}\n Color: {details['color']}\n Stock: {details['stock']}\n Discount: {details['discount']}")
        elif choice == "6":
            users = userCollection.find()
            for user in users:
                print(f"Name: {user['name']}\n Email: {user['email']}\n Mobile: {user['mobile']}\n Address: {user['address']}\n Created at: {user['created_at']}\n \n")
        elif choice == "7":
            user_email = input("Enter the user email you want to view: ")
            details = userCollection.find_one({"email": user_email})
            if not details:
                print("User not found")
                continue
            print(f"Name: {details['name']}\n Email: {details['email']}\n Mobile: {details['mobile']}\n Address: {details['address']}\n Created at: {details['created_at']}\n \n")
        elif choice == "8":
            user_email = input("Enter the user email you want to remove: ")
            userCollection.find_one_and_delete({"email": user_email})
            print("User removed successfully")
        elif choice == "9":
            view_all_orders()
        elif choice == "10":
            view_orders_by_user()
        elif choice == "11":
            view_orders_by_product()
        elif choice == "12":
            update_order_status()
        elif choice == "13":
            print("Logged out successfully")
            break

def add_admin(name, email, password, mobile):
    try:
        if adminCollection.find_one({"email": email}):
            return "Email already exists"
        else:
            adminCollection.insert_one(
                {
                    "name": name,
                    "email": email,
                    "password": password,
                    "mobile": mobile,
                    "role": "admin",
                    "created_at": datetime.now()
                }
            )
            return "Admin added successfully"
    except Exception as e:
        return str(e)

def admin_login(admin_email, admin_password):
    try:
        user = adminCollection.find_one({"email": admin_email, "password": admin_password})
        if user:
            print("Login successful")
            admin_options()
        else:
            return "Invalid email or password"
    except FileNotFoundError as e:
        return str(e)
    except Exception as e:
        return str(e)


def main():
    while True:
        choice = input("Enter what you want to do :\n 1.Sign up \n 2.Log in \n 3.Get all products \n 4.exit \n")
        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            mobile = input("Enter your mobile number: ")
            address = input("Enter your address: ")
            message = add_user(name, email, password,mobile,address)
            if message:
                print(message)
            else:
                login_user(email, password)
        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            result = login_user(email, password)
            if result:
                print(result)
        elif choice == "3":
            products = productCollection.find()
            for product in products:
                print(f"Product ID: {product['_id']} \n Name:{product['name']} \n Price : {product['price']} \n Model: {product['model']} \n Color: {product['color']} \n  Stock: {product['stock']} \n Discount: {product['discount']} \n \n")
        elif choice == "4":
            print("Exiting the program")
            break
        elif choice == "5":
            admin_email = input("Enter admin email:")
            admin_password = input("Enter admin password:")
            result = admin_login(admin_email, admin_password)
            if result:
                print(result)
        elif choice == "6":
            admin_name = input("Enter admin name:")
            admin_email = input("Enter admin email:")
            admin_password = input("Enter admin password:")
            admin_mobile = input("Enter admin mobile number:")
            print(add_admin(admin_name, admin_email, admin_password, admin_mobile))
main()