import random

MAX_LINES = 3
MAX_BET = 255
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "Peach": 2,
    "Bowser": 4,
    "Yoshi": 6,
     "Mario": 8,
}#get 3 of them for every column, Peach is the rarest and most valuable

symbol_value_multiply = {
    "Peach": 9,
    "Bowser": 5,
    "Yoshi": 4,
     "Mario": 2,
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        first_symbol = columns[0][line]#1st symbol of the each column
        for i in range(1,len(columns)):
            symbol_to_check = columns[i][line]
            if first_symbol != symbol_to_check:#line failed
               break
        else:#doesn't run if there is a break triggered
             winnings += symbol_value_multiply[symbol_to_check]*bet
             winning_lines.append(line + 1)
            
    return winnings, winning_lines
      

def get_slot_machines_spin(rows, cols, symbols):
    all_symbols = []#a list of
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):# so the Peach appears twice and is added twice into the array same thing for the others
            all_symbols.append(symbol)#addition is here, and took em all, for example 2 Peach added
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
              value = random.choice(all_symbols)#choose any element from the array randomly
              current_symbols.remove(value)# you remove what was chosen from the array, cuz it's taken already
              column.append(value)# and add it to column
              
        columns.append(column)#then add the whole 3-elements array to form a matrix   
        
    return columns#returns all the randomly genrated arrays with 3 elements each as a matrix
        


def show_slot_machines_lines(columns):
    lm = len(columns[0])
    for row in range(lm):
        i = 0
        for elem in columns[row]:
             if i != 3:
                 print(elem, end="|")
                 i += 1
             else:
                 print(column[row], end="")
        print()          
     

def deposit():
    while True: # we want the user to deposit an actual amount if not, we keep repeating that
        amount = int(input("how much you gonna deposit? €:"))
        if amount > 0:
            print("money deposited =", amount,"€")
            break

        elif amount < 0:
            print("That's a negative number, give some real money you dumbass!")

        else:
            print("Invalid value, typing in 0 is like doing nothing, give dough, you gotta play!")

    return amount


def get_number_of_lines():
          while True: # we want a number of lines/chances to be chosen so you bet on.
              lines = input("Enter the numbers of lines to bet on (1-"+ str(MAX_LINES) +")?")
              lines = int(lines)
              if 1 <= lines <= MAX_LINES:#greater than or equal 1 and less than 3
                  print("number of chosen lines =", lines)
                  break
              
              elif lines < 0:
                  print("That's a negative number, negative lines don't exist, shithead")

              else:
                  print("Invalid value, typing in 0 is like making fun of me, you need line!")

          return lines




def get_bet():
     while True: # we want the user to deposit an actual amount if not, we keep repeating that
         amount = int(input("how much you gonna bet on each line thanks to how much you have? €:"))
         if MIN_BET <= amount <= MAX_BET:
             print("money bet =", amount,"€")
             break
         
         elif amount < 0:
             print("..What you even thinkin' about??")

         else:
             print(f'jeez, the amount to bet for each line has to be between ${MIN_BET} - ${MAX_BET}')

     return amount
    
    
def spin(balance):
     lines = get_number_of_lines()# returns the number of chosen lines
     while True:
         bet = get_bet()#return what you bet
         total_bet = bet*lines
         if total_bet > balance:
            print("you bet an amount way greater than what your balance actually is, try again!")
            print("amount in question multiplied by the number of lines:", total_bet,"€")
            print("thy balance:",balance,"€")   
         else:
             print(f'you bet ${bet} on ${lines} lines, so the total amount is: ${total_bet}')
             break
       
         
     slots = get_slot_machines_spin(ROWS, COLS, symbol_count)
     print(slots)#matrix
     show_slot_machines_lines(slots)
     winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value_multiply)
     print(winnings)
     print(winning_lines)
     if winnings == 0:
         print("You haven't won anything, loser!")
     else:
         print(f'you got ${winnings}.')
         print(f'you won on lines:', * winning_lines)
   
     return winnings - total_bet
    
    
def main():
    balance = deposit()
    while True:
        print(f'Current balance is ${balance}')
        answer = input("Press enter to play (q to quit playing)")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f'you left with ${balance}')
    
main()       

























