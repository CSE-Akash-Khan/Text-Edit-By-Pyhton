
#! read text file
#? tutorial:- 213
#todo: discouse about
#! read file
#! open function
#! seek file
#! tell file
#! readline methode
#! readlines methode
#! close methode

#todo: open function and read file
# f = open('file1.txt','r') #? we can do 2 tipes of operation with file read(r) and write(w). by defult it's complete read operation
# print(f.read())
# print(f.read()) #? its will be readed one time. becouse its read according to cursor
# f.close() #?always we should close after reading file

#todo: tell methode-->its use for showing cursor position
# f = open('file1.txt','r')
# print(f"coursor position {f.tell()}") #? here start
# print(f.read())
# print(f"coursor position {f.tell()}") #? here end
# f.close()

#todo: seek methode--> by this we can change our cursor position.. cursor position jekhane dibo oikhan theke read start korbe
# f = open('file1.txt','r')
# print(f"coursor position {f.tell()}")
# print(f.read())
# print(f"coursor position {f.tell()}")
# print('......................................')
# print(f'before seek methode..... cursor positon was {f.tell()}')
# f.seek(0) # now cursor position is 0 that means its now again starting position
# f.seek(50) # now cursor position is 50 that means its now again starting from 50 th position
# print(f"after seek methode...now cursor position is {f.tell()}")
# print(f.read()) #again it's readed
# print(f.close)

#todo: readline methode--> its print one line one time
f = open('file1.txt','r')
# print(f.readline(),end="") #?its remove our space between 2 lines
# print(f.readline())
# print(f.readline(),end="")
#todo: readlines methode--> its add every lines under the list
# f = open('file1.txt','r')
# lines = f.readlines()
# print(lines)
# print(len(lines))
#? we can use for loop with this
# for line in lines:
#     print(line,end="")
# #! or
# f = open('file1.txt','r')
# for line in f:
#     print(line)
#?-- one more usefull things with readlines
# for line in f.readlines()[:2]: #?we can slicing with our text file.. amra amader issa moto line print korte pari
# # for line in f.readlines(): #? we can print every line use it
#     print(line,end="")

#todo: show file name
#? for this we use data discriptor---2 types of data discriptor
#? 1. name, 2. closed
# f = open('file1.txt','r')
# print(f.name)
# print(f.closed)# its checked that is our file close or not, if close return True else return False#?return False
# print(f.close())
# print(f.closed) #? return True

#todo: if file1.txt stay another file then what happend
# f = open(r'C:\Users\Dell\Desktop\problem_solve\file1.txt')#?have to copy full path and put r before string
# # f = open(r'C:/Users/Dell/Desktop/problem_solve/file1.txt') #? if we change back slash to forword slash then its will be right
# print(f.read())
# print(f.close())


#?...............................its a batter idea for read file.........................................

#! read file with block--it's autometicly closed file
#? its called context manager
with open('file1.txt','r') as f:
    data = f.read()
    print(data)
    # print(f.read())
print(f.closed) #? its autometicly closed file. don't needed to close