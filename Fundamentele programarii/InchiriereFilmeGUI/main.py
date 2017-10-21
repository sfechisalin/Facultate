'''
Created on 6 dec. 2016

@author: Alin
'''
from UI.gui import RentalGUI

from Repository.FileRepo import ClientFileRepo,UniversalFileRepo 
from Repository.inmemory import repositoryClient,repositoryInchiriere,repositoryMovie
from Controller.controllerClient import controlerCustumer
from Controller.controllerInchiriere import controllerRental
from Controller.controllerMovie import controllerMovie
from UI.Interface import Consola
from Domain.Film import movie
from Domain.Validators import clientValidator,movieValidator,inchirieriValidator
from Domain.Inchiriere import inchiriere
if __name__=='__main__':
#     client_repo=repositoryClient()
#     movie_repo=repositoryMovie()
#     inchiriere_repo=repositoryInchiriere()
    client_repo=ClientFileRepo("clienti.txt")
    movie_repo=UniversalFileRepo("filme.txt",movie)
    inchiriere_repo=UniversalFileRepo("inchirierii.txt",inchiriere)     
    client_val=clientValidator()
    movie_val=movieValidator()
    inchiriere_val=inchirieriValidator()
    
    client_controller=controlerCustumer(client_repo,client_val)
    movie_controller=controllerMovie(movie_repo,movie_val)
    inchiriere_controller=controllerRental(movie_repo,client_repo,inchiriere_repo,inchiriere_val)
     
    #generator=Generator(client_repo,movie_repo,inchiriere_repo)
    #generator.initializare(7)   
      
    #consola=Consola(client_controller,inchiriere_controller,movie_controller)
    consola = RentalGUI(client_controller,movie_controller,inchiriere_controller)    
    consola.start_UI()