"""This app will help you generate strong password of user given length"""

import string
import random
import re

pwd = []
def password(size):
  combined = string.printable # printable = digits+ascii_letters+punctuation+whitespace
  # combined = string.ascii_letters+string.digits+string.punctuation
  choice = random.sample(combined,size) # random sampling of mentioned size
  pwd = ''.join(choice)
  
  # methods for removing illegal characters in a password
  
  # method 1
  # pwd = ''.join(pwd.split(' ')) # remove spaces and join the strings
  
  #method 2
  pwd.replace(' ','!').replace('\n','!').replace('\t','!')

  # method 3
  # char_list = ['\n','\t',' ']
  # pwd = re.sub("@".join(char_list), "",pwd)
  
  return pwd

size = int(input("enter the size of password you need"))
pwd = password(size)

print(pwd)