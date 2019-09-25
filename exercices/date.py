import datetime

# f_m = '13-08-2019 20:02:20'

# def form_date(param):
#     f_m = '13/08/2019 20:02:20'
#     format_date = datetime.datetime.strptime(f_m, '%Y-%m-%d %H:%M:%S')
#     return format_date

# print(str(form_date(f_m)))
date_time_str = '13/08/2019 20:02:20'

def f_date(fe):
    date_time_obj = datetime.datetime.strptime(fe, '%d/%m/%Y %H:%M:%S')
    return date_time_obj.date()

print(str(f_date(date_time_str)))

# print('Date:', date_time_obj.date())
# print('Time:', date_time_obj.time())
# print('Date-time:', date_time_obj)