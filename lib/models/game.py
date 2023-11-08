from models.__init__ import CURSOR, CONN

class Game:

    def __init__(self):
        self.create_table()
        
    # create genre table
    def create_table(self):
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS games (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                console_id INT,
                genre_id INT
            )
        ''')
        CONN.commit()
        

    def __repr__(self):
        return f"{self.name}"
    
    # Adds a game to games table
    def add_game(self, name, console_id, genre_id):
        name_new = name.lower()
        CURSOR.execute("SELECT id FROM games WHERE name = ?", (name_new,))
        existing_id = CURSOR.fetchone()

        if existing_id:
            print(f'A game with the name "{name}" already exists.')
        else:
            CURSOR.execute("INSERT INTO games (name, console_id, genre_id) VALUES (?, ?, ?)", (name, console_id, genre_id))
            CONN.commit()

    # Delete game from games by game_id
    def delete_by_id(self, game_id):
        CURSOR.execute("SELECT name FROM games WHERE id = ?", (game_id))
        existing_game = CURSOR.fetchone()

        if existing_game:
            print(f"Deleting {existing_game} (id: {game_id})...")
            CURSOR.execute("DELETE FROM games WHERE id = ?", (game_id)) 
            CONN.commit()
        else:
            print(f'A game with the name "{existing_game}" does not exist.')
    
    # delete game from games by name
    def delete_by_name(self, name):
        name_search = name.lower()
        CURSOR.execute("SELECT id FROM games WHERE name = ?", (name_search))
        existing_id = CURSOR.fetchone()

        if existing_id:
            print(f"Deleting {name} (id: {existing_id})...")
            CURSOR.execute("DELETE FROM gamess WHERE id = ?", (existing_id)) 
            CONN.commit()
        else:
            print(f'A game with the name "{name}" does not exist.')
    
    # find games by id
    def find_by_id(self, game_id):
        CURSOR.execute("SELECT * FROM games WHERE id = ?", (game_id))
        existing_game = CURSOR.fetchone()

        if existing_game:
            return CURSOR.fetchone()
        else: 
            print(f'A game with the id "{game_id}" does not exist.')

    # find games by name
    def find_by_name(self, name):
        name_search = name.lower()
        CURSOR.execute("SELECT * FROM games WHERE name = ?", (name_search))
        existing_game = CURSOR.fetchone()

        if existing_game:
            return CURSOR.fetchone()
        else: 
            print(f'A game with the name "{name}" does not exist.')

    # get all games
    def get_all_games(self):
        CURSOR.execute("SELECT * FROM gamess")
        return CURSOR.fetchall()