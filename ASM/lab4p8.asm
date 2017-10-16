;8. Sa se stearga un fisier al carui nume va fi introdus de la tastatura. 
;Orice situatie de eroare va fi semnalata printr-un mesaj corespunzator.
assume cs:code, ds:data

data segment
	fileName db 12, ?, 12 dup (?)
	pnf db 'Path not found. $'
	fnf db 'File not found. $'
	ad db 'Access denied. $'
	input db 'Give the name of the file: ', 13, 10, '$'
	
data ends

code segment
start:

	mov ax, data
	mov ds, ax
		;print the message for the user
		mov ah, 09h
		lea dx, input
		int 21h
		
		;first i read the file name
		mov ah, 0ah
		mov dx, offset filename
		int 21h
		
		;then i transform the filename into an asciiz string
		; i.e. i add a '0' at the end
		mov bl, fileName[1]
		mov bh, 0
		add bx, offset fileName
		add bx, 2

		mov byte ptr [bx], 0
		
		;now i delete, using 41h function
		
		mov ah, 41h
		mov dx, offset filename + 2
		int 21h
		
		jc errors		;if the carry is set, means there've been errors
		jmp done		;otherwise, smile! we're done :)
		
		errors:			;tedious job, handling those errors...
		
		cmp ax, 3
		je pathNotFound
		jb fileNotFound	;i.e. ax = 2
		ja accesDenied	;i.e. ax = 5
		
		jmp done		;i skip treating the errors
		
		pathNotFound:
			mov ah, 09h
			mov dx, offset pnf
			int 21h
			jmp done
		
		fileNotFound:
			mov ah, 09h
			lea dx, fnf
			int 21h
			jmp done
		
		accesDenied:
			mov ah, 09h
			lea dx, ad
			int 21h
			jmp done

	done:
	mov ax, 4c00h
	int 21h
	
code ends
end start
