import os
import random
os.system("clear")

class Board():
    def __init__(self):
        self.cells = [] # Make a list of 10? cells to hold data of what is in each cell
        for i in range(10):
            self.cells.append(" ") # Initialize cells with for in loop


    def display(self):
        print (" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        if self.cells[cell_no] == " ":
            self.cells[cell_no] = player

    def is_winner(self, player):
        # 8 ways to win
        # List of lists
        for combo in [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9,],[3,5,7]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False
            if result == True:
                return True
        return False

    def reset(self):
        self.cells = [" " for cell in self.cells] # wow this is fancy!

    def tied(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True # Then it's a tie game
        else:
            return False

    def ai_move(self, player):
        if player == "X":
            enemy = "O"
        if player == "O":
            enemy = "X"

        # If center is open, choose that
        if self.cells[5] == " ":
            self.update_cell(5, player)


            # AI can win

            # AI blocks player

            # Random choice
        else:
            flag = True
            rand = random.randrange(1, 10)
            while flag:
                if self.cells[rand] == " ":
                    self.update_cell(rand, player)
                    flag = False
                else:
                    rand = random.randrange(1, 10)

# Main Program
# Initialize
def print_welcome():
    print ("Welcome to Tic-Tac-Toe\n")

def refresh_screen():
    os.system("clear")
    print_welcome()
    board.display()
    print ("\n")


board = Board()    # Initialize board object


# Game Loop
while True:
    refresh_screen()

    # Get X input
    x_choice = int(raw_input("\nX) Please choose spot 1-9. >"))

    # Update board
    board.update_cell(x_choice, "X")

    # Refresh screen
    refresh_screen()

    # Check for X win
    if board.is_winner("X"):
        print ("\nX wins!\n")
        play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Check for a tie after X goes
    if board.tied():
        print ("\nTie game!\n")
        play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Get O input
    #o_choice = int(raw_input("\nO) Please choose spot 1-9. >"))
    board.ai_move("O")
    refresh_screen()

    # Update board
    #board.update_cell(o_choice, "O")

    # Refresh screen
    refresh_screen()

    # Check for O win
    if board.is_winner("O"):
        print ("\nO wins!\n")
        play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break

    # Check for a tie after O goes
    if board.tied():
        print ("\nTie game!\n")
        play_again = raw_input("Would you like to play again? (Y/N) > ").upper()
        if play_again == "Y":
            board.reset()
            continue
        else:
            break




    #gg
