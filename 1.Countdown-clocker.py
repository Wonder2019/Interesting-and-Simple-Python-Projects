#
import time
total_time = 0
while True:
    try:
        print("\n")
        total_minutes = float(input("Please input the minutes: \n")) # 输入倒计时分钟数
        total_seconds = int(total_minutes * 60) # 转为秒数
        total_time += total_seconds
        starttime = time.time() # 当前时间
        print('Started')
        current = 0
        while current <= total_seconds:
            print("\r", total_seconds - current, 'Seconds Left', end='', flush=True) # 保证打印出的剩余时间在一行重复刷新打印
            time.sleep(1)
            current += 1
    except:
        print('\nStopped')
        endtime = time.time()
        print('Total Time:', round(total_time, 0),'secs')
        break
