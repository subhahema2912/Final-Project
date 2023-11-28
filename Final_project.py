# main.py
from food_ordering_operations import FoodOrderingApp, User, Admin

def main():
    app = FoodOrderingApp()

    while True:
        print("Welcome to the Food Ordering App")
        print("1. Admin Login")
        print("2. Admin Register")
        print("3. User Register")
        print("4. User Login")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            admin_username = input("Enter admin username: ")
            admin_password = input("Enter admin password: ")
            authenticated_admin = app.admin.login(admin_username, admin_password)
            if authenticated_admin:
                admin_menu(app)
            else:
                print("Admin authentication failed.")

        elif choice == "2":
            full_name = input("Enter your full name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Enter your password: ")
            app.admin.register(full_name, phone_number, email, address, password)

        elif choice == "3":
            full_name = input("Enter your full name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your email: ")
            address = input("Enter your address: ")
            password = input("Enter your password: ")
            app.user.register(full_name, phone_number, email, address, password)

        elif choice == "4":
            user_email = input("Enter your email: ")
            user_password = input("Enter your password: ")
            authenticated_user = app.user.login(user_email, user_password)
            if authenticated_user:
                user_menu(app)
            else:
                print("User authentication failed.")

        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def admin_menu(app):
    while True:
        print("Admin Menu:")
        print("1. Add new food item")
        print("2. Edit food item")
        print("3. View food menu")
        print("4. Remove food item")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            app.admin.add_food_item()
        elif choice == "2":
            app.admin.edit_food_item()
        elif choice == "3":
            app.admin.view_food_menu()
        elif choice == "4":
            app.admin.remove_food_item()
        elif choice == "5":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(app):
    while True:
        print("User Menu:")
        print("1. Place New Order")
        print("2. Order History")
        print("3. Update Profile")
        print("4. Logout")
        choice = input("Enter your choice: ")

        if choice == "1":
            app.user.place_order()
        elif choice == "2":
            app.user.view_order_history()
        elif choice == "3":
            app.user.update_profile()
        elif choice == "4":
            print("User logged out.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()