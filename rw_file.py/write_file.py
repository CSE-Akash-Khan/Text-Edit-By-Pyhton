
#! for writing we use three type of command
#todo: tutorial 215
#? 1. w
#? 2. a
#? 3. r+

#! use w command
#? if any data store in text file before. then its deleted and keep new data
# # with open('write1.txt','w') as f: #todo: jodi age theke file create kora na thake then eti file er nam dile auto create kore nibe and ja lekha dewa thakbe ta likha hoye jabe
# with open('write.txt','w') as f:
#     f.write('hello rana') # its deleted previous data and store new data

#! use a command
#? if any data store in file then its add new data. and don't delete previus data
# # with open('write3.txt','a') as f: #? its also can make folder autometicly
# with open('write.txt','a') as f:
#     f.write("\nhow are you")

#! use r+ command
#? its can be use for read and write both. but its can't make new file
#? r+ command replace previus data when we use write mode. jototuku write kora hobe thik outotuku replace korbe bakita theke jabe. but we can write data without delete use seek methode

# with open('write.txt','r+') as w:
#     w.seek(len(w.read())) #? its change our cursor position.cursor position move to end
#     w.write('\ni am writing')

#todo: one usefull terminal command
#? its make new file and writen this item
# echo -e "hello\n i am akash khan" >> write.txt

#! read and write
# with open('write.txt','r') as f:
#     with open('new_write.txt','w') as w:
#         w.write(f.read())

#! exercise
# with open('write.txt','r') as rf:
#     with open('new_write.txt','w') as wf:
#         for i in rf.readlines():
#             name,selary = i.split(',')
#             wf.write(f"{name}'s selary is {selary}")

#! exercise 2

with open("link.txt",'r') as rf:
    with open("output1.txt",'w') as wf:
        for line in rf.readlines():
            # var = rf.find('<href = ')
            # if line[var:var+8] == '<href = ':
            if '<href' in line:
                store = line.find('"')
                store2 = line.find('"',store+1)
                wf.write(f"{line[store+1:store2]}\n")

#! batter solution of ex:2
#? tutorial 221
# with open('link.txt','r') as webpage:
#     with open('output1.txt','w') as wf:
#         rf = webpage.read()
#         link_exist = True
#         while link_exist:
#             pos = rf.find('<href')
#             if pos == -1:
#                 link_exist = False
#             else:
#                 first_quat = rf.find('"')
#                 second_quat = rf.find('"',first_quat+1)
#                 url = f"{rf[first_quat+1:second_quat]}\n"
#                 wf.write(url)
#                 rf = rf[second_quat:]
