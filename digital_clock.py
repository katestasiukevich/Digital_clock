import time, os
from clocknum import *
from random import choice


def clock():
    t = time.localtime()

    hour = str(t.tm_hour) if int(t.tm_hour) > 9 else '0' + str(t.tm_hour)
    minute = str(t.tm_min) if int(t.tm_min) > 9 else '0' + str(t.tm_min)
    second = str(t.tm_sec) if int(t.tm_sec) > 9 else '0' + str(t.tm_sec)
    
    clock_face = [] #generates the current displayed time from 'square' symbols
    for i in range(7):
        for h in hour:
            h = int(h)
            clock_face.append(nums[h][i])
        clock_face.append(separator[i])
        for m in minute:
            m = int(m)
            clock_face.append(nums[m][i])
        clock_face.append(separator[i])
        for s in second:
            s = int(s)
            clock_face.append(nums[s][i])
        print(*clock_face)
        clock_face.clear()
    
    time.sleep(0.9)
    os.system('cls||clear')


colors = ['🟥', '🟧', '🟨', '🟩', '🟦', '🟪', '🟫', '⬛', '⬜']
start_color = '⬛'

while True:
    change_color = choice(colors)
    for num in nums:
        for i in range(7):
            num[i] = num[i].replace(start_color, change_color)
    start_color = change_color
    
    clock()
    animation()
