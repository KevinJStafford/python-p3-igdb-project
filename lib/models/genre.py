# pip install colorama

from colorama import Fore, Style
from models.__init__ import CONN, CURSOR

class Genre: 
    def __init__(self):
        self.create_table()

    # create genre table
    def create_table(self):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS genres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT
            )
        ''')
        CONN.commit()
    
    # add genre
    def add_genre(self, name, description):
        name_new = name.lower()
        CURSOR.execute("SELECT id FROM genres WHERE name = ?", (name_new,))
        existing_id = CURSOR.fetchone()

        if existing_id:
            print(f'{Fore.RED}ERROR: A genre with the name "{name}" already exists.{Style.RESET_ALL}')
        else:
            CURSOR.execute("INSERT INTO genres (name, description) VALUES (?, ?)", (name, description))
            CONN.commit()
            print(f"{Fore.GREEN}New genre added.\nName: {name}\nDescription: {description}{Style.RESET_ALL}")

    # delete by id
    def delete_by_id(self, genre_id):
        CURSOR.execute("SELECT name FROM genres WHERE id = ?", (genre_id,))
        existing_name = CURSOR.fetchone()
        
        if existing_name:
            name_letters_only = existing_name[0]
            
            print(f"{Fore.GREEN}Deleting... \nID: {genre_id}\nName: {name_letters_only}{Style.RESET_ALL}")
            CURSOR.execute("DELETE FROM genres WHERE id = ?", (genre_id,)) 
            CONN.commit()
            print(f"{Fore.GREEN}Genre delete completed.{Style.RESET_ALL}")
        else:
            print(f'{Fore.RED}ERROR: A genre with the name "{existing_name}" does not exist.{Style.RESET_ALL}')
    
    # delete by name
    def delete_by_name(self, name):
        name_search = name.lower()
        CURSOR.execute("SELECT id FROM genres WHERE name = ?", (name_search,))
        existing_id = CURSOR.fetchone()

        if existing_id:
            id_numbers_only = existing_id[0]

            print(f"{Fore.GREEN}Deleting... \nID: {id_numbers_only}\nName: {name}{Style.RESET_ALL}")
            CURSOR.execute("DELETE FROM genres WHERE id = ?", (existing_id)) 
            CONN.commit()
            print(f"{Fore.GREEN}Genre delete completed.{Style.RESET_ALL}")
        else:
            print(f'{Fore.RED}ERROR: A genre with the name "{name}" does not exist.{Style.RESET_ALL}')
    
    # find genre by id
    def find_by_id(self, genre_id):
        CURSOR.execute("SELECT * FROM genres WHERE id = ?", (genre_id,))
        existing_genre = CURSOR.fetchone()

        if existing_genre:
            (id, name, description) = existing_genre
            print(f"{Fore.GREEN}Name: {name}\nDescription: {description}{Style.RESET_ALL}")
        else: 
            print(f'{Fore.RED}ERROR: A genre with the id "{genre_id}" does not exist.{Style.RESET_ALL}')

    # find genre by name
    def find_by_name(self, name):
        name_search = name.lower()
        CURSOR.execute("SELECT * FROM genres WHERE name = ?", (name_search,))
        existing_genre = CURSOR.fetchone()

        if existing_genre:
            (id, name, description) = existing_genre
            print(f"{Fore.GREEN}ID: {id}\nName: {name}\nDescription: {description}{Style.RESET_ALL}")
        else: 
            print(f'{Fore.RED}ERROR: A genre with the name "{name}" does not exist.{Style.RESET_ALL}')

    # get all genres
    def get_all_genres(self):
        CURSOR.execute("SELECT * FROM genres")
        all_genres = CURSOR.fetchall()

        if all_genres:
            for genre in all_genres:
                id, name, description = genre
                print(f"{Fore.GREEN}ID: {id} \nName: {name}\nDescription: {description}\n{Style.RESET_ALL}")
        else: 
            print(f"{Fore.GREEN}There are no genres currently. Use the menu to add a genre.{Style.RESET_ALL}")
