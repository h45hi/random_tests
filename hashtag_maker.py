"""hashtag maker"""
str_name = input('enter a string & don\'t forget to use _ :')
new_str = str_name.split('_')
final_str = ''

for n in new_str:
  n_title = n.title()
  for n in n_title:
    final_str += n
print('#'+final_str)