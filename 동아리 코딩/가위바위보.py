import random


computer = random.choice (['가위','바위','보'])
user = input('나:')

print('컴퓨터:{}'.format(computer))

if computer == '가위':
    if user == '가위':
        print('비기셨습니다')
    elif user == '보':
        print('지셨습니다')
    elif user == '바위':
        print('이기셨습니다')
        
elif computer == '보':
    if user == '가위':
        print('이기셨습니다')
    elif user == '보':
        print('비기셨습니다')
    elif user == '바위':
        print('지셨습니다')
     

elif computer == '바위':
    if user == '가위':
        print('지셨습니다')
    elif user == '보':
        print('이기셨습니다')
    elif user == '바위':
        print('비기셨습니다')
     

