
#! write csv file use writer
# from csv import writer
# with open('write_file.csv','w',newline='') as wf: #? for removing space
    # csv_writer = writer(wf)#its return object

    #todo: for writing we can use 2 methode
    #) 1. writerow-- its take input as a list and create one list one time
    #) 2. writerows-- its take input as a list and inside can take many list

    #? use writewrow
    # csv_writer.writerow(['name','country'])
    # csv_writer.writerow(['akash','bangla'])
    # csv_writer.writerow(['rana','India'])

    #? use writewrows
    #todo: it's best way for use
    # csv_writer.writerows([['name','country'],['akash','bangladesh'],['rana','India']])


#! write csv file use DictWriter. its return dictionary
#todo: its best way for write csv file.
from csv import DictWriter
with open('write_file2.csv','w',newline='') as wf:
    csv_writer = DictWriter(wf,fieldnames = ['first_name','last_name','age']) #when you use DidctWriter always you have to specefi what is header in your file. its a very good think
    csv_writer.writeheader() #its will be create your header which you defined

    #todo: hears also befores two methode
    #)1. writerow    #)2. writerows
    
    # #? use writerow -- its create dictionary
    # csv_writer.writerow({
    #     'first_name' : 'akash',
    #     'last_name'  : 'khan',
    #     'age'        :20
    # })
    # csv_writer.writerow({
    #     'first_name' : 'rana',
    #     'last_name'  : 'khan',
    #     'age'        :20
    # })

    #? use writerows methode
    #todo: its best way for writing. and its take a list and inside too many dictionary
    #todo: example: [dict,dict,dict........]
    csv_writer.writerows([
        {'first_name':'akash','last_name':'khan','age':22},
        {'first_name':'rana','last_name':'khan','age':22},
        {'first_name':'naim','last_name':'khan','age':22},
        {'first_name':'sohel','last_name':'khan','age':22}
    ])