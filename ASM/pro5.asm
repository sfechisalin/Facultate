;primele n numere impare
assume cs:code,ds:data

data segment
	msg1 db 'Introduce-ti valoarea lui n $'
	n db 3,?,3 dup (0)
	rez db 100 dup(0)
	newLine db 10,13,'$'
	zece db 10 
data ends

code segment
	start:
		push data
		pop ds 
		
		mov ah,9
		lea dx,msg1
		int 21h
		
		mov ah,0Ah
		lea dx,n 
		int 21h 
		
		xor ch,ch
		mov cl,n[1]
		
		
		mov ah,9
		lea dx,newLine
		int 21h
		
		mov si,2
		mov bx,0
		repeta:
			mov al,n[si]
			sub al,30h 
			xor ah,ah 
			push ax
			inc bx 
			
			inc si 
			loop repeta
		
		mov cx,bx 
		xor bx,bx 
		mov ax,0 ; suma 
		repeta1: 
			pop bx 
			mul zece 
			add ax,bx 
			loop repeta1 
			
	mov ah,4C00h
	int 21h
code ends
end start 