'''Bug-->Error in the program which prevents it from running as expected.
Finding and fixing bugs is called Debugging.
Types of errors:
1. Syntax Error: occurs due to violation of programming language rules.
2. Logical Error: occurs when program runs but gives wrong output.  
3. Runtime Error: occurs during program execution.
debugging techniques:
1. Print Statements:
2. try-exc
3.using of pdb
'''
try:
    num=int(input("Enter a number:"))
    print(10/num)
except ZeroDivisionError:
    print("can not divide by Zero")
except ValueError:
    print("Invalid Input")
