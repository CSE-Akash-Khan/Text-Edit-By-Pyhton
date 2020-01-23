
#! read emoji file
# with open('text_emoji.txt','r',encoding='utf-8') as rf: #? we have to change our encoding other wise we can't read our love story
#     print(rf.encoding) #for showing our encoding type
#     data = rf.read()
#     print(data)

#! read big story
# with open('story.txt','r') as rf:
#     data = rf.read()
#     print(data) #? ee vabe kono boro file read kora jabena but soto text file read kora jay. so boro file read korar jonno ja amader korte hobe...

#? amade parse e read korte hobe--that meand for loop use kore read korte hobe lets see
with open('story.txt','r') as rf:
    data = rf.read(100) # amra ee vabe fix kore read korte pari
    while len(data) > 0: #that means joto khon data thkbe totokhon loop ta cholte thakbe
        print(data)
        data = rf.read(100)