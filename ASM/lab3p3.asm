;3. Se dau doua siruri de octeti. Sa se parcurga cel mai scurt sir dintre cele doua siruri 
;si sa se construiasca un al treilea sir care va contine cel mai mare element de acelasi 
;rang din cele doua siruri, iar pâna la lungimea celui mai lung sir, sirul al treilea se 
;va completa alternativ cu valoarea 1 respectiv 0. 

assume cs:code, ds:data

data segment
	s1 db 2, 3, 2,3,4, 1
	len1 equ $-s1
	s2 db 2, 3, 2,3,2,3,4, 5, 6 , 9, 9
	len2 equ $-s2
	s3 db len1+len2 dup(?)
	max db ?
	min db ?
	value db ?
data ends

code segment
start:
	mov ax, data
	mov ds, ax
	
	mov si, 0
	
	;first, i determine the shortest length. i assume that len1 is the one, and i hold it in al
	mov al, len1
	mov ah, len2
	cmp al, ah
	jb correct
		;otherwise, i reverse them
		mov al, len2
		mov ah, len1
	correct:
	push ax			;i keep the min/max values on the stack (min=al, max=ah)
	mov ah, 0
	cbw				;i work only with al
	mov cx, ax
	;first, i take care of first part of the problem
		again:
			mov bl, s1[si]
			mov bh, s2[si]
			cmp bl, bh
			ja puneDin1
				;otherwise, i put from the second string
				mov s3[si], bh
				jmp endStep
			puneDin1:
				mov s3[si], bl
			endStep:
			inc si
		loop again
		
	;now, i handle the remaining part of the exercise
	;i will fill the vector with 1,0,1,...
	;for this, at each step i will store AL in the vector
	;then, i switch its value by negating it and adding 1
	;hence, for 1: neg 1 = -1, -1 + 1 = 0
	;		for 0: neg 0 = 0, 0 + 1 = 1
		
		pop ax 			;i restore the min/max
		sub ah, al
		mov cl, ah		
		mov ch, 0
		mov al, 1		;i will place AL in s3[si]
		
		iar:
			mov s3[si], al
			inc si
			neg al
			add al, 1
		loop iar
		
	mov ax, 4c00h
	int 21h
code ends
end start