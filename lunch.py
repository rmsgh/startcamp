# 주석은 해석되지 않음
# ctrl + / : 선택한 문장 주석처리 단축키 (IDE마다 다름)
# 리스트는 가변 , array는 고정길이
# 임의의 값을 뽑아오는 기능 

menu = ['한식', '일식', '중식', '양식' , '굶기']

import random
lunch = random.choice (menu) 
# print(lunch)

number = {'한식': '1234-5678', '일식' : '4545-4545', '중식' : '4587-5452', '양식' : '4546-1212' , '굶기' : '0'}
# print(number[lunch])

#오늘의 점심은 xxx입니다. 전화번호는  xxxx-xxxx입니다
print('오늘의 점심은',lunch,'입니다. 전화번호는 ',number[lunch],'입니다')
print(f'오늘의 점심은 {lunch}입니다. 전화번호는 {number[lunch]} 입니다.')