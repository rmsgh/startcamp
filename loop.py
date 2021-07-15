dust =[49,55,80,75,39]
i = 0
while i < 5 :
  
    print(dust[i])
    i = i + 1

#i=0
#while i < 5 :
 #   i = i + 1
  #  print(dust[i])

    for e in dust :
        print('for문입니다')
        print(e)

#while 문과 같이 반복 계수를 이용해서 인덱스에 접근하여 출력
for i in range(5) :  # i : 0~4 증가하는 변수
    print('for문입니다.222')
    print(i)
    print(dust[i])