;Sa se citeasca de la tastatura un nume de fisier si un nume de director. 
;Sa se afiseze un mesaj corespunzator daca fisierul exista sau nu in directorul dat.

assume cs:code,ds:data

data segment

	mesajdir db 'Dati directorul: ','$'    ;mesajul care cere directorul
	director db 12,?,13 dup(?)	       ;variabila unde vom memora directorul	
	mesajfis db 10,13,'Dati fisierul: ','$' ;mesajul care cere fisierul
	fisier db 12,?,13 dup(?)		;variabila care memoreaza fisierul	
	mesaj_ok db 'Fisierul se afla in director',10,13,'$'
	mesaj_err db 'Fisierul NU se afla in director',10,13,'$'

data ends

code segment
start:

mov ax,data
mov ds,ax

mov ax,0900h
lea dx,mesajdir    ;afisam mesajul ptr director
int 21h	

mov ah,0Ah
lea dx,director     ;citim directorul
int 21h

mov bh,0
mov bl,director[1]
add bx,offset director     ;pointerul catre director trebuie sa fie in ASCIIZ,asa ca am adaugat un 0
mov byte ptr [bx+2],0

mov ax,3b00h
mov dx,offset director+2   ; am schimbat directorul curent de lucru in cel specificat de la tastatura
int 21h

mov ax,0900h
lea dx,mesajfis            ;afisam mesajel pentru fisier   
int 21h

mov ax,0A00h
lea dx,fisier               ;citim fisierul
int 21h

mov bh,0
mov bl,fisier[1]
add bx,offset fisier         ;punem 0 la sfarsitul pointerului catre fisier
mov byte ptr [bx+2],0

mov dx,offset fisier+2
mov ax,3D00h                   ;incercam sa deschidem fisierul, sa vedem daca este sau nu in director
int 21h

jc eroare                      ; daca CF s-a modificat, inseamna ca a fost o eroare la deschidere <=>fisierul nu exista
 	mov ah,09h
	lea dx,mesaj_ok        ; daca CF nu s-a modificat, fisierul exista,afisam mesajul OK
	int 21h
      jmp sfarsit

eroare:
	mov ah,09h
	lea dx,mesaj_err       ; a fost eroare la deschidere, fisierul nu exista, afisam mesajul de eroare
	int 21h

sfarsit:
mov ax,4c00h
int 21h

code ends
end start