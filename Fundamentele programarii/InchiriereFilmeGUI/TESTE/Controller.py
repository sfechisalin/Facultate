# import unittest
# 
# 
# from datetime import date
# from Domain.Film import movie
# from Domain.Client import client
# from Domain.Inchiriere import inchiriere
# 
# from Repository.inmemory import repositoryClient,RepoExceptionFromMemory
# from Controller.controllerClient import controlerCustumer
# from Domain.Validators import clientValidator,MyError
# 
# from Repository.inmemory import repositoryInchiriere,RepoExceptionFromMemory
# from Controller.controllerInchiriere import controllerRental
# from Domain.Validators import inchirieriValidator
# 
# from Repository.inmemory import repositoryMovie,RepoExceptionFromMemory
# from Controller.controllerMovie import controllerMovie
# from Domain.Validators import movieValidator
# 
# 
# from Repository.FileRepo import UniversalFileRepo,RepoException
# 
# class TestMovieController(unittest.TestCase):
#     def setUp(self):
#         self.ctr=controllerMovie(UniversalFileRepo("fisier_filme.txt",movie),movieValidator())
#         self.ctr.addMovie(11,"Awake","Okkkk", "Actiune")
# 
#     def test_create(self):
#         #self.assertTrue(self.ctr.size()==10)
#         self.assertRaises(RepoException,self.ctr.addMovie,11,"The Expandables","Bun","Actiune")
# 
#     def test_delete(self):
#         el=self.ctr.deleteMovie(1)
#         self.assertTrue(self.ctr.size() == 0)
#         self.assertTrue(el.getId()==1)
#         self.assertTrue(el.getTitle()=="Abduction")
#         self.assertTrue(el.getDescription()=="Okkkk")
#         self.assertTrue(el.getGender()=="Actiune")
# 
#     def test_update(self):
#         filmul=self.ctr.updateMovie(1, "Home Alone", "Bun", "Comedy")
#         self.assertTrue(filmul.getId()==1)
#         self.assertTrue(filmul.getTitle()=="Home Alone")
#         self.assertTrue(filmul.getDescription()=="Bun")
#         self.assertTrue(filmul.getGender()=="Comedy")
# 
# 
# class TestCaseClientController(unittest.TestCase):
#     def setUp(self):
#         val = clientValidator()
#         self.crt = controlerCustumer(repositoryClient(),val)
#         self.crt.add(1, "Alin", "007")
# 
# #     def tearDown(self):
# #         self.crt.dispose()
# #         self.crt=None
# 
# 
#     def test_Create(self):
#         self.assertTrue(self.crt.size()==1)
#         self.assertRaises(MyError,self.crt.add,"asa","Alin","123")
# 
#     def test_Remove(self):
#         self.assertRaises(RepoExceptionFromMemory,self.crt.removeCustumer,2)
#         self.assertTrue(self.crt.size()==1)
#         cl=self.crt.removeCustumer(1)
#         self.assertTrue(self.crt.size()==0)
#         self.assertTrue(cl.getId()==1)
#         self.assertTrue(cl.getName()=="Alin")
#         self.assertTrue(cl.getCnp()=="007")
# 
# class TestInchiriereController(unittest.TestCase):
#     def setUp(self):
#         self.ctr=controllerRental(repositoryMovie(),repositoryClient(),repositoryInchiriere(),inchirieriValidator())
#         self.ctr.adauga_inchiriere(1, 1, 1, date(2007, 12, 5),date(2007, 12, 5))
# 
#     def test_Create(self):
#         self.assertTrue(self.ctr.size()==1)
#         self.assertRaises(RepoExceptionFromMemory,self.ctr.existaIdFilm,2)
# 
#     def test_Remove(self):
#         inc = self.ctr.returnare_inchiriere(1)
#         self.assertTrue(self.ctr.size()==0)
#         self.assertTrue(inc.id_inchiriere == 1)
#         self.assertTrue(inc.id_film == 1)
#         self.assertTrue(inc.id_custumer == 1)
#         self.assertTrue(inc.data_inchirierii == date(2007, 12, 5))
#         self.assertTrue(inc.data_returnarii == date(2007, 12, 5))
