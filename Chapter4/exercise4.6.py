#!/usr/bin/env python
import sys
import locale
locale.setlocale( locale.LC_ALL, '' )

# Python for Informatics Exploring Information
# Exercise 4.6 Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only untilize techniques
# introduced up to that point in the text.

def computepay(hours, rate):
    
    overtime_hours = 0

    if hours > 40:
        overtime_hours = hours - 40
        hours -= overtime_hours
    
    print "Pay: " + str(locale.currency(round(rate * hours,2) + round(rate * 1.5 * overtime_hours, 2)))

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

computepay(hours, rate)

sys.exit(0)
