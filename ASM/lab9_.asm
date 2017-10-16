assume cs:code, ds:data 
data segment 
	sir db 2, 4, 2, 5, 2, 2, 4, 4 ,1,1,1,7,8
	l EQU $-sir  
	cont dw 0
	lb dw 1
	dest dw l DUP(?) 

data ends
code segment
start:
	mov ax,data
	mov ds,ax
	mov es,ax
	mov dx,l
	mov di,offset dest
	repeta:
		mov si,offset sir
		add si,cont
		inc cont
		lodsb 
		mov bl,al 
		mov cx,lb
		mov si,offset dest 
		next: 	 
			lodsw 
			cmp al,bl 
			je adaugare 
			loop next 
			jmp pune 
			adaugare:
				mov di,si
				sub di,2 
				inc ah 
				stosw 
				jmp final 
			pune: 
				mov di,offset dest
				add di,lb
				add di,lb
				sub di,2
				mov al,bl 
				mov ah,1 
				stosw 
				inc lb 
	final: 
		dec dx 
		cmp dx,0 
		jnz repeta  
	mov ax,4C00h 
	int 21h 
code ends 
end start
		
	
