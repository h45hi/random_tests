'''Date to Day Converter'''

from datetime import *

year,month,day = [int(x) for x in input('enter a value').split('-')]

def week_day(y, m, d):
  return date(y, m, d).weekday()

z = week_day(year, month, day)

my_dict = {0:"Monday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
print('Entered date is {}'.format(my_dict[z]))