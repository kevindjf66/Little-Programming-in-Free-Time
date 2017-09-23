'''
There is one integer. After 100 plus the integer, it comes out a number which could be rooted evenly.
Then after the number plus 168, it comes a number could be rooted evenly again.
'''
# x + 100 = n^2, x + 100 + 168 = m^2
# m^2 - n^2 = 68
# (m + n)(m - n) = 168
# m + n = i, m - n = j, i * j = 168
# m = (i + j) / 2, n = (i - j) / 2
# i and j are both even
# so 

for i in range(1,85):
    if 168 % i == 0:
        j = 168 / i;
        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)
