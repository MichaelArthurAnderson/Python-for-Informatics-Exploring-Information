#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 6.5 Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only untilize techniques
# introduced up to that point in the text.

text = "X-DSPAM-Confidence:    0.8475";

print float(text[text.find(':') + 1:len(text)])

sys.exit(0)
