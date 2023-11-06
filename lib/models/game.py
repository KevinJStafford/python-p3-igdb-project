from models.__init__ import CURSOR, CONN

class Game:

    def __init__(self, name, game_id=None):
        self.name = name
        self.game_id = game_id
        

    def __repr__(self):
        return f"{self.name}"
    
    # Adds a game to games table
    def add_genre(self, name, description):
        name_new = name.lower()
        CURSOR.execute("SELECT id FROM genres WHERE name = ?", (name_new))
        existing_id = CURSOR.fetchone()

        if existing_id:
            print(f'A game with the name "{name}" already exists.')
        else:
            CURSOR.execute("INSERT INTO games (name) VALUES (?)", (name))
            CONN.commit()

    # Delete game from games by game_id
    def delete_by_id(self, game_id):
        CURSOR.execute("SELECT name FROM games WHERE id = ?", (game_id))
        existing_name = CURSOR.fetchone()

        if existing_name:
            print(f"Deleting {existing_name} (id: {genre_id})...")
            CURSOR.execute("DELETE FROM games WHERE id = ?", (genre_id)) 
            CONN.commit()
        else:
            print(f'A game with the name "{existing_name}" does not exist.')
    
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