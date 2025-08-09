#comprehension in py
import math 
def isprime(num:int) -> bool:
    """check wheter the number  is prime"""
    for i in range(2,math.floor(math.sqrt(num)+1)):
        if num%i == 0:
            return False
    return True

# print(isprime(15))

# l1  = [x for x in range(1,100000000)]
# l2 = []
# for i in l1 :
#     if isprime(i)== True:
#         l2.append(i)
# print(l2)
l1 = [x for x  in range(2,100000)if isprime)]