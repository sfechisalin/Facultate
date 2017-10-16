assume cs:code, ds:data
data segment
	s dw '12','34','56','78'
	;21436587
	len equ $-s
	s2 db len dup(?)
	fileName db 'text.txt',0
	fileHandle dw ?
	openErrorMsg db 'Fisierul nu a putut fi deschis','$'
	writeErrorMsg db 'Nu s-a putut realiza scrierea in fisier','$'
data ends
code segment
start:
	mov ax,data
	mov ds,ax
	;deschid fisierul
	openFile:
		mov ah,3dh
		mov al,1
		mov dx,offset fileName
		int 21h
		jc openError
		mov fileHandle,ax
	
	mov cx,len 
	mov si,len
	dec si
	mov di,0
	jcxz final
	;formez noul sir cu biti in ordinea inversa ,tin cont de little-endian
	formare:
		mov dl,byte ptr s+si-1
		mov s2[di],dl
		inc di
		mov dl,byte ptr s+si
		mov s2[di],dl
		inc di
		sub si,2
		dec cx
		loop formare
	
	;scriu in fisier
	writeToFile:
		mov al,0h
		mov ah,40h
		mov bx,fileHandle
		mov cx,len
		mov dx,offset s2
		int 21h
		jc writeError
	jmp final
	
	openError:
		mov ah,09h
		mov dx,offset openErrorMsg
		int 21h
		
	writeError:
		mov ah,09h
		mov dx,offset writeErrorMsg
		int 21h	
	final:
		mov ax, 4c00h
		int 21h
code ends
end start