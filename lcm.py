x = int(input("enter a number"))
y = int(input("enter a number"))
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
         if(greater % x == 0) and (greater % y == 0):
             lcm = greater
             break
         greater += 1
    return lcm
print("lcm",compute_lcm(x, y))