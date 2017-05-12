
# coding: utf-8

# In[36]:

import pandas as pd
import os
import sys


# In[37]:

palabra = ['SELECT',
 'emp.ename',
 'FROM',
 'emp,',
 'asg,',
 'proj',
 'WHERE',
 'emp.eno=asg.eno',
 'AND',
 'asg.pno=proj.pno',
 'AND',
 "proj.pname='cad/cam'"]


# In[38]:

def imprimir(pila):
    temp = pila
    while not temp.isEmpty():
        print temp.pop()


# In[39]:

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila esta vacia levanta excepción"""
        try:
         return self.items.pop()
        except IndexError:
            raise ValueError("LA PILA ESTA VACIA")
     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     
    


# In[40]:

def consulta(elementos):
    resultado = None
    p = Stack()
    m = Stack()
    for elemento in elementos:
        if elemento not in ["SELECT","FROM","WHERE","AND"]:
            p.push(elemento)
        elif elemento  in ["SELECT","FROM","WHERE","AND"]:
            next
    return p
       
        


# In[113]:

pila = consulta(palabra)


# In[114]:

contador = 0
#while contador < 3:
A = pila.pop().split(".")
print A
(campo,valor) = A[1].split("=")

proj=pd.read_csv(A[0]+'.csv',index_col='pno')
jvar= proj[proj[campo].str.contains(valor)]


# In[115]:

llave = jvar.index.values[0]


# In[116]:

contador = 0
#while contador < 3:
B = pila.pop().split(".")
print B

(campo,valor) = B[1].split("=")
print campo,valor
asg=pd.read_csv(B[0]+'.csv',index_col='eno')
asg



# In[117]:

print campo,valor
gvar = asg[asg[campo].str.contains(llave)]
gvar


# In[130]:

keys = gvar.index.values
keys


# In[131]:

emp=pd.read_csv('emp.csv',delimiter=',')


# In[132]:

for i in keys:
    a = emp.loc[emp['eno'] == i]
    print "Select ename from emp where eno=",i
    print a
    


# In[126]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



