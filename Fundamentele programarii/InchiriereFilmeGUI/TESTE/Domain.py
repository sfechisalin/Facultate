
from Domain.Client import client
from Domain.Film import movie
from Domain.Inchiriere import inchiriere
from datetime import date

import unittest
class TestClient(unittest.TestCase):
    def setUp(self):
        self.dom = client(1,"Alin","19700000000")

    def testCreate(self):
        self.assertTrue(self.dom.getId() == 1)
        self.assertTrue(self.dom.getName() == "Alin")
        self.assertTrue(self.dom.getCnp() == "19700000000")
        self.assertTrue(self.dom == client(1,"Sfechis","123"))
        self.assertTrue(self.dom < client(1,"Sfechis","123"))

class TestMovie(unittest.TestCase):
    def setUp(self):
        self.mov= movie(1,"Abduction","Ok","Actiune")
        
    def testCreate(self):
        self.assertTrue(self.mov.getId() == 1)
        self.assertTrue(self.mov.getTitle() == "Abduction")
        self.assertTrue(self.mov.getDescription() == "Ok")
        self.assertTrue(self.mov.getGender() == "Actiune")
        self.assertTrue(self.mov == movie(1,"Alt_film","rau","Alt_ceva"))

class TestImchiriere(unittest.TestCase):
    def setUp(self):
        self.inc= inchiriere(1,1,1,"1997/01/02","2017/3/4")
    
    def testCreate(self):
        self.assertTrue(self.inc.getId() == 1)
        self.assertTrue(self.inc.getIdCustumer() == 1)
        self.assertTrue(self.inc.getIdFilm() == 1)
        self.assertTrue(self.inc.getDataInchirierii() == date(1997,1,2))
        self.assertTrue(self.inc.getDataReturnarii() == date(2017,3,4))
        
