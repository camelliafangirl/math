# enum for number, operator, function, variable, constant

# token class:
# number: value(val)
# operator: precedence, arguments, associativity
# function: name, variable, arguments, representation as tokens (+reverse polish notation for evaluation)
# constant: name, value
# string to token method
# shunting yard method

# data structures for storing user variables/functions
# io loop
# plotting of function within ranges

from mathtoken import Assoc, Type, Token

def main():
    while True:
        line = input()
        if line.lower() == 'exit':
            exit()
        

if __name__ == '__main__':
    main()