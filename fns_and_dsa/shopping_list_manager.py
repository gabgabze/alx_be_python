# create a shopping list
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    """
    core functionalities are 
    add_items() - add items to shopping_list
    delete_items() - delete items from shopping_list
    display_items() - display items in shopping_list
    define an option display for the users to choose from
    """
    def main():
        shopping_list = []
        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                # Prompt for and add an item
                put_item = input("Add item: ")
                shopping_list.append(put_item)

            elif choice == '2':
                # Prompt for and remove an item
                remove_item = input("Remove item: ")
                if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
                elif remove_item not in shopping_list:
                    print("Item not found")
            elif choice == '3':
                # Display the shopping list
                print(shopping_list)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    request_option = input('What operation would you like to do? ')
print("Welcome to shopping list manager")
print(display_menu())