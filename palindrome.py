my_str='malayalam'
my_str=my_str.casefold()
rev_str=reversed(my_str)
print()
if list(my_str)==list(rev_str):
    print("the string is a palindrome.")
else:
    print("the string is not a palindrome")