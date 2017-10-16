;16. Sa se citeasca de la tastatura numele unui fisier. Sa se verifice 
;daca dimensiunea fisierului este multiplu de 13, si în caz negativ sa se 
;completeze fisierul cu un numar minim de octeti 0 astfel încât dimensiunea 
;fisierului sa devina multiplu de 13.

assume ds:data, cs:code
data segment
msgInput db 'Introduceti numele fisierului$'
msgEMultiplu db 'Fisierul are dimensiunea multiplu de 13$'
maxFile	db 13
lenFile	db ?
strFile	db 13 dup('$')
LF	 equ 10
filehandle dw ?
buffer db 12 dup('0')

data ends
code segment
start:
	mov ax,data
	mov ds, ax
	
	; Afisez un mesaj pt introducerea numelui fisierului
	mov dx, offset msgInput
	mov ah, 09h
	int 21h

	; Citesc numele fisierului
	mov dx, offset maxFile ; pointer spre input buffer
	mov ah, 0Ah ; buffered input
	int 21h ; apelez intreruperea

	; Las un rand liber
	mov dl, LF 
	mov ah, 02h 	; char output
	int 21h
	
	; Transform numele fisierului intr-un sir ASCIIZ
	mov al, lenFile
	mov ah,0 ; =xor ah,ah
	mov si, ax
	mov [strFile+si], 0

	; Open file with handle
	mov ah, 3Dh
	mov al, 2h 	;open mode; Access mode ;Read/Write acces
	mov dx,  offset strFile
	int 21h
	mov filehandle, ax
	
	; Aflu numarul de octeti din fisier
	mov bx, ax	; bx handle 
	mov ah, 42h
	mov cx, 0
	mov dx,0
	mov al, 2
	int 21h
	
	; Aflu daca dimensiunea fisierului e multiplu de 13
	mov bx, 13
	div bx
	cmp dx, 0
	je multiplu
	mov cx, 13
	sub cx, dx ;cx ne va spune care e nr minim de octeti care trebuie adaugati la sfarsitul fisierului
				; pt ca dimensiunea acestuia sa devina multiplu de 13
	mov ah, 40h
	mov bx, filehandle
	mov dx, offset buffer
	int 21h
	jmp sfarsit
	
	multiplu:
	;afisez mesajul
		mov dx, offset msgEMultiplu
		mov ah, 09h
		int 21h
		
	; the end
	sfarsit:
	mov ax, 4C00h
	int 21h

code ends
end start

	

