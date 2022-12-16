#!/usr/bin/env python
# coding: utf-8

# In[1]:


a = "mukhil"


# In[2]:


b="mukhil"


# In[3]:


a


# In[4]:


b


# In[6]:


c= "this is my name"


# In[7]:


c[0]


# In[8]:


c[-3]


# In[9]:


len(c)


# In[10]:


c[3:10]


# In[13]:


c[10:3:-2]


# In[19]:


for i in range(len(c)):
    print(c[::-1])
    break


# In[20]:


"mukhi"+"rajendran"


# In[21]:


"mukhil" + str(3)


# In[22]:


"m"*5


# In[32]:


c.startswith("m",0)


# In[27]:


c="mukhil"


# In[34]:


c.find("k")


# In[48]:


c="my name is mukhil"
b=c.find("name")
for i in range(len("name")):
    print(int(b)+i)


# In[39]:


c.find("name")


# In[49]:


c.count("name")


# In[53]:


c.split('m')


# In[54]:


c


# In[55]:


c.upper()


# In[56]:


c.lower()


# In[57]:


c.swapcase()


# In[58]:


" ".join(c)


# In[4]:


for i in reversed(c):
    print(i)


# In[10]:


c="     my name is    mukhil    "


# In[12]:


c.strip()


# In[13]:


c.lstrip()


# In[14]:


s="greeting from mukhil"


# In[15]:


s.replace("g",'s')


# In[17]:


s1=s.replace("gr",'swer')


# # 

# In[18]:


s1


# In[19]:


s1.split(" ")


# In[20]:


s


# In[23]:


s.split("o")


# In[25]:


s="kill"


# In[27]:


s.center(23,'h')


# In[28]:


s="sudh\tjay"


# In[29]:


s


# In[30]:


s.expandtabs()


# In[31]:


a="we are all part of ineuron"


# In[32]:


a.lower()


# In[33]:


a.count("a")


# In[38]:


a.rindex("w")


# In[39]:


a.replace("a","ineuron")


# In[41]:


a.split()


# In[42]:


for i in range(len(a)):
    if a[i]=="a":
        print(i)


# In[43]:


a.islower()


# In[44]:


s.isupper()


# In[45]:


s.endswith("s")


# In[49]:


count=0
for i in a:
    count=count+1
print(count)


# In[53]:


for i in range(len(a)):
    print(a[-i])


# In[56]:


s="dada"
ch=len(s)-1
while ch>=0:
    print(s[ch])
    ch=ch-1


# In[57]:


name='ineuron'
vowels="AaEeIiOoUu"

for i in name:
    if i in vowels:
        print("{} is a vowel".format(i))
    else:
        print("{} is not a vowel".format(i))


# In[60]:


"{} name {} dada".format(a,b)


# In[59]:


a=input()
b=input()


# In[62]:


a="xyx"
b=90909
c="kiik"
d= "hih"


# In[63]:


s=input("enter the data: ")
s1=s[::-1]
if s==s1:
    print("its a palindrome")
else:
    print("its not a palindrome")


# In[64]:


l=["sudh",45,4564,6567,[54,767]]


# In[65]:


s="kill him"


# In[67]:


l+list(s)


# In[69]:


len(l)


# In[70]:


453 in l


# In[1]:


l=["mukhil",23,43,45.45,[54,234,5454,"hf"],True]


# In[2]:


for i in l:
    print(i)


# In[3]:


l[::-1]


# In[4]:


for i in l:
    if type(i)==list:
        print(i,"this is a list")
    else:
        print(i,"this is not a list")


# In[7]:


max("dsd","dfdfda","z")


# In[8]:


l=[1,2,3,4]


# In[10]:


l.append("kihds")


# In[ ]:





# In[11]:


l


# In[12]:


l.append(6+6j)


# In[13]:


l


# In[14]:


l.insert(3,"ineuron")


# In[15]:


l


# In[20]:


l.insert(-2,"test")


# In[21]:


l


# In[22]:


l.count("test")


# In[23]:


l.append([1,3,4,53])


# In[24]:


l


# In[25]:


l.extend("test1")


# In[26]:


l


# In[27]:


s="killer"


# In[28]:


list(s)


# In[29]:


l=[1,2,3,4]


# In[30]:


l


# In[34]:


l.extend([3,4,6,454,["sdsda",3,4,3]])


# In[35]:


l


# In[36]:


l.pop()


# In[37]:


l=[3,34,53,4]


# In[38]:


l.pop()


# In[39]:


l


# In[40]:


l.pop(2)


# In[41]:


l


# In[42]:


l=[3,4,45,21,13]


# In[44]:


l.remove(4)


# In[ ]:





# In[45]:


l


# In[47]:


l=[3.4,45,454,["dfdd",454]]

 
# In[48]:


l.reverse()


# In[49]:


l


# In[51]:


l=[45,5243,3,43,2]


# In[52]:


l.sort()


# In[53]:


l


# In[73]:


l=[[1,2,3,4],343,5464,["rter",45,543]]


# In[74]:


l.insert(2,[12,343,43])


# In[75]:


l


# In[ ]:





# In[76]:


l


# In[78]:


for i in l: 
    for k in i:
        if k == string:
            pop(k)
        else:
            print("no string available")
    if i== string:
            pop(i)
    else:
        print("no string available")
  


# In[81]:


l=[]
for i in range(10):
    l.append(int(input()))


# l

# In[82]:


l


# In[1]:


l=[[1,2,4],[43,'b','b','b'],[34,56,'t'],[4,5,3],[7,8,90],"demo",12.5]


# In[ ]:


for i in l:
    if type(i)==list:
        j=0
        while j<len(i):
            if type(i[j]) ==str:
                print("index {}".format(i[j]),j)
            j=j+1
        j=0
        while j<len(i):
            if type(i[j]) is str:
                print("The string in the nested list'{}'".format(  ))


# In[ ]:


for i in l:
    if type(i)==list:
        j=0
        while j<len(i):
            print(i)
            


# In[9]:


l=[[2,34,4],45,[5,7,32,'b','b','b'],[32,'g',67],'HILL',23.5]


# In[10]:


l


# In[11]:


for i in l:
    if type(i)==list:
        j=0
        while j<len(i):
            if type(i[j])==str:
                print("index of str is {}".format(i[j]))
                i.remove(i[j])
                continue
            j=j+1
        


# In[12]:


l


# In[13]:


l=[1,2,3,4,5]


# In[14]:


l1=[]


# In[15]:


for i in "sudh":
    l1.append(i)


# In[16]:


l1


# In[17]:


[i for i in "sudh"]


# In[18]:


l=[]
for i in range(10):
    if i%2==0:
        l.append(i)


# In[19]:


l


# In[20]:


## list comprehension
[i for i in range(10) if i%2==0]


# In[22]:


l=[]
for i in range(10):
    if i%2 !=0:
        l.append("odd")
    else:
        l.append("even")


# In[ ]:





# In[23]:


l


# In[24]:


["odd" if i%2 !=0 else "even" for i in range(10)]


# In[1]:


mat=[]
for i in range(3):
    mat.append([])
    for j in range(3):
        mat[i].append(j)
mat


# In[20]:


mat=[]
for i in range(3):
    mat.append(i)
mat


# In[17]:


[mat for i in range(3)]


# In[23]:


[[j for j in range(3)] for i in range(3)]


# In[26]:


[i for i in range(8) if i%2==0 if i%3==0]


# In[27]:


l=[]
for i in range(10):
    l.append(i)


# In[28]:


l


# In[29]:


["yes " if i==1 else "no" if i==2 else "test" for i in l]


# In[ ]:




