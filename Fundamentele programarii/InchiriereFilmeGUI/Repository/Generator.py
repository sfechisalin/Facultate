'''
Created on 11 dec. 2016

@author: Alin
'''
import random
from datetime import date
#from Repository.inmemory import repositoryClient,repositoryInchiriere,repositoryMovie
from Domain.Client import client
from Domain.Film import movie
from Domain.Inchiriere import inchiriere


class Generator():
    def __init__(self,client_repo,movie_repo,rental_repo):
        self.__client_repo=client_repo
        self.__movie_repo=movie_repo
        self.__renal_repo=rental_repo
    
    def initializare(self,number):
        self.initialize_client_repo(number)
        self.initalize_movie_repo(number)
        self.initialize_rental_repo(number)
    
    def initalize_movie_repo(self,number):
        
        title=["Lord of the Rings: The Fellowship of the Ring","Lord of the Rings: The Two Towers","The Expendables",
               "The Expendables 2","The Expendables 3","Fast and Furious 6","Inception","Fight Club"]
        description=["good","bad","ok","Special"]
        gender=["trailer","comedy","drama","documentary"]
        for i in range(1,number):
            fm=movie(i,title[random.randint(1,len(title)-1)],description[random.randint(1,len(description)-1)],gender[random.randint(1,len(gender)-1)])
            self.__movie_repo.addMovie(fm)

    def initialize_client_repo(self,number):
        
        nume=["Alin","Nichita","Andrei","Florin","Flavius"]
        cnp=["1982341415413","1241567725151","120816544817661","241454132211","14511241221","213145513452"]
        for i in range(1,number):
            Cl=client(i,nume[random.randint(1,len(nume)-1)],cnp[random.randint(1,len(cnp)-1)])
            self.__client_repo.addCustumer(Cl)
            
    def initialize_rental_repo(self,number):
        
        for i in range(1,number):
            idFilm=random.randint(1,number-1)
            idCustumer=random.randint(1,number-1)
            data_inchirierii=date(random.randint(1997,2018),random.randint(1,12),random.randint(1,31))
            data_returnarii=date(random.randint(1997,2018),random.randint(1,12),random.randint(1,31))
            rent=inchiriere(i,idFilm,idCustumer,data_inchirierii,data_returnarii)
            self.__renal_repo.add_inchiriere(rent)
            
            
            