import random
import time

lunch=['된장찌개', '피자', '제육볶음', '짜장면']

while True:
    print(lunch)
    item=input('음식을 추가해주세요 : ')
    if item=='q':
        break
    else:
        lunch.append(item)
print(lunch)

set_lunch=set(lunch)
while True:
    print(list(set_lunch))
    item=input('음식을 삭제해주세요 : ')
    if item=='q':
        break
    else:
        set_lunch-=set([item])
lunch=list(set_lunch)

print(lunch, '중에서 선택합니다.')
for x in range(5,0,-1):
    print(x)
    time.sleep(1)

print('오늘 먹을 음식은...',random.choice(lunch),'입니다!!')