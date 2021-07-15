import pickle
import os
from board import Board
from settings import SPEEDS
from cmds import HELP


class Keno:
    def __init__(self, player, credits=500):
        self.start_credits = credits
        self.player = player
        self.init_data()
    
        self.run = True
        self.start()

    def start(self):
        while self.run == True:
            self.run_loop()
        

    def init_data(self, data=None):
        self.cmds = {
            'BET': self._bet,
            'WIPE': self._wipe_board,
            'QUICK': self._quick_pick,
            'PICK': self._pick,
            'START': self._start,
            'SPEED': self._speed,
            'SAVE': self._save,
            'LOAD': self._load,
            'QUIT': self._quit,
            'HELP': self._help,
        }
        if data is None:
            self.data = {
                'BET': 1,
                'CREDITS': self.start_credits,
                'PLAYER': self.player,
                'WON': 0,
                'SPEED': 'DEFAULT',
            }
        else:
            self.data = data
        self.board = Board(self.data, self)

    def run_loop(self):
        self.board.render()
        cmd = str(input("Enter a command to play Keno [HELP] >>> "))
        
        cmdcall, arg = self.handle(cmd)
        if cmdcall is None:
            pass

        cmdcall(arg=arg)

        self.board.render()

    def handle(self, cmd):
        cmd = cmd.split(' ')
        
        command = cmd[0].upper()
        try:
            arg = cmd[1]
        except:
            arg = ""
        
        return self.cmds.get(command), arg

    def _bet(self, arg):
        self.board.bet()

    def _wipe_board(self, arg):
        self.board.wipe()

    def _quick_pick(self, arg):
        if arg == "":
            arg = 10
        else:
            arg = int(arg)
        self.board.quick(arg)
        
    def _pick(self, arg):
        
        try:
            pick = int(arg)
        except:
            print("Invalid pick!")
        self.board.toggle(pick)
        
    def _start(self, arg):
        self.board.play()

    def _speed(self, arg):
        os.system('clear')
        header = "Speed Config"
        subheader = f"{'='*len(header)}"
        print(header)
        print(subheader)
        for speed in SPEEDS.keys():
            if speed == self.data['SPEED']:
                print(f"[{speed}]")
            else:
                print(speed)
        selection = str(input("Enter a value >>> "))
        selection = selection.upper()
        if selection not in SPEEDS.keys():
            print("Invalid input")
            input("Continue >>> ")
            self._speed()
        else:
            self.data['SPEED'] = selection
            self.board.update_data('SPEED', selection)

    def _save(self, arg):
        filename = arg.strip() + '.pkl'

        with open(filename, 'wb') as handle:
            pickle.dump(self.data, handle, protocol=pickle.HIGHEST_PROTOCOL)

        os.system('clear')
        print("Data saved to: '{}'".format(filename))
        input("Continue >>> ")

    def _load(self, arg):
        filename = arg.strip() + '.pkl'

        try:
            with open(filename, 'rb') as handle:
                data = pickle.load(handle)

            self.init_data(data=data)
        except FileNotFoundError:
            os.system('clear')
            print("Save File not found..")
            input("Continue >>> ")

    def _quit(self, arg):
        os.system('clear')
        print("Thanks for playing!")
        input("Continue >>> ")
        self.run = False

    def _help(self, arg):
        os.system('clear')
        header = 'COMMANDS'
        subheader=  f'{"="*len(header)}'
        print(header)
        print(subheader)
        for cmd in self.cmds.keys():
            print(cmd)
            print(f'{"-"*len(cmd)}')
        if arg.upper() in self.cmds.keys():
            print(HELP[arg.upper()])
        else:
            print("Type HELP [CMD] to see help for specific topic.")
            
        input("Continue >>> ")



if __name__ == '__main__':
    game = Keno("Player")
