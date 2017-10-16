; GRupa 216
;Sfechis Alin Catalin
;10. Se da un sir de octeti S. Sa se obtina in sirul D multimea elementelor din S.
;Exemplu:
;S: 1, 4, 2, 4, 8, 2, 1, 1
;D: 1, 4, 2, 8

assume cs:code, ds:data

data segment
    S db  1, 4, 2, 4, 8, 2, 1, 1
    lenS equ $-S;lenS=8=1000b=8h
    D db lenS dup(?)
    lenD db 0;byte pt a-l putea modifica
data ends

code segment
start:
    mov ax,data
    mov ds,ax ; ds = SEG data
    mov es,ax ; es = SEG data
    
    ;pregatim parcurgerea lui S
    mov cx,lenS; cx = lenS cx=8=1000b=8h
    lea si, S ; mov si, offset S (adresa primului element din S)
    cld ; DF = 0
    
    jcxz final
    parcurgeS:
        lodsb ; al = <ds:si>, inc si
                ;echivalent cu:
                    ;mov si,0
                    ;mov al,ds:S[si]
                    ;inc si (trece la urmatorul element din S)
        push cx ; il punem pe cx in stiva cx=8=1000b=8h
        
        mov cl,lenD ;cl = lenD
        mov ch,0 ; cx = cl = lenD
        lea di, D ; mov di, offset D; di=offset D
        
        jcxz adauga ; lenD = 0 => nu avem elem in D => il punem oricum
        parcurgeD: ; parcurgem D
            scasb ; cmp al, <es:di>
            je found ; sunt egale, trecem peste adaugare
        loop parcurgeD

        adauga: ; adaugam doar daca lenD == 0 sau nu l-am gasit pe al in D
            ;di == lenD+1
            stosb ; <es:di> = al
            ;incrementam lenD
            mov al, lenD
            inc al
            mov lenD, al
        found:
            ;revenim la parcurgerea lui S
            pop cx ;cx = cx vechi (lenS)
    loop parcurgeS
    
    final:
    mov ax,4c00h
    int 21h
code ends
end start