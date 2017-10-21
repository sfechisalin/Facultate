from Repository.inmemory import repositoryClient
from Domain.Client import client


class RepoException(Exception):
    def __init__(self,ex):
        self.__eroare=ex
        
    def __str__(self):
        return str(self.__eroare)
    
    
class UniversalFileRepo:
    '''
    Store/retrive movies from file
    '''
    def __init__(self,fName,stored_type):
        self.__filename=fName
        self.__stored_type=stored_type
        try:
            open(self.__filename,"r")
        except IOError:
            open(self.__filename,"w")
        self.__load_from_file()
    
    def __load_from_file(self):
        '''
        Read movies from file and return a list with movies
        '''
        list_to_return=[]
        with open(self.__filename,"r") as f:
            for line in f:
                line = line.strip()
                if line=="":
                    continue
                elements=line.split(";")
                entity=self.__stored_type(*elements)
                list_to_return.append(entity)
                
        return list_to_return
    
    def __store_to_file(self,lista):
        '''
        Printeaza o lista in fisier
        '''
        with open(self.__filename,"w") as f:
            for obj in lista:
                    f.write(str(obj)+"\n")
                
    def getById(self,ID):
        '''
        Returneaza True,daca filmul cu id-ul "ID" se afla in fisie,False,in caz contrar
        '''
        lista=self.__load_from_file()
        for obj in lista:
            if int(obj.getId()) == ID:
                return True
        
        return False
    
    def add(self,entity):
        '''
        Adauga un film in fisier
        '''
        if self.getById(entity.getId()) is not False:
            raise RepoException("Id-ul nu este unic") 
        
        
        lista=self.__load_from_file()
        lista.append(entity)
        self.__store_to_file(lista)
    
    def size(self):
        '''
        Returneaza numarul de obiecte din fisier
        '''
        return len(self.__load_from_file())
        
        
    def delete_by_id(self,ID):
        '''
        Sterge un obiect dupa id
        '''
        obj = None
        lista=self.__load_from_file()
        # for i,el in enumerate(lista):
        #     if int(el.getId()) == int(ID):
        #         obj = lista [ i ]
        #         del lista[i]
        #         break
        def stergere(poz,ID):
            if poz < len(lista):
                if int(lista[poz].getId()) == int(ID):
                    obj = lista[poz]
                    del lista[poz]
                    return#
                stergere(poz+1,ID)
        stergere(0,ID)
        self.__store_to_file(lista)
        return obj 
    
    def delete_by_id_client(self,ID):
        '''
        Sterge un obiect dupa id
        '''
        lista=self.__load_from_file()
        for i,el in enumerate(lista):
            if int(el.getIdCustumer()) == int(ID):
                del lista[i]
                break
        self.__store_to_file(lista)    
        
    def getByIdFilm(self,ID):
        '''
        Sterge un obiect dupa id
        '''
        lista=self.__load_from_file()
        for i,el in enumerate(lista):
            if int(el.getIdFilm()) == int(ID):
                del lista[i]
                break
        self.__store_to_file(lista)
        
        
    def modify_by_id(self,obj):
        self.delete_by_id(obj.getId())
        lista=self.__load_from_file()
        lista.append(obj)
        self.__store_to_file(lista)
        return obj 
        
    def getAll(self):
        '''
        Returneaza o lista cu toate obiectele din fisier
        '''
        return self.__load_from_file()    
         
class ClientFileRepo(repositoryClient):
    """
    Store/retrieve custumers from file
    """
    def __init__(self,fileN):
        repositoryClient.__init__(self)
        self.__fName=fileN
        self.__load_from_file()
         
    def __load_from_file(self):
        '''
        Load custumers from file
        Return CorruptedFileException if there is an error when reading from file
        '''
        try:
            f=open(self.__fName,"r")
        except IOError:
            return 
        line = f.readline().strip()
        #rez=[]
        while line!="":
            atribute=line.split(";")
            cl=client(atribute[0],atribute[1],atribute[2])
            repositoryClient.add(self, cl)
        #   rez.append(cl)
            line = f.readline().strip()
        # return rez
        f.close()
 
     
    def getByIdCustumer(self,ID):
        lista=self.getAll()
        for obj in lista:
            if int(obj.getId()) == int(ID):
                return obj
        
        return None
     
    def add(self,cl):
        '''
        Salveaza un client,la sfarsitul fisierului
        Returneaza RepositoryClientException in cazul in care acesta se afla in fisier
        '''
        repositoryClient.add(self, cl)
        self.__store_to_file()
     
         
    def modify_by_id(self,Object):
        '''
            Modifica numele si cnp-ul unui client dupa id-ul sau
            Lanseaza ValueError in cazul in care acesta nu se afla in lista
        '''
        repositoryClient.modify_by_id(self,Object)
        self.__store_to_file()
         
    def delete_by_id(self,ID):
        '''
        Sterge un client din fisier.
        Returneaza RepositoryClientException in cazul in care acesta nu se afla in fisier
        '''
        custumer=repositoryClient.delete_by_id(self, ID)
        self.__store_to_file()
        return custumer
     
         
    def __store_to_file(self):
        f=open(self.__fName,"w")
        custumers=repositoryClient.getAll(self)
        for custumer in custumers:
            clientii='{};{};{}\n'.format(custumer.getId(),custumer.getName(),custumer.getCnp())
            f.write(clientii)
        f.close()
     
    def size(self):
        '''
        Returneaza dimensiunea depozitului de clienti
        '''
        return len(self.__load_from_file())
     
# def testClientFileRepo():
#     filename="clienti.txt"
#     fileRepoCustumers=ClientFileRepo(filename)
#     cl = client(1,"Alin","123")
#     
#     fileRepoCustumers.addCustumer(cl)
#     assert fileRepoCustumers.size()==1
#     assert fileRepoCustumers.deleteByIdCustumer(1)==cl
#     
#testClientFileRepo()
