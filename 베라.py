
menu_type = input('컵으로 하실건가요 콘으로 하실건가요?:')


#메뉴가 컵일때
if menu_type == '컵':

    print('컵 크기: 파인트(3가지맛) 9800원, 쿼터(4가지맛) 18500원, 패밀리(5가지맛), 하프갤런(6가지맛)')

    size = input('컵 크기를 입력해주세요: ')

    def lim_taste():
        global taste_kind
        
        while  taste_kind.count(',') >= taste_number :
            taste_kind = input(f'이 사이즈는 {taste_number}맛 까지만 선택이 가능하세요 다시 선택해주세요.:')
        else:  print('{}을 선택하셨습니다.'.format(taste_kind))

    taste_number = 3
    taste_kind = ['민트초코','엄마는 외계인','슈팅스타','뉴욕 치즈케이크','바닐라','베리베리스트로베리','오레오 쿠키앤크림']

    taste_kind = input(f'민트초코,엄마는 외계인,슈팅스타,뉴욕 치즈케이크,바닐라,베리스트로베리,오레오 쿠키앤크림 (중 {taste_number}개를 택하세요) ')

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

#메뉴가 콘일때
elif menu_type == '콘':
    price = 3500
    taste_kind = input('민트초코,엄마는 외계인,슈팅스타,뉴욕 치즈케이크,바닐라,베리스트로베리,오레오 쿠키앤크림 (중 1개를 택해주세요)')

    
    while taste_kind.count(',') > 0:
        taste_kind = input('이 맛은 1가지 까지만 선택이 가능합니다. 다시 선택해주세요.:')
    else: print(f'{taste_kind}를 선택하셨습니다.')
    
cups = int(input('수량을 입력해주세요.(숫자로만):')) 

total_price = cups * price

payment_method = input('카드로 하실건가요 현금으로 하실건가요.:')

if payment_method == '현금':
    recieved_money = int(input(f'가격은 {total_price}원 입니다. 현금을 투입해주세요.:'))
    while recieved_money < total_price:
        recieved_money = int(input('금액이 부족합니다. 금액을 추가로 투입해주세요:'))
        
    else: 
        change = recieved_money - total_price
        print(f'거스름돈은 {change}원 입니다')

elif payment_method == '카드':
    print('카드를 꽂아주세요.')
    recieved_money = total_price

print('결제가 완료되었습니다.')