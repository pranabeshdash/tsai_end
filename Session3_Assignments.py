#!/usr/bin/env python
# coding: utf-8

# In[163]:


# Assignment 1
#Write a function using only list filter lambda that can tell whether 
#a number is a Fibonacci number or not. You can use a pre-calculated
# list/dict to store fab numbers till 10000 
def getFabNumList():
    endNum = 10000
    listOfNum = [0,1]
    for i in range(endNum):
        if i == 0 or i == 1:
            continue
        nextNum = listOfNum[i-2] + listOfNum[i-1]
        if nextNum <= endNum:  
            listOfNum.append(nextNum)
            #print(nextNum)
        else:
            break
    return listOfNum;

#print (getFabNumList())
fn = lambda i: True if i in getFabNumList() else False 
fn(6765)


# In[16]:


#Assignment 2 Prob 1 - 
#add 2 iterables a and b such that a is even and b is odd
1/(1 + np.exp(-x)) 
b = [11,12,13,4,5,6]
list(map (lambda x,y: x+y, list(filter(lambda x : x % 2 == 0, a)),           list(filter(lambda x : x % 2 != 0, b))))


# In[5]:


#Assignment 2 Prob 2 - 
#strips every vowel from a string provided (tsai>>t s)
t_str = 'whois there'
no_vowel = ''.join(filter (lambda x : False if x in ['a', 'e', 'i', 'o', 'u'] else True, list(t_str)))
print (no_vowel)


# In[11]:


#Assignment 2 Prob 3 - 
#acts like a ReLU function for a 1D array
arr = [-1, -5, -3, -12345, 5, 8, 12, 12345]

list(map (lambda x : max(0,x), arr))


# In[59]:


#Assignment 2 Prob 4 -
# acts like a sigmoid function for a 1D array
import numpy as np 
import math

arr = [-1, -5, -3, -200, 5, 8, 12, 123]
list(map(lambda x: 1.0/(1 + np.exp(-x)), arr)) 


# In[175]:


#Assignment 2 Prob 5 - 
#takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
t_str = 'whois'

# ord('a') = 97 , ord('z')  122, ord('A') = 65 ord('Z') = 90
"".join(list (map(lambda x : chr(ord(x)+5) if ord(x) > 96 and ord(x) < 118 else chr(97+ord(x)+5-122-1), t_str)))


# In[229]:


#Assignment 3 
# A list comprehension expression that takes a ~200 word 
# paragraph (write your own paragraph to check), and checks 
# whether it has any of the swear words mentioned in 
# https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt
import urllib
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    getData = False
    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        for attr in attrs:
            if (attr[0] == 'itemprop' and attr[1] == 'text'):
                if (MyHTMLParser.getData == False):
                    MyHTMLParser.getData = True
                print("     attr:", attr,MyHTMLParser.getData)

#    def handle_endtag(self, tag):
#        print("End tag  :", tag)

    def handle_data(self, data):
        if (MyHTMLParser.getData):
            if not (data.isspace() or not string):
                print("Data     :-", data,"-")

#    def handle_comment(self, data):
#        print("Comment  :", data)

#    def handle_entityref(self, name):
#        c = chr(name2codepoint[name])
#        print("Named ent:", c)

#    def handle_charref(self, name):
#        if name.startswith('x'):
#            c = chr(int(name[1:], 16))
#        else:
#            c = chr(int(name))
#        print("Num ent  :", c)

#    def handle_decl(self, data):
#        print("Decl     :", data)

        
url = "https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt"
file = urllib.request.urlopen(url)

#data = file.read().replace('\n', '')
data = ''
for line in file:
    decoded_line = line.decode("utf-8")
    data += decoded_line.replace('\n', '')

parser = MyHTMLParser()
parser.feed(data)


# In[72]:


#Assignment 4 - Prob 1
#Using reduce functions: PTS:100
#add only even numbers in a list
import functools
numList = [1,2,3,4,5,6,8]
functools.reduce (lambda a,b: a + b if ((a % 2 == 0) and (b % 2 == 0))                   else ( a if a % 2 == 0 else (b if b % 2 == 0 else 0)),                  numList)


# In[81]:


#Assignment 4 - Prob 2
#Using reduce functions:
#find the biggest character in a string (printable ascii characters)
import functools
t_str = 'Avgtgh'
functools.reduce (lambda a,b : a if (ord(a) < 32 and ord(b) < 32 and                                      ord(a) > 127 and ord(b) > 127)                                  else ( a if (ord(a) > ord (b)) else b),                                    t_str) 


# In[158]:


#Assignment 4 - Prob 3
#Using reduce functions 
#adds every 3rd number in a list
import functools
numList = [1,2,3,4,5,6,8,9,10]

#ranked_users = ['jon','bob','jane','alice','chris']
#user_details = [ranked_users.index(x) for x in ranked_users]
#print (user_details)
functools.reduce (lambda a, b : a+b , list (map (lambda x : x[1] if x[0] else 0,                                                 list(zip(                     list(map(lambda x : (x[0]+1) % 3 == 0, enumerate(numList))),                                                           numList)))) )  


# In[189]:


#Assignment 5
#Using randint, random.choice and list comprehensions, write an 
#expression that generates 15 random KADDAADDDD number plates, 
#where KA is fixed, D stands for a digit, and A stands for Capital 
#alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 PTS:100

import random

[''.join(['KA',str(random.randint(11,98)),                      random.choice(string.ascii_uppercase ),                         random.choice(string.ascii_uppercase),                     str(random.randint(1001,9998))]) for i in range(15)]


# In[190]:


#Assignment 6
#Write the above again from scratch where KA can be changed to DL, 
#and 1000/9999 ranges can be provided.

import random

def numPlate (st_code, num_range):
    return [''.join([st_code,str(random.randint(11,98)),                      random.choice(string.ascii_uppercase ),                         random.choice(string.ascii_uppercase),                     str(random.randint(num_range[0]+1,num_range[1]-1))]) for i in range(15)]

numPlate('DL', (1015,8000))
