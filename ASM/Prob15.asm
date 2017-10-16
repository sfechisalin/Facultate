;15. Sa se citeasca de la tastatura un doua nume de directoare dir1 si dir2.
;Sa se creeze directorul dir1\dir2.



assume ds:data,cs:code

data segment
 msg1 db 'Numele primului director: $'
 msg2 db 'Numele celui de-al doile director: $'
 maxDirName1 db 12
 lDirName1 db ?
 DirName1 db 12 dup (?)
 maxDirName2 db 12
 lDirName2 db ?
 DirName2 db 12 dup (?)
data ends

code segment
 inceput:
 mov ax,data
 mov ds,ax
 
 mov dx,offset msg1 ;afisez la interfata
 mov ah,09h           ; standard de iesire mesajul msg1
 int 21h                 ;folosind functia 09h din intreruperea 21h
 mov ah,0Ah
 mov dx, offset maxDirName1
 int 21h
 ;în urma citirii la adresa maxDirName+2=DirName se memoreaza numele directorului citit
 ;la adresa maxDirName+1=lDirName se memoreaza dimensiunea sirului de caractere care reprezinta numele directorului
 mov ah,39h
 mov dx,offset dirName1
 int 21h
 mov ah,0Ah
 
 mov dx, offset maxDirName2
 int 21h
 ;în urma citirii la adresa maxDirName+2=DirName se memoreaza numele directorului citit
 ;la adresa maxDirName+1=lDirName se memoreaza dimensiunea sirului de caractere care reprezinta numele directorului
 mov ah,39h
 mov dx,offset dirName2
 int 21h

 mov ax,4C00h
 int 21h
code ends

end inceput