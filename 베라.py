print('컵 크기: 파인트(3가지맛) 9800원, 쿼터(4가지맛) 18500원, 패밀리(5가지맛), 하프갤런(6가지맛)')

size = input('컵 크기를 입력해주세요: ')

taste_number = 3

def lim_taste():
    global taste_kind
    if len(taste_kind) > taste_number:
        taste_kind = input(f'이 사이즈는 {taste_number}맛 까지만 선택이 가능하세요 다시 선택해주세요')
    else: print('{}을 선택하신거 맞으세요?'.format(taste_kind))

taste_kind = ['민트초코','엄마는 외계인','슈팅스타','누욕 치즈케이크','바닐라','베리베리스트로베리','오레오 쿠키앤크림']
taste_kind = input(f'민트초코,엄마는 외계인,슈팅스타,뉴욕 치즈케이크,바닐라 (중 {taste_number}개를 택하세요) ')

if size == '파인트':
    price = 9800
    taste_number 
    lim_taste() 

elif size == '쿼터':
    price = 18500
    taste_number += 1
    lim_taste()

elif size == '패밀리':
    price = 26000
    taste_number += 2
    lim_taste()

elif size == '하프갤런':
    price = 31500
    taste_number += 3
    lim_taste()

cups = int(input('몇 개를 드릴까요: '))

total_price = cups * price

received_cash = int(input(f'가격은 {total_price}원 입니다. 얼마를 주실건가요'))

if received_cash >= total_price:
    change = received_cash - total_price
    print(f'거스름돈은 {change}원 입니다')
else: print('가격이 부족합니다.')






