import re
import string
import random
from itertools import cycle

class tic_tac():
    global current
    symbol ={'Player-1':'X','Player-2':'O'}

    def __init__(self):
        self.current =''
        return

    def clear_board(self,bd):
        for i in(1,9):
            bd[i]=''
        return bd

    def display_bd(self,bd):
        vline = "|"
        print '{:>6}{:2}{:2}{:2}{:2}'.format( bd[1], vline, bd[2], vline, bd[3])
        print  '{:2}{:-<12}'.format('','')
        print '{:>6}{:2}{:2}{:2}{:2}'.format( bd[4], vline, bd[5], vline, bd[6])
        print '{:2}{:-<12}'.format('','')
        print '{:>6}{:2}{:2}{:2}{:2}'.format( bd[7], vline, bd[8], vline, bd[9])
        return

    def chooes_player(self):
         who= random.randint(1,2)
         who = "Player-"+str(who)
         print  '{:>10}{:<20}'.format(who," Won, your symbol is 'x'")
         return who

    def is_empty(self,bd,pos):
        if bd[pos]=='':
            return True
        else:
            return False

    def is_space_left(self,bd):
        for i in range(1,10):
            if (self.is_empty(bd,i)):
                return True
        return False


    def check_win(self,bd,mark):
        return ((bd[1]== bd[2]== bd[3]==mark) or
            (bd[4] == bd[5] == bd[6] ==mark) or
            (bd[7]== bd[8]== bd[9] ==mark) or
            (bd[1] == bd[4] == bd[7] ==mark) or
            (bd[2] == bd[5] == bd[8] ==mark) or
            (bd[3] == bd[6] == bd[9]==mark) or
            (bd[1] == bd[5] == bd[9]==mark) or
            (bd[3] == bd[5] == bd[7]==mark)
            )


    def player_input(self,bd):
        pos =''
        while pos not in '1 2 3 4 5 6 7 8 9'.split() or not self.is_empty(bd,int(pos)):
            print "\t",self.current
            pos = raw_input("Enter your position from 1 to 9 ")
        return int(pos)

    def switch_player(self):
        self.current = 'Player-2' if self.current == 'Player-1' else 'Player-1'
        return

    def play_again(self):
        ans =''
        while ans not in 'yes no'.split():
            ans= raw_input("play again(yes/no)").lower()
        ans = True if ans =='yes' else False
        return ans

    def main_play(self):
        while True:
            bd = ['']*10
            self.clear_board(bd)
            marker = ''
            self.display_bd(bd)
            game_on = True
            self.current = self.chooes_player()
            while game_on:
                pos=self.player_input(bd)
                marker = self.symbol[self.current]
                bd[pos]= marker
                self.display_bd(bd)
                if self.check_win(bd,marker):
                    print '\Congratulation ', self.current ,"you win"
                    self.display_bd(bd)
                    game_on = False
                else:
                    if not self.is_space_left(bd):
                        self.display_bd(bd)
                        print " This is a tie"
                        game_on = False
                    else:
                        self.switch_player()
            if not self.play_again():
                break
        return

