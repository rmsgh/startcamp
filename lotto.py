import random

numbers = range(1,46)  # range(a,b): a는 포함되고 b는범위에 포함 안됨
#print (random.choice(numbers))
#random.sample(seq,k) : 시퀀스에서 랜덤한 중복되지않는 길이 k의 리스트를 반환

lotto = random.sample(numbers,7) #맨마지막건 보너스
print('로또번호는', lotto)
