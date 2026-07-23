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
pdb-->python debugger module
1.pause execution at certain points
2.inspect variables
pdb commands:
1.n(ext): execute next line
2.p(rint) <variable_name>: print value of variable
3.c(ontinue): continue execution 
4.l(ist): list nearby code
5.s(tep): to start function
6.r(eturn): continue execution until current function returns
7 h(elp): list available commands
8 q(uit): quit the execution
'''
try:
    num=int(input("Enter a number:"))
    print(10/num)
except ZeroDivisionError:
    print("can not divide by Zero")
except ValueError:
    print("Invalid Input")
#pdb example
import pdb
def add(a,b):
    pdb.set_trace()
    return a+b
a=int(input())
b=int(input())
print(add(a,b))