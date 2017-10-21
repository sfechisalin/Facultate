'''
Created on 5 dec. 2016

@author: Alin
'''
from Repository.FileRepo import RepoException
from Domain.Inchiriere import inchiriere
class controllerRental:
    def __init__(self,repo_movie,repo_client,repo_rental,val):
        '''
        Creeaza un controller pentru un repository.
        
        + repository : store list
        + validator : validator class
        '''
        self.__repo_movie=repo_movie
        self.__repo_client=repo_client
        self.__repo_rental=repo_rental
        self.__val=val
    
    
    def adauga_inchiriere(self,id_inchiriere,id_film,id_custumer,data_inchirierii,data_returnarii):
        '''
        Adauga o inchiriere in repository-ul de inchirieri
        +id_inchiriere= id-ul la care se face inchirierea
         id_film= id-ul filmului pe care il inchiriem
         id_custumer=id-ul clientului care inchiriaza filmul
         data_inchirierii=data la care se face inchirierea
         data_returnarii=data pana la care trebuie returnat filmul 
        '''
        inc1=inchiriere(id_inchiriere,id_film,id_custumer,data_inchirierii,data_returnarii)
        print(inc1)
        print("\n")
        print("Mergem la Validare \n")
        self.__val.valideaza(inc1)
        print("Am iesit din Validare \n")
        self.__repo_rental.add(inc1)
        
        
    def returnare_inchiriere(self,ID):
        '''
            Returneaza inchirierea cu id-ul ID
        '''
        return self.__repo_rental.delete_by_id(ID)
        
    def returnare_inchiriere_client(self,ID):
        '''
            Returneaza inchirierea a carui client are ID-ul ID
        '''
        return self.__repo_rental.delete_by_id_client(ID)
    
    def returnare_inchiriere_film(self,ID):
        '''
        Returneaza inchirierea a carui film are id-ul ID 
        '''
        return self.__repo_rental.delete_by_id_film(ID)
           
    def clientiRentalRepository(self):
        '''
        Returneaza o lista cu toti clientii care au inchiriat filme
        '''
        
        lista=[]
        lista_existente=[]
        for obj in self.__repo_rental.getAll():
            ob=self.__repo_client.getById(obj.getIdCustumer())
            if ob.getName() not in lista_existente:
                lista.append(self.__repo_client.getById(obj.getIdCustumer()))
                lista_existente.append(ob.getName())

        return lista
    
    
    def listaClientiFilmeInchiriateOrd(self):
        '''
        Returneaza o lista cu toti clientii care au inchiriat filme,sortati
        '''
        all_clienti=self.clientiRentalRepository()
        all_clienti.sort()
        
        return all_clienti 
    
    
    def filmeInchiriateId(self,ID):
        '''
        Returneaza numarul de filme inchiriate de clientul cu id-ul ID
        '''
        return len([obj for obj in self.__repo_rental.getAll() if int(obj.getIdCustumer()) == int(ID)])
        #return len([obj for obj in self.__repo_rental.getAll() if int(obj.getIdFilm()) == int(ID)])
    
    def filmeIdClienti(self):
        '''
        Returneaza o lista de tuple-uri in care primul camp este numele clientului
        iar al doilea camp este numarul de filme inchiriate de acest client
        '''
        list_to_return=[]
        for obj in self.__repo_client.getAll():
            list_to_return.append((obj.getName(),self.filmeInchiriateId(obj.getId())))
            
        return list_to_return
        
        
    def listaClientiNumarFilmeInchiriateOrd(self):
        '''
        Returneaza o lista(de tuple-uri) a clientilor sortata dupa numarul de filme inchiriate
        '''
        lista=self.filmeIdClienti()
        lista.sort(key = lambda x:x[1] , reverse=True)
        return lista
    
    
    def numarInchirieriFilmID(self,ID):
        '''
        Returneaza numarul de inchirieri al filmului cu id-ul ID
        +ID=id-ul filmului caruria dorim sa-i aflam numarul de inchirieri
        '''
        answ = 0
        for obj in self.__repo_rental.getAll():
            if obj.getId() == ID:
                answ = answ + 1
        return answ
    
    
    def celeMaiInchiriateFilme(self):
        '''
            Returneaza o lista cu cele mai inchiriate filme
        '''
        lista=[]
        maxim = 0 
        for film in self.__repo_movie.getAll():
            actual = self.numarInchirieriFilmID(film.getId())
            if actual > maxim:
                maxim = actual 
                lista=[]
                lista.append(film)
            else:
                if actual == maxim:
                    lista.append(film)
        return lista
    
    def returneazaDataOrEroare(self,stringData):
        '''
            Returneaza data in formatul de data,in cazul in care data este corecta
            sau eroare ,altfel
        '''
        return self._val.valideaza_data(stringData)
    
    
    def treiZeciLaSutaClienti(self):
        '''
        Returneaza o lista(de forma client,numar_filme_inchiriate)
         cu primii 30% clienti cu cele mai multe filme inchiriate
        '''
        cat = (30*self.__repo_client.sizeRepoCustumer())//100
        lista=self.filmeIdClienti()
        lista=lista[:-cat]
        return lista
    
    
    def existaIdFilm(self,ID):
        '''
        Returneaza True daca exista id-ul ID in lista de filme,
        ridica o eroare in caz contrar
        '''
        for mov in self.__repo_movie.getAll():
            if int(mov.getId()) == int(ID):
                return True
            
        raise RepoException("Nu exista id-ul {} in lista de filme \n".format(ID))
    
    
    def existaIdClient(self,ID):
        '''
        Returneaza True daca exista id-ul ID in lista de clienti,
        ridica o eroare in caz contrar
        '''
        for custumer in self.__repo_client.getAll():
            if int(custumer.getId()) == int(ID):
                return True
            
        raise RepoException("Nu exista id-ul {} in lista de clientii \n".format(ID))
    
    def InchiriereID(self,ID):
        '''
        Returneaza inchirierea cu id-ul ID ,in cazul in care aceasta exista,
        lanseaza o eroare altfel
        '''
        for rental in self.__repo_rental.getAll():
            if int(rental.getId()) == int(ID):
                return rental
        raise RepoException("Nu exista nici o inchiriere cu id-ul {} ".format(ID))
                
    def getAllRentals(self):
        '''
        Returneaza o lista cu toate inchirieriile
        '''
        return self.__repo_rental.getAll()
    def size(self):
        return len(self.__repo_rental.getAllInchirieri())