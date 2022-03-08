def compare(s1,s2,n):
    string1=[]
    string2=[]
    str1=[]
    str2=[]
    string1=s1.split(s1)
    string2=s2.split(s2)



    for i in string1:
        for j in range(n):
            str1.append(i)
        print(str1)

    for i in string2:
        for i in range(n):
            str2.append(j)
        print(str2)
    if (str1==str2):
        return true
    else:
        return false





s1=input("enter the first string")
s2=input("enter the second string")
n=float(input("entrthe limit"))

compare(s1,s2,n)

