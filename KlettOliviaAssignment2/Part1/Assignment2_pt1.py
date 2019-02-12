'''
Olivia Klett
oklett1@binghamton.edu
Lab Section A52, Elizabeth Vorshylo
Assignment 2, pt 1
'''

'''
ANALYSIS

RESTATEMENT: Write a program that computes the number of
diagonals in a regular polygon given the number of sides.

OUTPUT to moniter:
num_diagonals (int) - number of diagonals in the polygon

INPUT from keyboard:
num_sides (int) - number of sides the polygon has

GIVENS:
HALF - 2

PROCESSING: Get user input for the number of sides in the
polygon, convert the string input to an integer, and calculate
the number of diagonals using the formula num_diagonals =
(num_sides * (num_sides - 3)) // 2. Finally, print the
output to the screen.
'''

#Contants
HALF = 2

##Brief description of program:
#This program calculates the number of diagonals in a regular
#based on user input of the number of sides in the polygon.

def main():
  #Describe program to user
  print('This program computes the number of diagonals in a regular ' +
        'polygon given the number of sides.')

  #Ask user for number of sides
  num_sides_str = input("Enter the number of sides in the polygon: ")

  #print(num_sides_str)

  #Convert string input to an interger
  num_sides = int(num_sides_str)

  #Compute the number of diagonals
  num_diagonals = (num_sides * (num_sides - 3)) // HALF

  #print the number of diagonals
  print('A polygon with %d sides has %d diagonals' % (num_sides, num_diagonals))

main()
