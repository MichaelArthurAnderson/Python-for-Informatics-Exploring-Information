#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 4.2 Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only utilize techniques
# introduced up to that point in the text.

repeat_lyrics()

def print_lyrics():
    print "I'm a lumberjack, and I'm okay."
    print 'I sleep all night and I work all day.'

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

sys.exit(0)



