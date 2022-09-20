#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   List - making selections from complex lists"""

import random

def main():
    wordbank= ["indentation", "spaces"]
    
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]
    
    wordbank.append(4)
    print(wordbank)

    num =(input("Enter a number between O and 18 (inclusive): or a name or random "))

    if num.isdigit():
        student_name = tlgstudents[int(num)]
    elif num in tlgstudents:
        student_name = num

    else:
        student_name = random.choice(tlgstudents)

    print(f"{student_name}  always uses { wordbank[2]} { wordbank[1]} to indent.")
main()
