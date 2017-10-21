'''
Created on 28 dec. 2016

@author: Alin
'''
from tkinter import *
import tkinter
from tkinter import messagebox
# from Domain.Client import client
from Domain.Validators import MyError
from Repository.inmemory import RepoExceptionFromMemory


class RentalGUI:
    def __init__(self,ctr_client,ctr_movie,ctr_rental):
        self.__ctr_client = ctr_client
        self.__ctr_movie = ctr_movie
        self.__ctr_rental = ctr_rental
    
    def clear_entrys(self): 
        self.text_label1.delete(0,END)
        self.text_label2.delete(0,'end')
        self.text_label3.delete(0,'end')
        
    def __adaugare_client(self):
        try:
            self.__ctr_client.add(self.text_label1.get(),self.text_label2.get(),self.text_label3.get())
            messagebox.showinfo("Adaugare Client", "Adaugare cu succes !!! :D ")
        except MyError:
            messagebox.showerror("Eroare", "Eroare la validare")
        except RepoExceptionFromMemory:
            messagebox.showerror("Eroare","Duplicated client id ")
            
        self.clear_entrys()
    
    def __stergere_client(self):
        try:
            self.__ctr_client.removeCustumer(self.text_label1.get())
            messagebox.showinfo("Stergere Client", "Stergere efectuata cu succes...")
        except MyError:
            messagebox.showerror("Eroare", "Eroare la validare")
        except RepoExceptionFromMemory:
            messagebox.showerror("Eroare","Client id not exist")
        
        self.clear_entrys()        
    
    def __modificare_client(self):
        try:
            self.__ctr_client.updateCustumer(self.text_label1.get(),self.text_label2.get(),self.text_label3.get())
            messagebox.showinfo("Modificare Client", "Modificare efectuata cu succes... !!! :D ")
        except MyError:
            messagebox.showerror("Eroare", "Eroare la validare")
        except RepoExceptionFromMemory:
            messagebox.showerror("Eroare","Client id not exist ")
            
        self.clear_entrys()
    
                
    def __afisare_clienti(self):
        costumers = self.__ctr_client.getAllCustumers()       
        windows1 = Tk()
        windows1.geometry("300x190")
        
        list_box1 = Listbox(windows1,bg = "blue", fg = "red")
        list_box1.pack(fill = "both")
        for poz,el in enumerate(costumers):
            list_box1.insert(poz+1,str(el))
        
        windows1.mainloop()     
                
    def start_UI(self):
        self.window = Tk()
        self.window.title("Inchiriere Filme ")
        
        groupbox = Frame(self.window)
        groupbox.pack()
        self.frame = groupbox
        
        
        label1 = Label(groupbox,text = "ID: ")
        label1.pack(side = LEFT)
        
        self.text_label1 = Entry(groupbox)
        self.text_label1.pack(side = LEFT)
        
        label2 = Label(groupbox,text = "Nume:")
        label2.pack(side = LEFT)
        
        self.text_label2 = Entry(groupbox)
        self.text_label2.pack(side = LEFT)
        
        label3 = Label(groupbox,text = "Cnp:")
        label3.pack(side = LEFT)
        
        self.text_label3 = Entry(groupbox)
        self.text_label3.pack(side = LEFT)
        
        self.bAdaugaClient = Button(groupbox,text = "Adaugare client" , fg = "blue" ,command = self.__adaugare_client)
        self.bAdaugaClient.pack(side = LEFT)
        
        self.bStergeClient = Button(groupbox,text ="Stergere client" , fg = "orange",command = self.__stergere_client)
        self.bStergeClient.pack(side = LEFT)
        
        
        self.bModificaClient = Button(groupbox,text = "Modificare client" ,fg = "green",command = self.__modificare_client)
        self.bModificaClient.pack(side = LEFT)
        
        self.bAfisareClienti = Button(groupbox,text = "Afisare clienti " , fg = "brown",command = self.__afisare_clienti)
        self.bAfisareClienti.pack(side = LEFT)
        
        
        self.window.mainloop()
        
        