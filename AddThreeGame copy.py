# Author: Peter Puczkowskyj
# Date: 7/25/2021
# Description: A game in which two players take turns picking numbers from one list of numbers and try to reach 15.

class AddThreeGame:
    ''' A representation of a game where players take turns trying to select three numbers that add up to 15. '''

    def __init__(self):

        ''' A function that keeps track of the game play. '''

        self._number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._current_state = "UNFINISHED"
        self._players_turn = "first"
        self._first_score = 0
        self._second_score = 0

    def get_current_state(self):  # maybe make setter function for current state

        ''' A function that gets the current state of game play '''

        return self._current_state

    def set_current_state(self):

        '''A function that checks scores and turns left in game, then changes the current state of the game'''

        if self._first_score == 15:
            self._current_state = "FIRST_WON"
        elif self._second_score == 15:
            self._current_state = "SECOND_WON"
        elif len(self._number_list) == 0:
            self._current_state = "DRAW"
        else:
            self._current_state = "UNFINISHED"

    def reset_game(self):

        ''' A function that resets the game '''

        self._number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._current_state = "UNFINISHED"
        self._players_turn = "first"
        self._first_score = 0
        self._second_score = 0

    def make_move(self, player, number_choice):

        ''' A function that represents game play '''

        if self._current_state == "UNFINISHED":
            if player == self._players_turn and number_choice in self._number_list:
                if player == "first":
                    self._first_score += number_choice
                    self._number_list.remove(number_choice)
                    self._players_turn = "second"
                    self.set_current_state()
                    return True

                else:
                    self._second_score += number_choice
                    self._number_list.remove(number_choice)
                    self._players_turn = "first"
                    self.set_current_state()
                    return True
            else:
                return False
        else:
            self.reset_game()
            return True
