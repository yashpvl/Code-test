import ast
import sys


if len(sys.argv) != 3:
    print("Invalid input")
    exit(1)
arg1 = sys.argv[1]
arg2 = sys.argv[2]

def sortlist(list1, list2):
    list_joined = ast.literal_eval(list1) + ast.literal_eval(list2)
    list_joined.sort()
    return list_joined
print(sortlist(arg1,arg2))
