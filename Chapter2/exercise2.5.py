#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 2.5 Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit and print out the converted temperature.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only untilize techniques
# introduced up to that point in the text.

try:
   temp = float(raw_input('Enter the temperature in Celsius:\n'))
except ValueError:
   print("Temperature must be an integer or floating point number.")
   sys.exit(1)

print str(temp) + " degress Celsius is " + str( round( ( (9.0 / 5.0) * float(temp) ) + 32, 2 ) ) + " degrees Fahrenheit."

sys.exit(0)


