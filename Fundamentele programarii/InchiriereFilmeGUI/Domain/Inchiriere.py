'''
Created on 25 nov. 2016

@author: Alin
'''
from datetime import date
from Domain.IDObject import IDObject

class inchiriere(IDObject):
    def __init__(self, id_inchiriere,id_film,id_custumer,data_inchirierii,data_returnarii):
        super().__init__(id_inchiriere)
        self.__id_film=id_film
        self.__id_custumer=id_custumer
        self.__data_inchirierii=date(*map(int,data_inchirierii.split("/")))
        self.__data_returnarii=date(*map(int,data_returnarii.split("/")))
    
    def getIdFilm(self):
        return self.__id_film
     
    def getIdCustumer(self):
        return self.__id_custumer
    
    def getDataInchirierii(self):
        return self.__data_inchirierii
    
    def getDataReturnarii(self):
        return self.__data_returnarii
    
    def setIdFilm(self,idf):
        self.__id_film = idf
     
    def setIdCustumer(self,idc):
        self.__id_custumer = idc
    
    def setDataInchirierii(self,di):
        self.__data_inchirierii = di
    
    def setDataReturnarii(self,dr):
        self.__data_returnarii = dr
        
    def __str__(self):
        return "{};{};{};{}/{}/{};{}/{}/{}".format(
            self.getId(),
            self.getIdFilm(),
            self.getIdCustumer(),
            self.getDataInchirierii().year,
            self.getDataInchirierii().month,
            self.getDataInchirierii().day,
            self.getDataReturnarii().year,
            self.getDataReturnarii().month,
            self.getDataReturnarii().day)
        