"""
根据目标文件2.txt把image里面文件的名称移动到3.txt文件中。其中3.txt文件必须包含2.txt文件里面的所有数据，
并且覆盖掉2.txt文件里面原有的重复数据
"""
import os


def file_name(file_dir_1 = 'image/'):
 for root, dirs, files in os.walk(file_dir_1):
  pass
 return files


def read_file():
 list_2 = []
 with open('2.txt', 'r') as f:
  for line in f.readlines():
   list_2.append(line.strip('\n'))
 return list_2


def product_file():
 list1 = read_file()
 for i in range(len(file_name())):
  for j in range(len(read_file())):
   if (read_file()[j]) in file_name()[i]:
    del list1[j]
    list1.insert(j, file_name()[i])
    break
   else:
    continue
   break
 print(list1)
 for k in range(len(list1)):
  with open('3.txt', 'a+') as f:
   f.write(list1[k])
   f.write('\n')



file_name()
read_file()
product_file()


