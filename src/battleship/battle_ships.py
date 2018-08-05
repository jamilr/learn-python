# Battleship is an implementation of a famous guessing game for two players
# You can find more about the game here: https://en.wikipedia.org/wiki/Battleship_(game)


__author__ = 'J.R.'


class Point:
    idx = -1
    letter = ''

    def __init__(self, idx, letter):
        self.idx = idx
        self.letter = letter

    def __str__(self):
        return "Point - " + str(self.idx) + str(self.letter)


class Ship:
    start = None
    end = None
    size = 0
    never_hit = True
    hits = 0

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.calc_size()

    def calc_size(self):
        v_delta = abs(self.end.idx - self.start.idx) + 1
        h_delta = abs(ord(self.end.letter[0]) - ord(self.start.letter[0])) + 1
        self.size = v_delta * h_delta

    def inc_hit(self):
        self.hits += 1

    def sunk(self):
        return self.hits == self.size

    def hits_the_ship(self, hit):
        if hit is None:
            return False
        hits_ship = True
        hits_ship &= self.end.letter >= hit.letter >= self.start.letter
        hits_ship &= self.end.idx >= hit.idx >= self.start.idx
        return hits_ship


class GameResult:
    hit = 0
    sunk = 0

    def __init__(self, hit, sunk):
        self.hit = hit
        self.sunk = sunk

    def inc_hit(self):
        self.hit += 1

    def dec_hit(self):
        self.hit -= 1

    def inc_sunk(self):
        self.sunk += 1

    def __str__(self):
        return 'Game Results: Hit Ships - ' + str(self.hit) + ', Sunk Ships - ' + str(self.sunk)

    @classmethod
    def no_game_result(cls):
        return GameResult(-1, -1)


class InputParser:

    @classmethod
    def parse_ships(cls, all_ships_input):
        ships_str = all_ships_input.split(',')
        ships_count = len(ships_str)
        all_ships = list()
        for i in range(ships_count):
            all_ships.append(InputParser.parse_ship(ships_str[i]))
        return all_ships

    @classmethod
    def parse_ship(cls, ship_input):
        points = ship_input.split(' ')
        start = InputParser.parse_point(points[0])
        end = InputParser.parse_point(points[1])
        return Ship(start, end)

    @classmethod
    def parse_points(cls, points_input):
        points_str = points_input.split(' ')
        points = list()
        for point_str in points_str:
            points.append(InputParser.parse_point(point_str))
        return points

    @classmethod
    def parse_point(cls, point_input):
        n = len(point_input)
        point_letter = point_input[-1:][0]
        point_idx = int(point_input[:n - 1])
        return Point(point_idx, point_letter)


class Game:
    ships_input = ''
    hits_input = ''

    def __init__(self, ships, hits):
        self.ships_input = ships
        self.hits_input = hits

    def run_the_game(self):
        if self.ships_input is None or len(self.ships_input) == 0 or self.hits_input is None or len(self.hits_input) == 0:
            return GameResult.no_game_result()

        hits = InputParser.parse_points(self.hits_input)
        if len(hits) == 0:
            return GameResult.no_game_result()

        all_ships = InputParser.parse_ships(self.ships_input)
        if len(all_ships) == 0:
            return GameResult.no_game_result()

        game_result = GameResult(0, 0)
        for hit in hits:
            if all_ships is None or len(all_ships) == 0:
                break
            for ship in all_ships:
                if ship.hits_the_ship(hit):
                    if ship.never_hit:
                        ship.never_hit = False
                        game_result.inc_hit()
                    ship.inc_hit()
                    if ship.sunk():
                        game_result.dec_hit()
                        game_result.inc_sunk()
                        all_ships.remove(ship)

        return game_result


if __name__ == '__main__':
    ships_input = '1B 2C,2D 4D'
    hits_input = '2B 2D 3D 4D'
    game = Game(ships_input, hits_input)
    print(game.run_the_game())
