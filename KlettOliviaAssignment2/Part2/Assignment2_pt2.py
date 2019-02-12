'''
Olivia Klett
oklett1@binghamton.edu
Lab Section A52, Elizabeth Vorshylo
Assignment 2, pt 2
'''

'''
ANALYSIS

RESTATEMENT: Write a program that draws a regular polygon,
with side lengths, the number of sides, color, and fill color
determined by user input.

OUTPUT to moniter:
draws a regular polygon filled with the desired color on a
turtle screen

INPUT from keyboard:
num_sides (int) - number of sides for the polygon
side_length (int) - length of each side
turtle_color (str) - color of the turtle
fill_color (str) - color to fill the polygon

GIVENS:
DEGREES - 360

PROCESSING: Import turtle module. Take user input of number of
sides, side lengths, color, and fill color and convert the number
of sides and side lengths to integers. Set up turtle screen and
turtle, and set the turtle color to the color specified by the user.
Then, begin the fill color, and use a for loop to draw each side of
the polygon with each iteration. The loop should iterate the number
of sides that are in the polygon, and the turtle should go forward
side_length units, then turn (360 / num_sides) degrees to the left
each time. End the fill color after the loop.
'''

#Constants
DEGREES = 360

##Breif description of program:
#This program draws a regular polygon based on user input of
#number of sides, side length, and fill color.

#Imports
import turtle

def main():
  #Description of program to user
  print('This program draws a regular polygon given the number ' +
        'of sides, side length, and fill color.')

  #Ask user for number of sides
  num_sides_str = input("Enter the number of sides: ")

  #Convert string input to integer
  num_sides = int(num_sides_str)

  #Ask user for side length
  side_length_str = input("Enter the side length: ")

  #Convert string input to integer
  side_length = int(side_length_str)

  #Ask for the turtle color
  turtle_color = input("Enter the border color: ")

  #Ask for fill color
  fill_color = input("Enter the fill color: ")

  #Create the turtle screen
  wn = turtle.Screen()

  #Create the turtle
  andrew = turtle.Turtle()

  #Set the turtle color
  andrew.color(turtle_color)

  #Set the fill color
  andrew.fillcolor(fill_color)

  #Begin the fill color
  andrew.begin_fill()

  #Create a for loop to draw each side of the polygon with each
  #iteration
  for i in range(num_sides):
    andrew.forward(side_length)
    andrew.left(DEGREES / num_sides)

  #End the fill color
  andrew.end_fill()

  #Exit turtle screen when clicked
  wn.exitonclick()

main()
  
  
