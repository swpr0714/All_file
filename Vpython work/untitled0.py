import random
min_num = 0
max_num = 99
ans_num = random.randrange(0,99)
while True:
    num = int(input())
    if 0<=num<=99:
        if num > ans_num:
            if num < max_num:
                max_num = num
            print ("在",min_num,"和",max_num,"之間")
        elif num < ans_num:
            if num > min_num:
                min_num = num
            print ("在",min_num,"和",max_num,"之間")
        else:
            print("Bingo答對了😍😍")
            break
    else:
        print("哭喔不要亂喊啦┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻")