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
        print("Welcome blurb")
        print("1. An option")
        print("2. Genre")
        print("3. Game")
        print("------------------------------------------------")

        choice = input("Please select an option: ")
        if choice == "1":
            pass
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
            exit_program()

        else:
            print("That is invalid. Please select one of the menu options.")
            


# game menu
def game_menu():
    user_game = Game()
    while True:
        print('''
                      Games Menu
              
        1. Add a game                    2. See all games
        3. Delete a game                 4. Find game genres by consoles
        5. Find consoles by game genre
        
        Enter 0 to return to the previous menu.
        ------------------------------------------
        ''')

        choice = input("Please select an option: ")

        if choice == "1":
            print('''You've chosen to add a game to the database.
                   
                 Please be sure to add a console type and genre type:
                  
                     CONSOLES                               GENRES
                     PlayStation = 1       Action-adventure = 1   Strategy = 4
                     Xbox = 2              RPG = 2                Turn-based RPG = 5
                     PC = 3                Horror/Survival = 3    Puzzle = 6
                  ''' )
            param1 = input("Game Name: ")
            param2 = input("Console: ")
            param3 = input("Genre: ")
            user_game.add_game(param1, param2, param3)

        elif choice == "2":
            print("All the Games!")
            user_game.get_all_games()

        elif choice == "3":
            print("You have chosen to delete a game, please enter the Game's ID: ")
            user_game.delete_by_id()

        elif choice == "4":
            print('''Please select a console:
                   CONSOLES
                PlayStation
                Xbox
                PC
                  ''')
            param1 = input("Console: ")
            user_game.consoles(param1)

        elif choice == "5":
            print('''Please select a genre:
                             GENRES
                    Action-adventure   Strategy
                    RPG                Turn-based RPG
                    Horror/Survival    Puzzle''')
            param1 = input("Genre: ")
            user_game.genres(param1)

        elif choice == "0":
            return
        
        elif choice == "quit" or "help" or "im lost":
            exit_program()

        else:
            print("Not a valid option. Please follow the menu options.")


# console menu
def console_menu():
    user_console = Console()
    while True:
        print('''
                      Console Menu
              
        1. Add a console          4. Find by id
        2. Delete by id         5. Find by name
        3. Delete by name       6. Get all consoles
        
        Enter 0 to return to the previous menu.
        ------------------------------------------
        ''')

        choice = input("Please select an option:")
        if choice == "1":
            print('You have selected "Add a console".')
            param1 = input("Console Name: ")
            param2 = input("Console Description: ")
            user_console.add_genre(param1, param2)

        elif choice == "2":
            print('You have selected "Delete by id".')
            param = input("Console ID: ")
            user_console.delete_by_id(param)

        elif choice == "3":
            print('You have selected "Delete by name".')
            param = input("Console Name: ")
            user_console.delete_by_name(param)

        elif choice == "4":
            print('You have selected "Find by id".')
            param = input("Console ID: ")
            user_console.find_by_id(param)

        elif choice == "5":
            print('You have selected "Find by name".')
            param = input("Console Name: ")
            user_console.find_by_name(param)

        elif choice == "6":
            print('You have selected "Get all consoles".')
            user_console.get_all_genres()

        elif choice == "0": 
            return
        
        elif choice == "quit" or "help" or "im lost":
            exit_program()

        else:
            print("That is invalid. Please select one of the menu options.")
            

if __name__ == "__main__":
    main()

