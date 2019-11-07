path = 'sherlock_small.txt'
list_text = []
white_list= list("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")


#import file
def import_text():
    with open(path,'r') as f:
        text = f.read().replace("\n", " ")
    return text

# #build dictionary
# def build_dictionary(t):
#     #sanitize
#     #get rid of line breaks
#     text=(t.replace("\n", " ").replace("--"," ").replace("(","").replace(")","").replace(",","").replace(".","").replace("-"," "))
#     print(text)
#     list_text=list(text.split(" "))
#     print(list_text)
   
#build dictionary try whitelist, check for valid cahracters, ignore the invalid ones
def build_list(t):
    print(text)
    list_text=list(text.split(" "))
    #print(list_text)
    return list_text

#try whitelist, check for valid cahracters, ignore the invalid ones
def wordscan(l):
    build_list = []
    #look at each index of each item in the list, if it matches add to a new oredered list
    
    for i in l:
        new =""
        word=i        
        for i in word:
            if i in white_list:
                new += i
            else:
                build_list.append(new)
                new=""                
        build_list.append(new)
    
    #still inserting empty elements in the list, crapp yway of cleaning it up
    build_list = ' '.join(build_list).split() 
    print(build_list)

text = import_text()
list_text = build_list(text)
wordscan(list_text)