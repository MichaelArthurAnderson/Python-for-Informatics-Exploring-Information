#!/usr/bin/env python
import sys
import locale
locale.setlocale( locale.LC_ALL, '' )

# Python for Informatics Exploring Information
# Exercise 2.3 Write a program to prompt the user for hours and rate per hour to compute gross pay.
# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25
# We won't worry about making sure our pay has exactly two digits after the decimal place for now. If you want, you can play with the built-in Python round function
# to properly round the resulting pay to two decimal places.
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
   
print "Pay: " + str(locale.currency(round(rate * hours,2)))

sys.exit(0)
