'''
Created on 23 nov. 2016

@author: Alin
'''
from Domain.Client import client
from Domain.Validators import clientValidator,MyError
from Repository.inmemory import repositoryClient

class controlerCustumer:
    def __init__(self,repo,val):
        self.__repo=repo
        self.__val=val
        

    def add(self,id,nume,cnp):
        '''Adauga un nou Client in lista de clienti
        input:
        -id=id-ul clientului
        -nume=numele clientului
        -cnp=cnp-ul clientului
        '''
        custumer=client(id,nume,cnp)
        # valideaza clientul pe care dorim sa-l adaugam in lista
        self.__val.valideaza(custumer)
        #se adauga in lista in cazaul in care clientul indeplineste toate cerintele
        self.__repo.add(custumer)
        #return custumer ,pentru teste 
        
    def search(self,keyword):
        '''Cauta in lista de clienti,clientii care au o anumita proprietate
        input:
        -keyword=proprietate
        output:
        -lista de clienti(sub forma unui dictionar) care indeplinesc aceasta proprietate
        '''
        dict_clienti={}
        for custumer in self.__repo.getAll():
            if custumer.getId()==keyword or custumer.getName()==keyword or custumer.getCnp()==keyword:
                dict_clienti[custumer.getId]=custumer
        return dict_clienti
   
    def removeCustumer(self,idCustumer):
        '''
        Sterge un client dupa id
        '''
        return self.__repo.delete_by_id(idCustumer)
  
    def updateCustumer(self,ID,NUME,CNP):
        '''
        Modifica cliendul dupa un id
        '''
        new_custumer=client(ID,NUME,CNP)
        self.__val.valideaza(new_custumer)
        self.__repo.modify_by_id(new_custumer)
    
    def getAllCustumers(self):
        '''Returneaza toti clientii'''
        return self.__repo.getAll()
    
    def size(self):
        return len(self.__repo.getAll())
    