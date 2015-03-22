#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 2.2 Write a program that uses raw_input to prompt a user for their name and then welcomes them.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only untilize techniques
# introduced up to that point in the text.

name = raw_input('What is your name?\n')

print "Welcome " + str(name) + "!"

sys.exit(0)


