import operator
def most_frequent(string):
    d1=dict()
    for key in string:
        if key not in d1:
            d1[key]=1
        else:
            d1[key]=d1[key]+1
    sorted_d1=dict(sorted(d1.items(),key=operator.itemgetter(1),reverse=True))
    print("letters in decreasing order of frequency of appearance: ")
    for key in sorted_d1:
        print(str(key)+" = "+str(sorted_d1[key]))

    
s1=input("Please enter a string: ")
s2=s1.lower()
most_frequent(s2) 
