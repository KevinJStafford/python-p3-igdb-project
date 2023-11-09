import ipdb 
from colorama import Fore, Style
from models.__init__ import CONN, CURSOR

class Console:

    def __init__ (self):
        self.create_table()

    def create_table(self):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS console (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                year TEXT
            )
        ''')
        CONN.commit()

    @classmethod
    def from_db(cls, row):
        return cls(id=row[0], name=row[1], year=row[2])

    # add console
    def add_console(self, name, year):
        name_new = name.lower()
        CURSOR.execute("SELECT id FROM console WHERE name = ?", (name_new,))
        existing_id = CURSOR.fetchone()

        if existing_id:
            print(f'{Fore.RED}ERROR: A console with the name "{name}" already exists.{Style.RESET_ALL}')
        else:
            CURSOR.execute("INSERT INTO console (name, year) VALUES (?, ?)", (name, year))
            CONN.commit()
            print(f"{Fore.GREEN}New  console added. \nName: {name}\nYear: {year}{Style.RESET_ALL}")

    #delete by id 
    def delete_by_id(self, console_id):
        CURSOR.execute("SELECT name FROM console WHERE id = ?", (console_id,))
        existing_name = CURSOR.fetchone()

        if existing_name:
            name_letters_only = existing_name[0]

            print(f"{Fore.GREEN}Deleting... \nID: {console_id}\nName: {name_letters_only}{Style.RESET_ALL}")
            CURSOR.execute("DELETE FROM console WHERE id = ?", (console_id))
            CONN.commit()
            print(f"{Fore.GREEN}Console delete completed.{Style.RESET_ALL}")
        else:
            print(f'{Fore.RED}ERROR: A console with the name "{existing_name}" does not exist.{Style.RESET_ALL}')


    # delete by name
    def delete_by_name(self, name):
        name_search = name.lower()
        CURSOR.execute("SELECT id FROM console WHERE name = ?", (name_search,))
        existing_id = CURSOR.fetchone()

        if existing_id:
            id_numbers_only = existing_id[0]

            print(f"{Fore.GREEN}Deleting... \nID: {id_numbers_only}\nName: {name}{Style.RESET_ALL}")
            CURSOR.execute("DELETE FROM console WHERE id = ?", (existing_id)) 
            CONN.commit()
            print(f"{Fore.GREEN}Console delete completed.{Style.RESET_ALL}")
        else:
            print(f'{Fore.RED}ERROR: A console with the name "{name}" does not exist.{Style.RESET_ALL}')

    # find console by id
    def find_by_id(self, console_id):
        CURSOR.execute("SELECT * FROM console WHERE id = ?", (console_id,))
        existing_console = CURSOR.fetchone()

        if existing_console:
            (id, name, year) = existing_console
            print(f"{Fore.GREEN}Name: {name}\nYear: {year}{Style.RESET_ALL}")
        else: 
            print(f'{Fore.RED}ERROR: A console with the id "{console_id}" does not exist.{Style.RESET_ALL}')

    # find console by name
    def find_by_name(self, console_name):
        name_search = console_name.lower()
        CURSOR.execute("SELECT * FROM console WHERE name = ?", (name_search,))
        existing_console = CURSOR.fetchone()

        if existing_console:
            (id, name, year) = existing_console
            print(f"{Fore.GREEN}ID: {id}\nName: {name}\nYear: {year}{Style.RESET_ALL}")
        else:
            print(f'{Fore.RED}ERROR: A console with the name "{console_name}" does not exist.{Style.RESET_ALL}')

    # get all console
    def get_all_consoles(self):
        CURSOR.execute("SELECT * FROM console")
        all_consoles = CURSOR.fetchall()

        if all_consoles:
            for console in all_consoles:
                id,name,year = console
                print(f"{Fore.GREEN}ID: {id} \nName: {name}\nYear: {year}\n{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}There are no consoles currently. Use the menu to add a console.{Style.RESET_ALL}")
    
    # get all genres
    @classmethod
    def genres(cls, id):
        sql = '''SELECT genres.* FROM genres
              JOIN games ON games.genre_id = genres.id
              WHERE games.console_id = ?'''
        params = (id, )
        genres_list = CURSOR.execute(sql, params).fetchall()
        
        if genres_list:
            print(f"{Fore.GREEN}Retrieving all genres for the selected platform.{Style.RESET_ALL}")
            for genre in genres_list: 
                print(f"{Fore.GREEN}{genre[1]}{Style.RESET_ALL}")
        else:
            print(f"{Fore.GREEN}There are no genres for the selected platform.{Style.RESET_ALL}")
    
    @classmethod
    def drop_table(cls):
        CURSOR.execute('DROP TABLE consoles')