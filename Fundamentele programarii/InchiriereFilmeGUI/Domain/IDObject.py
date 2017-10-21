'''
Created on 25 nov. 2016

@author: Alin
'''

class IDObject:
    def __init__(self, id_initial):
        '''
        Constructor
        '''
        self.__id=id_initial
        
    def getId(self):
        '''
        Returneaza id-ul unui client
        '''
        return self.__id

def test_ID():
    id1=IDObject(1)
    assert id1.getId()==1
    id2=IDObject(5)
    assert id2.getId()==5
test_ID()