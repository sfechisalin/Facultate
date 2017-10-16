;4. Se da un sir de cuvinte. Sa se construiasca doua siruri de octeti, s1 si s2, astfel: pentru fiecare cuvânt,
;- daca numarul de biti 1 din octetul high al cuvântului este mai mare decât numarul de biti 1 din octetul low, 
;atunci s1 va contine octetul high, iar s2 octetul low al cuvântului
;- daca numarul de biti 1 din cei doi octeti ai cuvântului sunt egali, atunci 
;s1 va contine numarul de biti 1 din cuvant, iar s2 valoarea 0
;- altfel, s1 va contine octetul low, iar s2 octetul high al cuvântului. 

assume cs:code, ds:data

data segment
	s1 dw 1111111100000000b, 1000000011000000b, 1111111111111111b, 0110011000010010b, 1010000010100000b
	len equ $-s1			;len will hold 10, because 10 bytes have been generated so far (a word = 2 bytes => 5 words, 10 bytes)
	s2 db len/2 dup (?)
	s3 db len/2 dup (?)

data ends

code segment
start:
	mov ax, data
	mov ds, ax
	mov es, ax
	
	mov si, offset s1
	mov di, 0
	mov cx, len
	
	
		again:
			lodsw
			mov bx, 0
			call compareNumberOfBits1		
				;the procedure will "return" bx having 
				;				in bh the number of 1s in the high byte
				;				in bl the number of 1s in the low byte
				
				cmp bh, bl
				je Equal
					;otherwise
					jb Below
						;otherwise, means the high byte has more 1s than the low byte
						;=> s1 will hold the high byte, s2 the low byte
						mov s2[di], ah
						mov s3[di], al
						jmp endStep
					Below:
						;means that the high bite has a smaller number of 1s than the low byte
						;=>s1 will hold the low byte, s2 the high byte
						mov s2[di], al
						mov s3[di], ah
						jmp endStep
				Equal:
					;means that the number of 1s is equal
					;=> s1 will hold the number of 1s from the word and s2 will hold 0
					add bh, bl
					mov s2[di], bh
					mov s3[di], 0
					
			endStep:
			inc di
		loop again
		
	jmp sfarsitProgram
		
		compareNumberOfBits1 Proc
			push cx			;i save the content of cx
			mov cx, 8
			mov bx, 0
			;i count in bl the number of 1s in al
			iar:
				rol al, 1 
				adc bl, 0
			loop iar
			
			;i count in bh the number of 1s in ah
			mov cx, 8
			siiar:
				rol ah, 1
				adc bh, 0
			loop siiar
			pop cx
			ret
		compareNumberOfBits1 Endp
	sfarsitProgram:	
	mov ax, 4c00h
	int 21h
code ends
end start