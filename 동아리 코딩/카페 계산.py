print('메뉴:아메리카노 1400원, 딸기 라떼 3000원, 자바칩 초코 프라페 5000원')

menu = input('메뉴를 입력해주세요:')


if menu == '아메리카노':
    coffe_price = 1400
elif menu == '딸기 라떼':
    coffe_price = 3000
elif menu == '자바칩 초코 프라페':
    coffe_price = 5000

cups = int(input('몇잔을 드릴까요'))

total_price = coffe_price * cups


received_cash = int(input('총 금액: {}. 지불하실 돈을 넣어주세요'.format(total_price)))
if received_cash >= total_price:
    change = received_cash - total_price
    print('거스름돈은 {}입니다'.format(change))
else:
    print('금액이 부족합니다')

 



    


