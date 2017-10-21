'''
Created on 19 nov. 2016

@author: Alin
'''
from Domain.IDObject import IDObject
class client(IDObject):
    def __init__(self,ID,name,cnp):
        IDObject.__init__(self, ID)
        self.__name=name
        self.__cnp=cnp
        
    def setName(self,name):
        self.__name=name
    
    def getName(self):
        return self.__name
    
    def getCnp(self):
        return self.__cnp
    
    def setCnp(self,cnp):
        self.__cnp=cnp
    
    def __eq__(self,cl):
        '''
        verify equality
        cl-client
        return true if current client equals with cl 
        '''
        return isinstance(cl,client) and self.getId()==cl.getId()
    
    def __lt__(self,cl):
        '''
        Verificare sortare dupa nume
        '''
        return isinstance(cl, client) and self.getName()<cl.getName()
     
         
    def __str__(self):
        return "Client : ID :{} , Nume : {} , Cnp : {}".format(
                    self.getId(),
                    self.getName(),
                    self.getCnp())