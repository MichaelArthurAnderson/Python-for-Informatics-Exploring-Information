#!/usr/bin/env python
import sys

# Python for Informatics Exploring Information
# Exercise 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range print an error.
# If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C 
# Enter score: 0.5
# F
# Run the program repeatedly as shown above to test the various different values for input.
#
# Note:  While there may be other ways to complete this exercise, I'm following the book in order.  Each example will only untilize techniques
# introduced up to that point in the text.


error_message = "Bad score. Scores should be a numeric percentage between 0 and 1 and should not contain letters or punctuation."

grades = {(0,60):"F",(60,70):"D",(70,80):"C",(80,90):"B",(90,101):"A"}
  
def computegrade(score):
    
    score *= 100
    
    grade = error_message
    
    for key in grades:
        if score in range(key[0],key[1]):
            grade = grades[key]
    
    return grade
  
try:

    score = float(raw_input("Enter a numeric percentage score between 0 and 1: "))
        
    print computegrade(score)
        
except:
            
    print error_message

sys.exit(0)
