'''
Created on 6 dec. 2016

@author: Alin
'''
from datetime import date
from Domain.Validators import MyError
from Repository.inmemory import RepoExceptionFromMemory
from Repository.FileRepo import RepoException

class EroareaMea(Exception):
    def __init__(self,msg):
        self.__eroare=msg
    def __str__(self):
        return str(self.__eroare)
    
    
class Consola:
    def __init__(self,client_controller,inchiriere_controller,film_controller):
        self.__client_controller=client_controller
        self.__inchiriere_controller=inchiriere_controller
        self.__film_controller=film_controller
    
    def __adaugare_client(self):
        '''
        Adaugam un client nou
        '''
        #while True:
        try:
            ID=int(input("Introduce-ti id-ul clientului"))
            NUME=input("Introduce-ti numele clientului")
            CNP=input("Introduce-ti cnp-ul clientului")
            self.__client_controller.add(ID,NUME,CNP)
            print("Adaugare cu succes...\n")
            # break
        except ValueError as ve:
            print(ve)
        except MyError as me:
            #print(`me`)
            #`a` == repr(a)
            print(me)
        except RepoException as re:
            print(re)
        except RepoExceptionFromMemory as rev:
            print(rev)
                
    def __stergere_client(self):
        '''
        Stergem un client
        '''
        while True:
            try:
                ID=int(input("Introduce-ti id-ul clientului pe care doriti sa-l stergeti")) 
                self.__client_controller.removeCustumer(ID)
                try:
                    self.__inchiriere_controller.returnare_inchiriere_client(ID)
                except:
                    pass
                print("Stergere cu succes...\n")
                break
            except RepoException as re:
                print(re)
            except MyError as me:
                print(me)
            except ValueError as ve:
                print(ve)
            except RepoExceptionFromMemory as rev:
                print(rev)
                
    def __modificare_client(self):
        '''
        Modifica clientul dupa id
        '''
        while True:
            try:
                ID1=int(input("Introduceti id-ul clientului pe care doriti sa-l modificati"))
                NUME=input("Introduceti noul nume al clientului")
                CNP=input("Introduceti noul cnp al clientului")
                self.__client_controller.updateCustumer(ID1,NUME,CNP)
                print("Modificare efectuata cu succes...\n")
                break
            except RepoException as re:
                print(re)
            except MyError as me:
                print(me)
            except RepoExceptionFromMemory as rev:
                print(rev)
                
    def __afisare_clienti(self):
        allcustumer=self.__client_controller.getAllCustumers()
        # for i,cl in enumerate(allcustumer):
        #     print("{}.{}".format(i+1,cl))
        def afisare_recursiv(poz):
            if poz < len(allcustumer):
                print("{}.{}".format(poz + 1, allcustumer[poz]))
                afisare_recursiv(poz+1)
        afisare_recursiv(0)
        print("============")
        
        
    def __adaugare_film(self):
        while True:
            try:
                ID=int(input("Dati id-ul filmului.\n "))
                TITLU=input("Dati numele filmului.\n")
                DESCRIERE=input("Dati descrierea filmului.\n")
                GEN=input("Dati genul filmului.\n")
                self.__film_controller.addMovie(ID,TITLU,DESCRIERE,GEN)
                print("Adaugare cu succes...")
                break
            except MyError as me:
                print(me)
            except ValueError as ve:
                print(ve)
            except RepoException as re:
                print(re)
            except RepoExceptionFromMemory as rev:
                print(rev)
            
    def __stergere_film(self):
        while True:
            try:
                ID=int(input("Introduceti id-ul filmului pe care doriti sa-l stergeti.\n"))
                self.__film_controller.deleteMovie(ID)
                try:
                    self.__inchiriere_controller.returnare_inchiriere_film(ID)
                except:
                    pass
                print("Stergere cu succes...")
                break
            except RepoException as me:
                print(me)
            except ValueError as ve:
                print(ve)
            except RepoExceptionFromMemory as rev:
                print(rev)
                
    def __modificare_film(self):
        while True:
            try:
                ID_OLD=int(input("Introduceti id-ul filmului de modificat"))
                TITLU_new=input("Dati noul numele al filmului.\n")
                DESCRIERE_new=input("Dati noua descrierea a filmului.\n")
                GEN_new=input("Dati noul genul al filmului.\n")
                self.__film_controller.updateMovie(ID_OLD,TITLU_new,DESCRIERE_new,GEN_new)
                print("Modificare cu succes...")
                break
            except RepoException as re:
                print(re)
            except ValueError as ve:
                print(ve)
            except MyError as me:
                print(me)
            except RepoExceptionFromMemory as rev:
                print(rev)
    
    def __afisare_filme(self):
        all_filme=self.__film_controller.getAllMovies()
        print("ID     TITLE    DESCRIPTION    GENDER \n")
        for film in all_filme:
            print("{}. {}  {}  {}".format(film.getId(),film.getTitle(),film.getDescription(),film.getGender()))
            
    def __adaugare_inchiriere(self):
        while True:
            try:
                ID_INCHIRIERE=int(input("Introduceti id-ul inchirierii"))
                ID_FILM=int(input("Introduceti id-ul filmului"))
                ID_CLIENT=int(input("Introduceti id-ul clientului"))
                self.__inchiriere_controller.existaIdClient(ID_CLIENT)
                self.__inchiriere_controller.existaIdFilm(ID_FILM)
                try:
#                     data_inchirierii = date(*map(int, input("Introduce-ti data inchirierii,format yy/mm//dd ").split("/")))
                    data_inchirierii =input("Introduceti data inchirierii,format yy/mm//dd ")
                    data_returnarii = input("Introduceti data returnarii,format yy/mm/dd ")
                    self.__inchiriere_controller.adauga_inchiriere(ID_INCHIRIERE,ID_FILM,ID_CLIENT,data_inchirierii,data_returnarii)
                    print("Adaugare cu succes...")
                    break
                except MyError as me:
                    print(me)
                except RepoExceptionFromMemory as rev:
                    print(rev)
                except:
                    print("Datele nu sunt valide")
            except MyError as me:
                print(me)      
            except RepoException as re:
                print(re)
            except ValueError as ve:
                print(ve)
            except RepoExceptionFromMemory as rev:
                print(rev)
                   
    def __sterge_inchiriere(self):
        while True:
            try:
                ID=int(input("Dati id-ul inchirierii pe care doriti sa o returnati "))
                self.__inchiriere_controller.InchiriereID(ID)
                self.__inchiriere_controller.returnare_inchiriere(ID)
                print("Sterere cu succes...")
                break
            except ValueError as ve:
                print(ve)
            except RepoException as re:
                print(re)
            except RepoExceptionFromMemory as rev:
                print(rev)   
               
    def __afisare_inchiriere(self):
        
        print("Id_inchiriere   Id_film    Id_custumer    Data_inchirierii   Data_returnarii \n")
        for rental in self.__inchiriere_controller.getAllRentals():
            print("{}          {}               {}                     {}    {} \n ".format(rental.getId(),rental.getIdFilm(),rental.getIdCustumer(),rental.getDataInchirierii(),rental.getDataReturnarii()))
                
        print("=========================================================")
        
    def __clientiFilmeOrderByName(self):
        for i,cl in enumerate(self.__inchiriere_controller.listaClientiFilmeInchiriateOrd()):
            print("Clientul {}. {} \n".format(i+1,cl))
    
            
    def __clientiFilmeOrderByNumber(self):
        for i,cl in enumerate(self.__inchiriere_controller.listaClientiNumarFilmeInchiriateOrd()):
            print("Clientul {}. {} {} \n".format(i+1,cl[0],cl[1]))
        
        
    def __filmeMaximInchiriate(self):
        for i,cl in enumerate(self.__inchiriere_controller.celeMaiInchiriateFilme()):
            print("Filmul {}. {}".format(i+1,cl))
    
    def __clienti_30(self):
        lista=self.__inchiriere_controller.listaClientiNumarFilmeInchiriateOrd()
        try:
            lungime = ( 30 * self.__client_controller.size() ) // 100
            answ = lista[:lungime]
            for i,cl in enumerate(answ):
                print("Clientul {}. {} {} \n".format(i+1,cl[0],cl[1]))
        except ZeroDivisionError:
            print("Avem de afisat 0 clienti :)) \n")
    def __show_menu(self):
        '''
        Afisam meniul programului
        '''
        print("=========================================================")
        print("1.Adaugare client.\n")
        print("2.Stergere client.\n")
        print("3.Modificare client(NUME).\n")
        print("4.Afisare clientii.\n")
        print("5.Adaugare film.\n")
        print("6.Stergere film.\n")
        print("7.Modificare film.\n")
        print("8.Afisare filmele.\n")
        print("9.Adaugare inchiriere.\n")
        print("10.Returnare inchiriere.\n")
        print("11.Afisare inchirieri.\n")
        print("12.Clientii cu filmele inchiriate ordonati dupa nume.\n")
        print("13.Clientii cu filmele inchiriate ordonati dupa numarul de filme inchiriate.\n")
        print("14.Cele mai inchiriate filme.\n")
        print("15.Primii 30% clienti cu cele mai multe filme inchiriate.\n")
        print("0.Exit")
        print("=========================================================")
        
    def start_UI(self):
        while True:
            self.__show_menu()
            try:
                op=int(input("Introduce-ti optiunea dorita\n"))
            except:
                print("Optiunea pe care ati introdus-o nu este valida")
            if op==1:
                self.__adaugare_client()
            elif op==2:
                self.__stergere_client()
            elif op==3:
                self.__modificare_client()
            elif op==4:
                self.__afisare_clienti()
            elif op==5:
                self.__adaugare_film()
            elif op==6:
                self.__stergere_film()
            elif op==7:
                self.__modificare_film()
            elif op==8:
                self.__afisare_filme()
            elif op==9:
                self.__adaugare_inchiriere()
            elif op==10:
                self.__sterge_inchiriere()
            elif op==11:
                self.__afisare_inchiriere()
            elif op==12:
                self.__clientiFilmeOrderByName()
            elif op==13:
                self.__clientiFilmeOrderByNumber()
            elif op==14:
                self.__filmeMaximInchiriate()
            elif op==15:
                self.__clienti_30()
            elif op==0:
                break;
            else:
                print("Comanda invalida \n Byeee :-h ")
                break;
            