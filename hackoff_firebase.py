# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 22:02:13 2019

@author: sarav
"""
import time
from firebase import firebase  




firebase = firebase.FirebaseApplication('https://hackoff-ef274.firebaseio.com/', None)  





f = open("C:\\Users\\sarav\\Desktop\\sample.txt", "r")
content = f.read()
while( len(content) < 2 or content[-1]!='!'):
    time.sleep(2)
    f = open("C:\\Users\\sarav\\Desktop\\sample.txt", "r")
    content = f.read()
    


if content[-1]=='!':
    



    #content=content[:-1]
    
    ind=content.rfind("//");
    content=content[ind+2:]
    content=content.split('|')
    for i in range(len(content)):
        content[i]=content[i].split()
        
    for i in content:
        print(i)    
    
    for i in range(9):
        data={'r':content[i][0] , 'c':content[i][1], 'e':content[i][2]}
        path="/levels/l"+str(i+1)+"/"
        firebase.put('',path,data)      