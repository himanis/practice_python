import re
import string
import random
import pdb
from itertools import cycle

class tic_tac():
    global current
    global bd # This is a board
    win_comb = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,6),(3,6,9),(1,5,9),(3,5,7))

    def __init__(self):
        print '{:^40}'.format("WELCOME TO TIC-TAC-TOE")
        self.current =''
        self.bd = ['']*10
        return

    def clear_board(self):
        for i in range(1,10):
            self.bd[i]=i
        return

    def display_bd(self):
        vline = "|"
        print '{:>6}{:2}{:2}{:2}{:2}'.format(self.bd[1], vline,self.bd[2], vline,self.bd[3])
        print  '{:2}{:-<12}'.format('','')
        print '{:>6}{:2}{:2}{:2}{:2}'.format(self.bd[4], vline,self.bd[5], vline,self.bd[6])
        print '{:2}{:-<12}'.format('','')
        print '{:>6}{:2}{:2}{:2}{:2}'.format(self.bd[7], vline,self.bd[8], vline,self.bd[9])
        return

    def chooes_player(self):
        who = random.randint(1,2)
        who = "Player-"+str(who)
        print  '{:<10}{:<20}'.format(who, " Won, you will go first ")
        return who

    def chose_symbol(self):
        sym = ''
        print "{:>6}{:<12}".format(self.current,", Please choose your symbol(X/O)")
        while sym not in 'X O'.split():
            sym = raw_input().upper()
            if sym not in 'X O'.split():
                print "Try Again, only X and O"
        return  sym


    def is_empty(self,pos):
        if self.bd[pos]== int(pos):
            return True
        else:
            return False

    def is_space_left(self):
        for i in range(1,10):
            if (self.is_empty(i)):
                return True
        return False


    def check_win(self,mark):
        return ((self.bd[1]==self.bd[2]==self.bd[3]==mark) or
            (self.bd[4] ==self.bd[5] ==self.bd[6] ==mark) or
            (self.bd[7]==self.bd[8]==self.bd[9] ==mark) or
            (self.bd[1] ==self.bd[4] ==self.bd[7] ==mark) or
            (self.bd[2] ==self.bd[5] ==self.bd[8] ==mark) or
            (self.bd[3] ==self.bd[6] ==self.bd[9]==mark) or
            (self.bd[1] ==self.bd[5] ==self.bd[9]==mark) or
            (self.bd[3] ==self.bd[5] ==self.bd[7]==mark)
            )

    '''def check_win(self,mark):
        #pdb.set_trace()
        for elem in self.win_comb:
            if elem[0]]== elem[1]== elem[2]==mark:
                return True
        else:
            return False'''

    def player_input(self):
        pos = ''
        try:
            while pos not in '1 2 3 4 5 6 7 8 9'.split() or not self.is_empty(int(pos)):
                pos = raw_input( self.current+", Enter your position from 1 to 9 ")
                if (pos == '' or not self.is_empty(int(pos))):
                    print " Please print correct value or chose the empty space"
        except ValueError:
            print "Oops! Enter again"
        return int(pos)

    def switch_player(self,marker):
        # type: () -> object
        self.current = 'Player-2' if self.current == 'Player-1' else 'Player-1'
        marker = 'X' if marker == 'O' else 'O'
        return marker

    def play_again(self):
        ans =''
        while ans not in 'yes no'.split():
            ans= raw_input("play again(yes/no)").lower()
        ans = True if ans =='yes' else False
        return ans

    def main_play(self):
        while True:
            self.clear_board()
            marker = ''
            self.display_bd()
            game_on = True
            self.current = self.chooes_player()
            marker = self.chose_symbol()
            #pdb.set_trace()
            while game_on:
                pos=self.player_input()
                self.bd[pos]= marker
                self.display_bd()
                if self.check_win(marker):
                    print '\Congratulation ', self.current ,"you win"
                    self.display_bd()
                    game_on = False
                else:
                    if not self.is_space_left():
                        self.display_bd()
                        print " This is a tie"
                        game_on = False
                    else:
                        marker = self.switch_player(marker)
            if not self.play_again():
                break
        return

    def __del__(self):
        print "cleaing the board"