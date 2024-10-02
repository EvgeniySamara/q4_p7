# Задание 1. Функцию группового переименования файлов.
# Напишите функцию группового переименования файлов. Она должна:
# 1. принимать параметр желаемое конечное имя файлов. При
# переименовании в конце имени добавляется порядковый номер.
# 2. принимать параметр количество цифр в порядковом номере.
# 3. принимать параметр расширение исходного файла. Переименование
# должно работать только для этих файлов внутри каталога.
# 4. принимать параметр расширение конечного файла.
# 5. принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик
# файлов и расширение. 3.Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами.
#
import os
from xml.dom.pulldom import parse


# from os import listdir
# from os.path import isfile, join


def group_rename(target_dir,wish_name, num_len,file_ext,wish_ext):

    def do_rename(old,new):
        os.rename(old,new)


    os.chdir(target_dir)
    num_limit = int('9'*num_len)
    # print(num_limit)
    filelist =  os.listdir()

    print(filelist)
    i = 0

    for file in filelist:

        if file_ext!='':
            parsename = file.split('.')
            if len(parsename)<2:
                continue
            else:
                if parsename[1]==file_ext:
                    i+=1
                    cur_num = str(i).rjust(num_len, '0')
                    new = f'wish_name{cur_num}.{wish_ext}'
                    do_rename(file,new)
        else:
            i += 1
            cur_num = str(i).rjust(num_len, '0')
            new = f'wish_name{cur_num}.{wish_ext}'
            do_rename(file, new)

    print(f"Переименовано {i} файлов")

group_rename('test_dir','newfile', 3,'me','txt')



# os.mkdir('test_dir')
# for i in range (10,16):
#     with open (f'file{i}',"w") as f1:
#         pass



# print(os.listdir('c:\\'))
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(os.getcwd())
# from os import walk
#
# f = []
# for (dirpath, dirnames, filenames) in walk(mypath):
#     f.extend(filenames)
#     break
# or, shorter:
# from os import walk
#
# filenames = next(walk(mypath), (None, None, []))[2]  # [] if no file