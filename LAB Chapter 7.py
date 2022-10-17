# LAB 7-1
from datetime import date
today = date.today()
print("오늘의 날짜:", today.year,"년", today.month,"월", today.day, "일")
from datetime import time
Time = time(11, 34, 56)
print("현재시간: 오후", Time.hour,"시", Time.minute,"분",  Time.second, "초")

# LAB 7-2
# 1.
import datetime as dt
today = dt.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
xMas = dt.datetime(2025, 10, 17)
time_gap = xMas - today
print("{}년 크리스마스 까지는 {}일 {}시간 남았습니다.".format(\
    xMas.year, time_gap.days,time_gap.seconds//3600))

# 2.
import datetime as dt
today = dt.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
future_date = dt.datetime(2036, 1, 1)
time_gap = future_date - today
print("{}년 새해 까지는 {}일 {}시간 남았습니다.".format(\
    future_date.year, time_gap.days,time_gap.seconds//3600))

# 3.
import datetime as dt
today = dt.datetime.now()
print('오늘은 {}년 {}월 {}일입니다'.format(today.year, today.month, today.day))
birthday = dt.datetime(2022, 10, 20)
time_gap = birthday - today
print("{}년 생일 까지는 {}일 {}시간 남았습니다.".format(\
    birthday.year, time_gap.days,time_gap.seconds//3600))

# LAB 7-3
# 1.
import datetime as dt
print('오늘 =', dt.datetime.now())
thousand = dt.timedelta(days = 1000)
plus1000day = dt.datetime.now() + thousand
print('1000일 후 =', plus1000day)

# 2.
# couple_day.py (1st method)
import datetime as dt
dating_day = input('처음으로 사권 연도와 월, 일을 입력하시오: ')
year, month, day = map(int, dating_day.split(' '))
dating_day = dt.date(year, month, day)
hundred = dt.timedelta(days = 99)
plus100day = dating_day + hundred
print("100일 기념일은 : {}년 {}월 {}일입니다.".format(plus100day.year, plus100day.month, plus100day.day))

# couple_day.py (2nd method)
import datetime as dt
year = int(input('Enter a year'))
month = int(input('Enter a month'))
day = int(input('Enter a day'))
dating_day = dt.date(year, month, day)
hundred = dt.timedelta(days = 99)
plus100day = dating_day + hundred
print("100일 기념일은 : {}년 {}월 {}일입니다.".format(plus100day.year, plus100day.month, plus100day.day))

# LAB 7-3
# 1.
import random as rd
a = list(range(0,101, 5))
rd.randrange(0, 101, 5)
print("0에서 100 이하의 정수 주에서 5의 배수\n", rd.sample(a, 3))

# 2.
import random as rd
a = list(range(1, 11))
print("0에서 10 사이의 임의의 정수:", rd.sample(a, 3))

# LAB 7-4 너무 어려워요
