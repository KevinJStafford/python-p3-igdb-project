# lib/cli.py
from helpers import (
    exit_program
)
from models.genre import Genre
from models.game import Game
from models.console import Console
from helper_functions.figure import show_image

# main menu
def main():
    show_image()
    while True:
        print("Welcome to the iGdb")
        print("1. Platform")
        print("2. Genre")
        print("3. Game")
        print("---------------------")

        choice = input("Please select an option: ")
        if choice == "1":
            console_menu()
        elif choice == "2":
            genre_menu()
        elif choice == "3":
            game_menu()
        elif choice == "quit" or "help" or "im lost":
            exit_program()
        else:
            print("That is invalid. Please select one of the menu options.")

# genre menu
def genre_menu():
    user_genre = Genre()
    while True:
        print('''
                      Genre Menu
              
        1. Add a genre          5. Find by name
        2. Delete by id         6. Get all genres
        3. Delete by name       7. Get all platforms
        4. Find by id
        
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
            user_genre.find_by_id(param)################################################

        elif choice == "5":
            print('You have selected "Find by name".')
            param = input("Genre Name: ")
            user_genre.find_by_name(param)

        elif choice == "6":
            print('You have selected "Get all genres".')
            user_genre.get_all_genres()

        elif choice == "7":
            param1 = input("Genre ID: ")
            user_genre.consoles(param1)

        elif choice == "0": 
            return
        
        elif choice == "quit" or "help" or "im lost":
            exit_program()

        else:
            print("That is invalid. Please select one of the menu options.")
            


# game menu
def game_menu():
    user_game = Game()
    while True:
        print('''
                      Games Menu
              
        1. Add a game                    
        2. Delete a game                 
        3. See all games
        
        
        Enter 0 to return to the previous menu.
        ------------------------------------------
        ''')

        choice = input("Please select an option: ")

        if choice == "1":
            print('''You've chosen to add a game to the database.
                   
                 Please be sure to add a platform type and genre type:
                  
                        PLATFORMS                       GENRES
                     PlayStation = 1       Action-adventure = 1   Strategy = 4
                     Xbox = 2              RPG = 2                Turn-based RPG = 5
                     PC = 3                Horror/Survival = 3    Puzzle = 6
                  ''' )
            param1 = input("Game Name: ")
            param2 = input("Platform: ")
            param3 = input("Genre: ")
            user_game.add_game(param1, param2, param3)

        elif choice == "2":
            print("You have chosen to delete a game")
            param = input("Game ID: ")
            user_game.delete_by_id(param)

        elif choice == "3":
            print("All the Games!")
            user_game.get_all_games()

        elif choice == "0":
            return
        
        elif choice == "quit" or "help" or "im lost":
            exit_program()

        else:
            print("Not a valid option. Please follow the menu options.")


# platform menu
def console_menu():
    user_console = Console()
    while True:
        print('''
                      Platform Menu
              
        1. Add a platform        5. Find by name
        2. Delete by id         6. Get all platform
        3. Delete by name       7. Get all genres
        4. Find by id
        
        Enter 0 to return to the previous menu.
        ------------------------------------------
        ''')

        choice = input("Please select an option:")
        if choice == "1":
            print('You have selected "Add a platform".')
            param1 = input("Platform Name: ")
            param2 = input("Platform Year Invented: ")
            user_console.add_console(param1, param2)

        elif choice == "2":
            print('You have selected "Delete by id".')
            param = input("Platform ID: ")
            user_console.delete_by_id(param)

        elif choice == "3":
            print('You have selected "Delete by name".')
            param = input("Platform Name: ")
            user_console.delete_by_name(param)

        elif choice == "4":
            print('You have selected "Find by id".')
            param = input("Platform ID: ")
            user_console.find_by_id(param)

        elif choice == "5":
            print('You have selected "Find by name".')
            param = input("Platform Name: ")
            user_console.find_by_name(param)

        elif choice == "6":
            print('You have selected "Get all platforms".')
            user_console.get_all_consoles()

        elif choice == "7":
            param1 = input("Platform ID: ")
            user_console.genres(param1)

        elif choice == "0": 
            return
        
        elif choice == "quit" or "help" or "im lost":
            exit_program()

        else:
            print("That is invalid. Please select one of the menu options.")
            

if __name__ == "__main__":
    main()

