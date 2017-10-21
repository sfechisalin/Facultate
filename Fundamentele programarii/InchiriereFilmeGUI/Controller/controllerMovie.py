'''
Created on 25 nov. 2016

@author: Alin
'''
from Domain.Film import movie
class controllerMovie:
    def __init__(self,repo,val):
        self.__repo=repo
        self.__val=val
        
   
    def addMovie(self,ID,TITLU,DESCRIERE,GENDER):
        '''
        Adauga un nou film,in lista de filme
        '''
        new_movie=movie(ID,TITLU,DESCRIERE,GENDER)
        self.__val.valideaza(new_movie)
        self.__repo.add(new_movie)
    
    
    def deleteMovie(self,idMovie):
        '''
        Sterge un film dupa un id
        '''
        return self.__repo.delete_by_id(idMovie)
    

    def updateMovie(self,ID,TITLU,DESCRIERE,GENDER):
        '''
        Actualizeaza informatile unui film
        '''
        new_movie=movie(ID,TITLU,DESCRIERE,GENDER)
        self.__val.valideaza(new_movie)
        return self.__repo.modify_by_id(new_movie) 
    
    
    def search_movie(self,keyword):
        '''
        Returneaza toate filmele cu proprietatea keyword
        '''
        lista_filme={}
        for mov in self.__repo.getAllMovies():
            if mov.getId()==keyword or mov.getTitle()==keyword or mov.getDescription()==keyword or mov.getGender()==keyword:
                lista_filme[mov.getId()]=mov
        print(lista_filme.values())
        return lista_filme
    
    
    def getAllMovies(self):
        '''
        Returneaza o lista cu toate filmele
        '''
        return self.__repo.getAll()
    
    def size(self):
        '''
        Returneaza dimensiunea depozitului de filme
        '''
        return self.__repo.size()