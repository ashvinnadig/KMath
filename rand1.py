"""
4 6 digit numbers and their sum. Print and fold
"""
from random import randint

lstj = []
for j in range(4):
    sum_int = 0
    lsti = []
    for i in range(4):
        randnum = randint(99999, 1000000)
        sum_int += randnum
        lsti.append(randnum)
    lsti.append(sum_int)
    lstj.append(lsti)

for i in range(4):
    print("{:>12}\t{:>12}\t{:>12}\t{:>12}".format(lstj[0][i], lstj[1][i], lstj[2][i], lstj[3][i]))

print("*"*65+"\n\n\n\n")
print("*"*65)

i = 4
print("{:>12}\t{:>12}\t{:>12}\t{:>12}".format(lstj[0][i], lstj[1][i], lstj[2][i], lstj[3][i]))