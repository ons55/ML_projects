# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 00:59:49 2019

@author: ADMIN
"""

class Lawn:
     def __init__(self,length=5,width=5):
        self.length=length
        self.width=width
        
L=Lawn(5,5)

class Mower:
    def __init__(self,x,y,o):
        self.x=x
        self.y=y
        self.o=o
 
    def deplacer(self,p):
        liste=["N","E","S","W"]
        c=liste.index(self.o)
        if p=='R'and c < 3:
            self.o=liste[c+1]
        elif p=='R' and c==3:
            self.o=liste[0]
        elif p=='L':
            self.o=liste[c-1]
        elif p=='F' and self.o=='N' and self.y < L.length:
            self.y=self.y+1
        elif p=='F' and self.o=='W' and self.x > 0:
            self.x=self.x-1
        elif p=='F' and self.o=='E' and self.x < L.width:
            self.x=self.x+1
        elif p=='F' and self.o=='S' and self.y> 0:
            self.y=self.y-1
    
    
            

L=Lawn(5,5)
M1=Mower(1,2,'N')    
M1.deplacer('L') 
M1.deplacer('F') 
M1.deplacer('L')   
M1.deplacer('F')   
M1.deplacer('L')   
M1.deplacer('F') 
M1.deplacer('L') 
M1.deplacer('F') 
M1.deplacer('F') 
print('the result of the first mower is ',M1.x,M1.y,M1.o)

M2=Mower(3,3,'E')    
M2.deplacer('F') 
M2.deplacer('F') 
M2.deplacer('R')   
M2.deplacer('F')   
M2.deplacer('F')   
M2.deplacer('R') 
M2.deplacer('F') 
M2.deplacer('R') 
M2.deplacer('R') 
M2.deplacer('F') 
print('the result of the second mower is ',M2.x,M2.y,M2.o)
        
        