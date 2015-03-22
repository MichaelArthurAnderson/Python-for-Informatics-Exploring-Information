#!/usr/bin/env python
import sys
import locale
locale.setlocale( locale.LC_ALL, '' )

# Python for Informatics Exploring Information
# Exercise 3.1 Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.


try:
   hours = float(raw_input('Enter Hours:\n'))
except ValueError:
   print("Entered hours must be an integer or floating point number.")
   sys.exit(1)
   
try:
   rate = float(raw_input('Enter Rate:\n'))
except ValueError:
   print("Entered rate must be an integer or floating point number.")
   sys.exit(1)

overtime_hours = 0

if hours > 40:
    overtime_hours = hours - 40
    hours -= overtime_hours
    
print "Pay: " + str(locale.currency(round(rate * hours,2) + round(rate * 1.5 * overtime_hours, 2)))

sys.exit(0)
