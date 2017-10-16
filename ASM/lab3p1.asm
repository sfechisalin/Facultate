; 1. Se da un sir de octeti. Sa se creeze un nou sir 
; de aceeasi lungime, care va contine 
; doar acei octeti din primul sir care au numarul de biti 1 mai mare 
; decât numarul de biti 0 
; sau acei octeti care au valoarea cuprinsa între [1fh,60h];
; în rest, cel de al doilea sir se va completa cu 0. 
assume cs:code, ds:data

data segment
	s1 db 11111000b, 10000000b, 020h, 01dh, 05fh, 060h, 061h
	len equ $-s1
	s2 db len dup (?)
data ends



code segment
start:
	mov ax, data
	mov ds, ax
	mov es, ax
	
	mov si, offset s1
	mov di, offset s2
	
	mov cx, len
	cmp cx, 0
	je sfarsit
	
	again:
		lodsb		;loads in AL a byte from s1
		;first, I check if it belongs to [1fh, 60h]
		cmp al, 1fh		;if it's bigger than 1fh, i test if it's less than 60h
		jna testbiti1	;if it's not bigger, i count the number of bits 1
		cmp al, 60h
		jnb testbiti1
		;if the execution has reached this point, means the number is in the interval
		;so I place it in the final string
		stosb
		jmp sfarsit
		;else, i test the number of bits
		testbiti1:
			call numaraBiti
			cmp bl, 4		;if there are at least 4 bits of 1, it is obvious that there are more 1s than 0s
			jb putZero
				;if it's above 4, i copy it to the final strng
				stosb
				jmp sfarsit
			putZero:
			mov al, 0
			stosb
		sfarsit:
	loop again
	
	jmp itisover
	numaraBiti proc		;numara bitii de 1 din AL
		push cx			;i save cx on the stack
		mov cx, 8		;i have to check 8 bits
		xor bx, bx		;equal to mov bx, 0
		
		iar:
			rol al, 1	;i rotate the bits
			adc bl, 0	;the leftmost will go in the carry
		loop iar
		
		pop cx			;restoring cl
		ret				;returning from the procedure
	numaraBiti endp
	itisover:
	
	mov ax, 4c00h
	int 21h
code ends
end start