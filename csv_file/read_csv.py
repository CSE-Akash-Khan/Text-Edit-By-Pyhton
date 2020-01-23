
#? we use csv file for store tebuler data. that means table akare je data gulo sajano thake

#! read csv file use reader
# from csv import reader #or 
# with open('file.csv','r') as rf:
#     read_csv = reader(rf) #? its returned object
#     # print(read_csv) #? its a iterator
#     #? so we can use for loop with this, we can take any action with this file
#     next(read_csv) #? its use for unshowing header of the csv file
#     for i in read_csv:
#         print(i)

#! another way read csv file use DictReader
#todo: its best way

# from csv import DictReader #? it will print ordered dictionary
# with open('file.csv','r') as rf:
#     diect_reader = DictReader(rf)
#     # print(diect_reader) #? its iterator
#     for row in diect_reader:
#         # print(row)
#         print(row['name']) #? its will print only name as a ordered,you can print any thing
#         # print(row['email'])
'''actually how it is work..first of all every headers one element come into the row when for loop run one time. then we can print speceficly one item of them example: when loop run one time then row = akash,khanakash779@gmail.com,01766738256. when we print any fixed itme then row[name]-- then print-- akash. 2nd time when loop run then row= rana,rana@gmail.com,01714224890. then again see row[name]-- then print rana. this way actually work'''

#! change delimiter
# #? actually csv file as a defult always separeted by comma, but we can change our delimiter
# from csv import DictReader
# with open('file.csv','r') as rf:
#     diect_reader = DictReader(rf,delimiter = '|') # we can use its also with reader 
#     for row in diect_reader:
#         print(row['email'])
