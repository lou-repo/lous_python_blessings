#!/bin/python

#take mcq marks
mcq_marks = float(input("Enter the MCQ marks: "))
#take theory marks
theory_marks = float(input("Enter the theory marks: "))

#check the passing condition using AND and OR operator
if (mcq_marks >= 40 and theory_marks >= 30 ) or (mcq_marks + theory_marks) >=70:
    print("\n You have passed." )
else:
    print("\n You have failed.")