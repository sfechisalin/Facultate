'''
Created on 19 nov. 2016

@author: Alin
'''
from Domain.IDObject import IDObject

class movie(IDObject):
    def __init__(self,ID,title,description,gender):
        IDObject.__init__(self,ID)
        self.__title=title
        self.__description=description
        self.__gender=gender
        
    #def getId(self):
    #   return self.__id
    def getTitle(self):
        return self.__title
   
    def getDescription(self):
        return self.__description
    
    def getGender(self):
        return self.__gender
    
    def __eq__(self,mov):
        """"
        Verify equality
        mov=movie
        return True if the current movie is equals with mov(have the same id)
        """
        return isinstance(mov,movie) and self.getId()==mov.getId()
    
    def __str__(self):
        return "{};{};{};{}".format(
            self.getId(),
            self.getTitle(),
            self.getDescription(),
            self.getGender())

def testMovie():
    my_movie=movie(1,"Home Alone","Ok","Comedy")
    assert my_movie.getId()==1
    assert my_movie.getTitle()=="Home Alone"
    assert my_movie.getDescription()=="Ok"
    assert my_movie.getGender()=="Comedy"
    compare_movie=movie(1,"Home Alone","Ok","Comedy")
    assert my_movie==compare_movie

testMovie()