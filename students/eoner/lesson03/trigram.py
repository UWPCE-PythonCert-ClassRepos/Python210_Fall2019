path = 'sherlock.txt'
list_text = []
# list of excepted characters
white_list= list("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'")
dictionary_output = {}

#import file, clean up line breaks
def import_text():
    with open(path,'r') as f:
        text = f.read().replace("\n", " ")
    return text
   
#build dictionary try whitelist, check for valid characters, ignore the invalid ones
def build_list(t):
    print(text)
    list_text=list(text.split(" "))
    #print(list_text)
    return list_text

#try whitelist, check for valid characters, ignore the invalid ones
def wordscan(l):
    f = []
    #look at each index of each item in the list, if it matches add to a new orcsdered list
    
    for i in l:
        new =""
        word=i        
        for i in word:
            if i in white_list:
                new += i
            else:
                f.append(new)
                new=""                
        f.append(new)
    
    #still inserting empty elements in the list, crap way of cleaning it up
    f = ' '.join(f).split() 
    print(f)
    return f

def build_dictionary(l):
    l = {}
    for i in range(len(final_list)-2):
        if (final_list[i],final_list[i+1]) not in l:
            #if key pair doesn't exist, update dic so we don't overwrite the value
            l.update({(final_list[i],final_list[i+1]):([final_list[i+2]])})

            #what if the value already exists in the list? keep multiples or clean up?
        elif (final_list[i+2]) in l[(final_list[i], final_list[i+1])]:
            pass
        else:
            #if in the dic keys, append to the value            
            l[(final_list[i], final_list[i+1])].append(final_list[i+2])
    print(l)
    return l

text = import_text()
list_text = build_list(text)
final_list = wordscan(list_text)
source_dic = build_dictionary(final_list)