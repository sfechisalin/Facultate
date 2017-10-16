;sa se calculeze suma a doua numere zecimale citite de la
;tastatura. Sa se afiseze rezultatul pe ecran.
ASSUME cs: code, ds:data
data SEGMENT     
    msg db 'Introdu un numar zecimal: $'
    n1 db 10,?,10 dup(0)   
    n2 db 10,?,10 dup(0)   
    newl db 10,13,'$'   
    int1 dw 3 dup(0)
    int2 dw 3 dup(0)  
    pi_int dw 3
    pi_fr dw 1415 
    rez db 9 dup(0)  
    zece dw 10
    
data ENDS
code SEGMENT

start:
	mov ax,data    
    mov ds,ax  
    mov es,ax  
                                       
    mov ah,09h
    lea dx,msg
    int 21h                                   
    ;citesc primul numar
    mov ah,0ah
    lea dx,n1
    int 21h
    
    ;determin cate cifre am inaninte de virgula
    mov bx,0
    mov cx,0
    mov ax,0
    lea si,n1[2]
    mov cl,n1[1]
    rep1: 
        lodsb
        cmp al,'.'
        je redoNr1
        cmp bl,n1[1]
        je redoNr1
        inc bl
        sub al,'0'
        push ax 
        loop rep1 
    redoNr1:
    ;refac numarul 
    mov cl,bl
    mov ax,1  
    mov word ptr int1[0],0
    loadDec1: 
        mov bx,ax
        pop dx
        mov dh,0
        mul dx
        add word ptr int1[0],ax
        mov ax,bx
        mov bl,10
        mul bl
        loop loadDec1
    ;determin cifrele de dupa virgula
    ;determin cate pozitii am parcurs din sir
    mov ax,si
    sub ax,offset n1[2]
    mov cx,0
    mov cl,n1[1]
    sub cl,al 
    ;daca cx=0 -> nu am cifre zecimale  
    mov ax,0
    jcxz aduna
    mov bx,0
    rep2:
        lodsb
        inc bl
        sub al,'0'
        push ax
        loop rep2
    ;refac numarul
    mov cl,bl  
    mov word ptr int1[4],bx
    mov ax,1
    mov word ptr int1[2],0
    loadDec2: 
        mov bx,ax
        pop dx
        mov dh,0
        mul dx
        add word ptr int1[2],ax
        mov ax,bx
        mov bl,10
        mul bl
        loop loadDec2
    
    ;verific daca trebuie sa inmultesc partea fractionara cu ^10
    mov al,4
    sub al,byte ptr int1[4]
    cmp al,0 
    je aduna
    xor cx,cx
    mov cl,al
    mov ax,word ptr int1[2]
    inm:
        mul zece
        loop inm  
        jmp adunaNr
    aduna: 
    mov ax,word ptr int1[2]
    adunaNr:
    ;in ax am partea fractionara, pun un dx partea intreaga
    mov dx,word ptr int1[0]
    add ax,pi_fr
    ;determin daca am transport
    cmp ax,10000
    jb addwc
    sub ax,10000
    stc;trebuie sa adaug un transport  
    adc dx,pi_int
    jmp next2
    addwc:
    add dx,pi_int    
    next2:
    ;transform in string si salvez in rez
    push ax;salvez partea zecimala
    mov ax,dx
    xor bx,bx
    divZ:
        mov dx,0
        div zece
        push dx
        inc bl
        cmp ax,0
        jne divZ
    ;transform in numar si adaug in rez
    lea di,rez
    cld      
    xor cx,cx
    mov cl,bl
    trnZ:
        pop ax
        add al,'0'
        stosb
        loop trnZ
    ;transform in numar partea zecimala si o adaug in rez
    mov al,'.'
    stosb
    pop ax
    xor bx,bx
    divF:
        mov dx,0
        div zece
        push dx
        inc bl
        cmp ax,0
        jne divF
    ;verific daca trebuie sa mai adaug un 0
    xor cx,cx
    mov cl,4
    sub cl,bl
    je next1
    adaugaZ:
        mov ax,0
        push ax
        loop adaugaZ
    next1:
    mov cx,4
    adaugaF:
        pop ax  
        add al,'0'
        stosb
        loop adaugaF
    
    
    
    
    mov ax,4C00h
    int 21h   
code ENDS
END start