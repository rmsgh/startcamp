#조건에 따른 실행문장 선택하기 : 조건문

dust = 55
#if 조건문  :
# 실행할 문장
if dust > 50 :
    print("50초과")
else :
    print("50이하")
 
 #들여쓰기 맞춰야함!!!


 #if elif else 순서대로!
 # 0~30 31~80 81~150 150~ 
if dust > 150 :
    print('메우나쁨')
elif dust > 80 :
    print('나쁨')
elif dust > 30 :
    print('보통')
else :
    print('좋음')


    ## while 은 조건 만족할때까지 for 은 특정함수