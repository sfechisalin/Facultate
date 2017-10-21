'''
Created on 19 nov. 2016

@author: Alin
'''
from Domain.Client import client
from Domain.Film import movie
from Domain.Inchiriere import inchiriere
from datetime import date

class MyError(Exception):
    def __init__(self,er):
        self.eroare=er
    def getEroare(self):
        return self.eroare
#     def __repr__(self):
#         return str(*self.eroare)
    def __str__(self):
        return str(self.eroare)
    
    
class clientValidator:
    def verificare_string(self,string):
        '''
        Verifica daca obiect contine doar caractere
        Returneaza True in caz favorabil si False,altfel
        '''
        for litera in string:
            if litera != ' ' and litera.isalpha()==False:
                return False
        return True
    
    
    def valideaza(self,custumer):
        errors=[]
        try:
            cID=int(custumer.getId())
        except ValueError:
            errors.append("Id-ul trebuie sa fie convertibil la tipul int\n")
        if custumer.getName()=="":errors.append("Numele nu poate fi vid\n")
        if self.verificare_string(custumer.getName())==False:
            errors.append("Numele clientului trebuie sa fie un sir de caracatere\n")
        try:
            cCnp=int(custumer.getCnp())
        except ValueError:
            errors.append("Cnp-ul trebuie sa fie convertibil la tipul int\n")
        if len(errors)>0:
            raise MyError(errors)# aici am instantant obiectul MyError(errors),self=MyError(errors)


class movieValidator:
    def verificare_string(self,string):
        '''
        Verifica daca obiect contine doar caractere
        Returneaza True in caz favorabil si False,altfel
        '''
        for litera in string:
            if litera != ' ' and litera.isalpha()==False:
                return False
        return True
    
    
    def valideaza(self,FILM):
        errors=[]
        try:
            IDFILM=int(FILM.getId())
        except:
            errors.append("Id-ul filmului trebuie sa fie convertibil la tipul int")
        if self.verificare_string(FILM.getTitle())==False:
            errors.append("Titlul filmului trebuie sa fie un sir de caracatere")
        if self.verificare_string(FILM.getDescription())==False:
            errors.append("Descrierea filmului trebuie sa fie un sir de caracatere")
        if self.verificare_string(FILM.getGender())==False:
            errors.append("Genul filmului trebuie sa fie un sir de caracatere")
        if len(errors)>0:
            raise MyError(errors)


class inchirieriValidator:
    def valideaza(self,INCHIRIERE):
        errors=[]
        try:
            idInchiriere=int(INCHIRIERE.getId())
        except:
            errors.append("ID-ul inchirierii trebuie sa fie convertibil la int \n")
        try:
            idFilm=int(INCHIRIERE.getIdFilm())
        except:
            errors.append("ID-ul filmuylui trebuie sa fie convertibil la int \n")
            
        try:
            idCustumer=int(INCHIRIERE.getIdCustumer())
        except:
            errors.append("ID-ul clientului trebuie sa fie convertibil la int \n")
        
        if type(INCHIRIERE.getDataInchirierii()) is not date :
            errors.append("Data inchirierii trebuie sa fie de tipul date \n")
        
        if type(INCHIRIERE.getDataReturnarii()) is not date :
            errors.append("Data returnarii trebuie sa fie de tipul date \n")
        
        if len(errors) > 0:
            raise MyError(errors)
def testMovieValidator():
    validatorMovie=movieValidator()
    m1=movie("10","Home Alone","OK","Comedy")
    try:
        validatorMovie.valideaza(m1)
        assert True
    except:
        assert False 
       
    m2=movie("qsa","Home Alone","OK","Comedy")
    try:
        validatorMovie.valideaza(m2) 
        assert False
    except MyError as me:
        assert len(me.getEroare())==1



def testClient():
    c1=client("1","Alin","197072306007")
    validator=clientValidator()
    try:
        validator.valideaza(c1)
        assert True
    except:
        assert False
    c2=client("asa","Alin","1921020101")
    try:
        validator.valideaza(c2)
        assert False
    except MyError as me:
        assert len(me.getEroare())==1
        
# def testInchiriere():
#     i1=inchiriere(1,1,1,date(2016,12,5),date(2017,1,10))
#     i2=inchiriere(1,1,1,date(2016,12,5),"NU ASA")
#     validator=inchirieriValidator()
#     try:
#         validator.valideaza(i1)
#         assert True
#     except:
#         assert False
#    
#     try:
#         validator.valideaza(i2)
#         assert False
#     except MyError as me:
#         assert len(me.getEroare())==1
     
testClient()
testMovieValidator()
#testInchiriere()