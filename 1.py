#根据给定的年月日以数字形式打印出日期
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
    ]
day_th = ['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

year = input("year:")
month = input("month:")
day = input("day:")

month_num = int(month)
day_num = int(day)
month_sp = months[month_num-1]
day_sp = day + day_th[day_num-1]

print(year+','+month_sp+','+day_sp)
