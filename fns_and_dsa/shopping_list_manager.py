def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    shopping_list = []

    while True:
        display_menu()
        # use strip to remove white spaces
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            item = input("Add item: ").strip()
            shopping_list.append(item)
            print(f"'{item}' has been added.")

        elif choice == '2':
            item = input("Remove item: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed.")
            else:
                print("Item not found in the list.")

        elif choice == '3':
            print("\nCurrent Shopping List:")
            if shopping_list:
                for index, value in enumerate(shopping_list, start=1):
                    print(f"{index}. {value}")
            else:
                print("List is empty.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number from 1 to 4.")


if __name__ == '__main__':
    print("Welcome to the Shopping List Manager!")
    main()
