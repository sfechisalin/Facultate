from Repository.inmemory import repositoryClient,repositoryMovie,repositoryInchiriere,RepoExceptionFromMemory
#from Repository.FileRepo import UniversalFileRepo,ClientFileRepo, RepoException

from Domain.Client import client
from Domain.Film import movie
from Domain.Inchiriere import inchiriere
import unittest


class TestRepoClient(unittest.TestCase):
    def setUp(self):
        self.repo=repositoryClient()
        self.repo.add(client(1,"Alin","19723060056"))

    def testCreate(self):
        self.assertTrue(self.repo.size() == 1)
        self.assertRaises(RepoExceptionFromMemory,self.repo.add,client(1,"Darius","123"))
        
    def testDelete(self): 
        self.assertTrue(self.repo.getById(1) == client(1,"Alin","19723060056"))
        self.repo.add(client(2,"Sfechis","19723060056"))
        self.assertTrue(self.repo.size() == 2)
        self.repo.delete_by_id(2)
        self.assertTrue(self.repo.size() == 1)
        
    def testUpdate(self):
        self.repo.modify_by_id(client(1,"alin_catalin","12345"))
        self.assertTrue(self.repo.getById(1) == client(1,"alin_catalin","12345"))
                               
class testRepositoryMovie(unittest.TestCase):
    def setUp(self):
        self.repo =  repositoryMovie()
        self.repo.add(movie(1,"Abduction","ok","Actiune"))
        
    def testCreate(self):
        self.assertTrue(self.repo.size() == 1)
        self.assertRaises(RepoExceptionFromMemory,self.repo.add,movie(1,"ALtceva","ok","OK"))
        
    def testDelete(self):
        self.assertTrue(self.repo.getById(1) == movie(1,"Abduction","ok","Actiune"))
        element = self.repo.delete_by_id(1)
        self.assertTrue(self.repo.size() == 0)
        self.assertTrue(element.getId() == 1 and element.getTitle() == "Abduction" and element.getDescription() == "ok"
                        and element.getGender() == "Actiune")
    
    def testUpdate(self):
        self.assertTrue(self.repo.size() == 1)
        self.assertRaises(RepoExceptionFromMemory,self.repo.modify_by_id,movie(4,"Home Alone ","ok","Comedie"))
        mov = self.repo.modify_by_id(movie(1,"Home Alone","ok","Comedie"))
        self.assertTrue(mov.getId() == 1 and mov.getTitle() == "Home Alone" and mov.getDescription() == "ok" and
                        mov.getGender() == "Comedie")

class testInchiriere(unittest.TestCase):
    def setUp(self):
        self.inc = repositoryInchiriere()
        self.inc.add(inchiriere(1,1,1,"1997/2/3","2017/1/1"))
    
    def testCreate(self):
        self.assertTrue(self.inc.size() == 1)
    
    def testDelete(self):
        self.inc.delete_by_id(1)
        self.assertTrue(self.inc.size() == 0)
        
# class testUniversalFileRepo(unittest.TestCase):
#     def setUp(self):
#         self.repo=UniversalFileRepo("filme.txt",movie)
#         #print(*self.repo.getAll())
#         self.repo.add(movie(17,"Ab","o","A"))
#         
#     def testCreate(self):
#         self.assertTrue(self.repo.size() is not  0)
#         self.assertRaises(RepoException,self.repo.add, movie(17,"Altceva","ok","ok"))
#     
#     
#     def testDelete(self):
#         lg = self.repo.size()
#         self.repo.delete_by_id(0)
#         self.assertTrue(self.repo.size() == (lg-1) )