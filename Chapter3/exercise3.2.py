#!/usr/bin/env python
import sys
import locale
locale.setlocale( locale.LC_ALL, '' )

# Python for Informatics Exploring Information
# Exercise 3.2 Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the
# program. The following shows two executions of the program:
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input
# Enter Hours: forty
# Error, please enter numeric input
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only untilize techniques
# introduced up to that point in the text.


try:
   hours = float(raw_input('Enter Hours:\n'))
except ValueError:
   print("Error, please enter numeric input.")
   sys.exit(1)
   
try:
   rate = float(raw_input('Enter Rate:\n'))
except ValueError:
   print("Error, please enter numeric input.")
   sys.exit(1)

overtime_hours = 0

if hours > 40:
    overtime_hours = hours - 40
    hours -= overtime_hours
    
print "Pay: " + str(locale.currency(round(rate * hours,2) + round(rate * 1.5 * overtime_hours, 2)))

sys.exit(0)
