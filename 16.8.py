list_a = [['A','7','9','T','K','Q'],['M','I','N','C','O','D']]

a, b = input().split()
answer = [a, b]

def isExist(x):
    for i in range(2):
        for j in range(6):
            if list_a[i][j]== x:
                return 1
    return 0



for i in range(2):
    if isExist(answer[i]):
        print('존재')
    else:
        print('없다')
