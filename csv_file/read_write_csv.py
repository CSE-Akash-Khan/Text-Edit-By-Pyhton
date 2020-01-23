
#? first of all we will read a csv file. and write another file use befores csv file data. and make some update new csv file
#? for this we can use (reader or DictReader and writer or DictWriter) you can use bouth..bouth of them

from csv import DictReader, DictWriter
with open('write_file2.csv','r') as rf:
    with open('write_update.csv','w',newline='') as wf:
        dict_reader = DictReader(rf) #tis return dictionary
        dict_writer = DictWriter(wf,fieldnames = ['FirstName','LastName','age'])
        dict_writer.writeheader()

        for row in dict_reader:
            fname,lname,age = row['first_name'], row['last_name'], row['age']

            # dict_writer.writerow({
            #     'FirstName' : fname.upper(),
            #     'LastName'  : lname.upper(),
            #     'age'       : age
            # })
            #! or
            dict_writer.writerows([
                {'FirstName': fname.upper(),'LastName' : lname.upper(),'age':age}
            ])