'''
Created on 21 nov. 2016

@author: Alin
'''
from Domain.Client import client
from Domain.Film import movie
from Domain.Inchiriere import inchiriere

class RepoExceptionFromMemory(Exception):
    def __init__(self,ex):
        self.__eroare=ex
        
    def __str__(self):
        return str(self.__eroare)
    
class repositoryClient:
    '''
        Functii simple pentru operarea pe lista de clienti
    '''
    
    def __init__(self):
        '''
            Creeaza un depozit gol
        '''
        self.__custumers=[]
    def size(self):
        '''
            Dimensiunea depozitului de clientii
        '''
        return len(self.__custumers)
    '''    self.__index=0
    def __len__(self):
        return len(self.__custumers)
    def __iter__(self):
        return self
    def __next__(self):
        if (self.__index==len(self)):
            self.__index=0
            raise StopIteration
        nxt=self.__custumers[self.__index]
        self.__index+=1
        return nxt
    '''
    def getById(self, id1):
        '''
            Returneaza entitatea cu id dat sau None altfel
            
            + id : int , id-ul disciplinei
            
        '''
        for obj in self.__custumers:
            if int(obj.getId()) == int(id1):
                return obj
        return None
    
    def add(self,custumer):
        '''
        
            Adauga un Client in depozit.
            Lanseaza RepoExceptionFromMemory ,daca exista un client cu acelasi id.
            
            custumer=clientul pe care dorim sa-l adaugam
        '''
        if self.getById(custumer.getId()) is not None:
            raise RepoExceptionFromMemory("ID-ul se afla in lista de clienti")
        
        self.__custumers.append(custumer)
    
    
    def getAll(self):
        '''
        Returneaza o lista cu toti clientii
        '''
        return list(self.__custumers)
    
    def delete_by_id(self,id1):
        '''
        Sterge un obiect din depozit
        Lanseaza KeyError daca nu exista un obiect cu id-ul obiectului ce trebuie sters
        
        id  :int , id-ul disciplinei
        '''
        
        existingObj = self.getById(id1)
        
        if existingObj is None:
            raise RepoExceptionFromMemory("Nu exista obiectul cu acest id")
        
        for i,currentObject in enumerate(self.__custumers):
            if currentObject.getId() == existingObj.getId():
                cl=self.__custumers[i]
                del self.__custumers[i]
                break
            
        return cl    
    
    def modify_by_id(self,Object):
        '''
            Modifica numele unei entitati ce are un id dat.
            Lanseaza RepoExceptionFromMemory in cazul in care nu exista ID-ul
            
            +ObjectToModify=client personalizat 
                Object.getId()=id-ul Clientului a carui nume trebuie modificat
                Object.getName()=Noul nume pe care dorim sa il atribuim clientului
        '''
        if self.getById(Object.getId()) is None:
            raise RepoExceptionFromMemory("ID-ul nu se afla in lista de clienti")
        for obj in self.__custumers:
            if int(obj.getId()) == int(Object.getId()):
                obj.setName(Object.getName())
                obj.setCnp(Object.getCnp())
                break

class repositoryMovie:
    '''
       Functii simple pentru operarea pe lista de filme 
    '''
    def __init__(self):
        '''
            Creeaza un depozit gol
        '''
        self.__collection={}
        
    # 
    def getById(self,ID):
        return self.__collection[ID]
    
    
    def size(self):
        '''
        Dimensiunea depoztitului
        '''
        return len(self.__collection)
    def add(self,mov):
        '''
            Adauga un film nou la lista actuala de filme
            Lanseaza RepoExceptionFromMemory in cazul in care ID-ul filmului mai exista.
            
            mov=filmul pe care dorim sa-l adaugam
        '''
        if mov.getId() in self.__collection:
            raise RepoExceptionFromMemory("ID-ul exista deja in colectia de filme !!! ")

        self.__collection[mov.getId()]=mov
    #
    
    def getAll(self):
        '''
        Returneaza o lista cu toate filmele aflate in depozit
        '''
        return list(self.__collection.values())
    #
    
    def delete_by_id(self,ID):
        '''
            Sterge un Film din colectia de filme,dupa id-ul sau.
            
            Lanseaza RepoExceptionFromMemory in cazul in care ID-ul nu se afla in lista
    
            ID=id-ul
        '''
        ID=int(ID)
        if ID not in self.__collection:
            raise RepoExceptionFromMemory("ID-ul nu se afla in lista!!! ")
        
        el =self.__collection[ID]
        del self.__collection[ID]
        return el
    #
    
    def modify_by_id(self,ObjectToModify):
        '''
            Modifica un film dupa un anumit id
            
            Lanseaza RepoExceptionFromMemory in cazul in care id-ul nu se afla in lista
            
            +ObjectToModify=film personalizat=>
            objectToModify.getId=id-ul filmului la care dorim sa-i schimbam numele
        '''
        ID=int(ObjectToModify.getId())
        if ID not in self.__collection:
            raise RepoExceptionFromMemory("ID-ul nu se afla in lista de filme!!! ")
        del self.__collection[ID]
        self.__collection[ObjectToModify.getId()]=ObjectToModify
        return self.__collection[ObjectToModify.getId()]
        
class repositoryInchiriere:
    def __init__(self):
        self.__storage=[]
        
    def add(self,inc1):
        '''
            Adaugam o noua inchiriere in depozit
          +inc1=inchiriere
        '''# inc1=inchiriere(id_inchiriere,id_film,id_custumer,data_inchiriereii,data_returnarii)
        if self.getById(inc1.getId()):
            raise RepoExceptionFromMemory("ID este ocupat...")
        
        self.__storage.append(inc1)
        
    def delete_by_id(self,ID):
        '''
        Stergem inchirierea din repository
        
        +ID=id-ul inchirierii pe care o stergem
        '''
        
        for ind,el in enumerate(self.__storage):
            if int(el.getId()) == int(ID):
                del self.__storage[ind]
                return el
                break    
        
    def getById(self,ID):
        for ind,el in enumerate(self.__storage):
            if int(el.id_inchiriere)==int(ID):
                return self.__storage[ind]
            
            
    def getAll(self):
        return list(self.__storage)
    
    
    def size(self):
        return len(self.__storage)
            
def testRepositoryMovies():
    repo=repositoryMovie()
    assert repo.size()==0
    film1=movie(1,"Home Alone","Ok","Comedy")
    repo.add(film1)
    assert repo.size()==1
    film2=movie(1,"Abduction","Ok","Trailer")
    try:
        repo.add(film2)
        assert False
    except RepoExceptionFromMemory:
        assert True
    film3=movie(2,"Forrest Gump","OK","Drama")
    repo.add(film3)
    repo.modify_by_id(movie(2,"Good Boys","Bun","Drama"))
    repo.delete_by_id(1)
    assert repo.getById(2) == movie(2,"Good Boys","Bun","Drama")

def testRepositoryClient():
    repo=repositoryClient()
    assert repo.size()==0
    custumer1=client("1","Sfechis Alin","1970723060056")
    repo.add(custumer1)
    assert repo.size()==1
    custumer2=client("1","Sfechis Alina","239101929421")
    try:
        repo.add(custumer2)
        assert False
    except RepoExceptionFromMemory:
        pass
    custumer3=client("2","Savin Catalin","1975894326056")
    repo.add(custumer3)
    assert repo.size()==2
    custumer4=client(1,"Alin","007")
    repo.modify_by_id(custumer4)
    repo.delete_by_id(1)
    assert repo.size()==1    

def testRepositoryInchiriere():
    repo=repositoryInchiriere()
    assert repo.size()==0
    #from datetime import date
    data_inchirierii="2016/12/5"
    data_returnarii="2017/1/10"
    inc1=inchiriere(1,1,1,data_inchirierii,data_returnarii)
    #print(inc1)
    repo.add(inc1)
    assert repo.size()==1
    repo.delete_by_id(1)
    assert repo.size()==0
         
testRepositoryClient()
testRepositoryMovies()
testRepositoryInchiriere()