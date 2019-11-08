path = 'sherlock_small.txt'
list_text = []
white_list= list("1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'")
dictionary_output = {}
# final_list = []

#import file
def import_text():
    with open(path,'r') as f:
        text = f.read().replace("\n", " ")
    return text
   
#build dictionary try whitelist, check for valid cahracters, ignore the invalid ones
def build_list(t):
    print(text)
    list_text=list(text.split(" "))
    #print(list_text)
    return list_text

#try whitelist, check for valid cahracters, ignore the invalid ones
def wordscan(l):
    f = []
    #look at each index of each item in the list, if it matches add to a new oredered list
    
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
    #clean up: if the key exists :
    # In [253]: ('i','was') in source_dic                                                                                                       

    l = {}
    for i in range(len(final_list)-2):
        if (final_list[i],final_list[i+1]) not in l:
            #if key pair doesn't exist, update dic
            l.update({(final_list[i],final_list[i+1]):([final_list[i+2]])})
        else:
            print(i)
            #if in the dic keys, append to the value
            l[(final_list[i], final_list[i+1])].append(final_list[i+2])
 
    print(l)
    return l

text = import_text()
list_text = build_list(text)
final_list = wordscan(list_text)
source_dic = build_dictionary(final_list)