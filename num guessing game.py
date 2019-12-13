from random import randint

minnum = int(input('Choose the smallest number I can pick '))
maxnum = int(input('Choose the biggest number I can pick '))

answer = randint(minnum, maxnum)
userguess = int(input('What is the number I am thinking of from ' + str(minnum)
                      + ' to ' + str(maxnum) + " "))

while userguess != answer:
    if userguess < answer:
        print('Higher! ')
        userguess = int(input('Try again! '))
        
    elif userguess > answer:
        print('Lower! ')
        userguess = int(input('Try again! '))
    
print('Correct! ')
print('To play again, press run!')