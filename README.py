import time

# 设置专注时间为25分钟
focus_time = 25 * 60 

# 倒计时，直到专注时间结束
while focus_time:
    mins, secs = divmod(focus_time, 60)
    timeformat = "{:02d}:{:02d}".format(mins, secs)
    print(timeformat, end="\r")
    time.sleep(1)
    focus_time -= 1
    
print("结束专注时间！")
