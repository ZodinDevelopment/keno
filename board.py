import time
import os
import random
from settings import SPEEDS
from prizetable import PrizeTable
import sounds


class Board:
    def __init__(self, game_data, parent):
        self.parent = parent
        self.balls = [i for i in range(1, 81)]
        self.picks = []
        self.draws = []
        self.hits = []
        self.game_data = game_data
        self.init_table()

    def init_table(self):
        self._prize_table = PrizeTable(self.picks, self.game_data.get("BET"))

    def toggle(self, value):
        if value > 0 and value <= 80:
            if value not in self.picks and len(self.picks) < 10:
                self.picks.append(value)
            elif value in self.picks:
                self.picks.remove(value)

            self.init_table()
        else:
            pass

    def update_data(self, key, value):
        self.game_data[key] = value
        self.parent.data = self.game_data
        

    def play(self):
        self.draws = []
        self.hits = []
        self.render()
        if self.game_data['BET'] < 1 or self.game_data["BET"] > 10:
            print('Bet must be 1-10')
        if self.game_data['BET'] > self.game_data['CREDITS']:
            print('Insufficient credits')

        delay = SPEEDS.get(self.game_data['SPEED'])
        self.game_data['CREDITS'] -= self.game_data['BET']
        while len(self.draws) < 20:
            draw = random.choice(self.balls)
            self.draws.append(draw)
            self.balls.remove(draw)
            if draw in self.picks:
                self.hits.append(draw)
                sounds.hit_sound()
            else:
                sounds.draw_sound()

            self.render(draw)
            time.sleep(delay)

        won = self._prize_table.win(len(self.hits))
        if won > 0:
            sounds.win_sound()
        self.game_data['WON'] = won
        self.game_data['CREDITS'] += won
        self.update_data('WON', won)
        self.update_data('CREDITS', self.game_data['CREDITS'])
        self.render()
        print(f"HIT {len(self.hits)}\nWON {won}")

        self.balls = [i for i in range(1, 81)]

    def quick(self, num):
        self.wipe()
        self.render()
        
        self.picks = []
        while len(self.picks) < num:
            pick = random.choice(self.balls)
            self.picks.append(pick)
            self.balls.remove(pick)
        self.balls = [i for i in range(1, 81)]
        self.init_table()
        self.render()

    def bet(self):
        if self.game_data['BET'] < 10:
            self.update_data('BET', self.game_data['BET'] + 1)
        else:
            self.update_data('BET', 1)

        self.init_table()
        self.render()

    def wipe(self):
        self.draws = []
        self.picks = []
        self.hits = []
        self.init_table()
        self.render()

    def render(self, draw=None):
        numrow = 8
        numcol = 10
        board = []
        for row in range(1,numrow+1):
            nums = []
            for col in range(1, numcol+1):
                if col < numcol:
                    num = int(str((row -1 )) + str(col))
                else:
                    num = int(str(row) + "0")
                if num < 10:
                    numstr = " " + str(num)
                else:
                    numstr = str(num)
                if num in self.hits:
                    tile = "[$$]"
                elif num in self.picks:
                    tile = f"[{numstr}]"
                elif num in self.draws:
                    tile = " ## "

                else:
                    tile = f" {numstr} "
                nums.append(tile)
            rowstr = "|".join(nums)
            board.append(rowstr)
        board = "\n".join(board)

        hud = []
        for info in self.game_data.keys():
            value = self.game_data[info]
            hud.append(f"{info}: {value}")
        hud = "//".join(hud)
        if draw is None:
            draw = "?"
        display = [
            draw, 
            board,
            hud,
            str(self._prize_table),
            f"HIT: {len(self.hits)} // WON: {self.game_data['WON']}",
            f"DRAWS: {len(self.draws)}"
        ]
        os.system('clear')
        for obj in display:
            print(obj)
