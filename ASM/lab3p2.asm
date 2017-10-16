;2. Se dau doua siruri de octeti s1 si s2. Daca sirul
; s1 este inclus în s2 atunci se va retine în variabila rez pozitia
;din sirul s2 de unde începe sirul s1, altfel rez va contine FFh. 

;sol: at each step, i load a byte from the second string and compare it with
;the current one from s1. if they are the same, i load another one
;from both strings. when they stop being the same, i take again the first 
;byte from the start and keep loading bytes in the second one

assume cs:code, ds:data

data segment
	s1 db 2, 3, 2,3,4
	len equ $-s1
	s2 db 2, 3, 2,3,2,3,4, 5, 6 , 9, 9
	len2 equ $-s2
	rez dw ?
	notFound equ 0FFh
	minusOne equ -1
	
data ends

code segment
start:
	mov ax, data
	mov ds, ax
	mov es, ax
	
	mov si, 0
	mov di, 0
	mov rez, minusOne
	mov cx, len2
	
		again:
			mov al, s1[si]
			mov bl, s2[di]
			cmp al, bl
			jne notEqual
				;if they are equal
				;i test to see whether i've checked the entire string s1
				cmp si, len-1
				je done		;if yes, i am done
					;otherwise
					inc si
					inc di
					jmp endLoop
				done:
					;i compute in rez the position = the position in the second string at which i am now minus the length of the first string
					mov rez, di
					sub rez, len
					add rez, 1
					jmp endProgram
			notEqual:
			;i continue my search
			sub di, si
			mov si, 0
			inc di
		endLoop:
		cmp di, len2
		jb again
		
		cmp rez, -1
		jne endProgram
			mov rez, notFound
		endProgram:
	mov ax, 4c00h
	int 21h
code ends
end start