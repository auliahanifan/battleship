import config
from model.game import Game
from factory.player_factory import PlayerFactory

class Application:

    def read_file(self):
        f = open('input.txt', 'r')
        lines = f.readlines()
        # delete new line
        lines = [line[:-1] for line in lines if line[-1] == '\n' ]

        if len(lines) != 7:
            raise Exception('File input is not standard')
        
        self.length_battleground = int(lines[0])

        if self.length_battleground > config.MAX_LENGTH_BATTLEGROUND:
            raise Exception(f'Length of battleground is greater than {config.MAX_LENGTH_BATTLEGROUND}')

        self.ship_number = int(lines[1])

        if self.ship_number > config.MAX_BATTLESHIP:
            raise Exception(f'Number of ships is greater than {config.MAX_BATTLESHIP}')

        self.player_1_ship_positions_and_value = self.parse_positions(lines[2])
        if len(self.player_1_ship_positions_and_value) != self.ship_number:
            raise Exception('Amount of ship player 1 and length of positions are not same')

        self.player_2_ship_positions_and_value = self.parse_positions(lines[3])
        if len(self.player_2_ship_positions_and_value) != self.ship_number:
            raise Exception('Amount of ship player 2 and length of positions are not same')
        
        self.missile_number = int(lines[4])

        self.player_1_missile_positions_and_value = self.parse_positions(lines[5])
        if len(self.player_1_missile_positions_and_value) != self.ship_number:
            raise Exception('Amount of missile player 1 and length of positions are not same')

        self.player_2_missile_positions_and_value = self.parse_positions(lines[6])
        if len(self.player_2_missile_positions_and_value) != self.ship_number:
            raise Exception('Amount of missile player 2 and length of positions are not same')

        f.close()

    def parse_positions(self, positions_string: str) -> list:
        temp_positions = positions_string.split(':')
        positions = list()
        for temp in temp_positions:
            vals = temp.split(',')
            position = list()

            for val in vals:
                position.append(int(val))

            positions.append(position)

        return positions
    
    def start_game(self):
        self.read_file()
        player_1 = PlayerFactory.create_new_player(self.length_battleground, self.player_1_ship_positions_and_value, self.player_1_missile_positions_and_value)
        player_2 = PlayerFactory.create_new_player(self.length_battleground, self.player_2_ship_positions_and_value, self.player_2_missile_positions_and_value)
        game = Game(player_1, player_2)
        game.start_battle()
        result = game.get_result()
        self.write_file(result)

    def write_file(self, string):
        f = open("output.txt", "w")
        f.write(string)
        f.close()