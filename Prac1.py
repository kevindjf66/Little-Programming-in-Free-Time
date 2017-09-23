'''
for number 1, 2, 3, 4, how many three-digits number can be gotten from the four numbers?
'''
#set a counter
count = 0
#set three loops to get the answers
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print i,j,k
                count += 1
print count
