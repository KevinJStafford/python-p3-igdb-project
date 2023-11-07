# lib/cli.py
from models.genre import Genre

# main menu
def main():
    while True:
        print("Welcome blurb")
        print("1. An option")
        print("2. Genre")
        print("3. Another option")
        print("------------------------------------------------")

        choice = input("Please select an option: ")
        if choice == "1":
            pass
        elif choice == "2":
            genre_menu()
        elif choice == "3":
            pass
        elif choice == "quit" or "help" or "im lost":
            print("Goodbye!")
            exit()
        else:
            print("That is invalid. Please select one of the menu options.")

# genre menu
def genre_menu():
    user_genre = Genre()
    while True:
        print('''
                      Genre Menu
              
        1. Add a genre          4. Find by id
        2. Delete by id         5. Find by name
        3. Delete by name       6. Get all genres
        
        Enter 0 to return to the previous menu.
        ------------------------------------------
        ''')
    
        choice = input("Please select an option: ")

        if choice == "1":
            print('You have selected "Add a genre".')
            param1 = input("Genre Name: ")
            param2 = input("Genre Description: ")
            user_genre.add_genre(param1, param2)

        elif choice == "2":
            print('You have selected "Delete by id".')
            param = input("Genre ID: ")
            user_genre.delete_by_id(param)

        elif choice == "3":
            print('You have selected "Delete by name".')
            param = input("Genre Name: ")
            user_genre.delete_by_name(param)

        elif choice == "4":
            print('You have selected "Find by id".')
            param = input("Genre ID: ")
            user_genre.find_by_id(param)

        elif choice == "5":
            print('You have selected "Find by name".')
            param = input("Genre Name: ")
            user_genre.find_by_name(param)

        elif choice == "6":
            print('You have selected "Get all genres".')
            user_genre.get_all_genres()

        elif choice == "0": 
            return
        
        elif choice == "quit" or "help" or "im lost":
            print("Goodbye!")
            exit()

        else:
            print("That is invalid. Please select one of the menu options.")
            

if __name__ == "__main__":
    main()
