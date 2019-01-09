.data
	myByte BYTE 0FFh, 0

	Rval SDWORD ?
	Xval SDWORD 25
	Yval SDWORD -5
	Zval SDWORD 20

	var1 SDWORD 5
	var2 SDWORD 20
	var3 SDWORD -5

.code

	; QUESTION 1
	mov al,myByte		; AL = FF
	mov ah,[myByte+1]	; AH = 00
	dec ah				; AH = FF
	inc al				; AL = 00
	dec ax				; AX = FEFF

	; QUESTION 2
	mov ax,00FFh
	add ax,1 ; AX= 0100h SF= 0 ZF= 0 CF= 0
	sub ax,1 ; AX= 00FFh SF= 0 ZF= 0 CF= 0
	add al,1 ; AL=   00h SF= 0 ZF= 1 CF= 1
	mov bh,6Ch
	add bh,95h ; BH= 01 SF= 0 ZF= 0 CF= 1
	mov al,2
	sub al,3 ; AL= FF SF= 1 ZF= 0 CF= 1

	; QUESTION 3
	mov al,-128
	neg al ; CF = 1 OF = 1
	mov ax,8000h
	add ax,2 ; CF = 0 OF = 0
	mov ax,0
	sub ax,2 ; CF = 1 OF = 0
	mov al,-5
	sub al,+125 ; OF = 1

	; QUESTION 4
	mov ax,0FDFFh ; -513
	cwd
	mov bx,100h
	idiv bx ;After idiv: DX = FFFF, AX = FFFE
	mov eax,00128765h
	mov ecx,10000h
	mul ecx ;After mul: EDX = 00000012, EAX = 87650000, CF = 1

	; QUESTION 5
	mov eax, Xval
	mov ebx, Yval
	neg ebx
	add ebx, Zval
	sub eax, ebx
	mov Rval, eax

	; QUESTION 6
	mov ebx,10
	mov ecx,2
	mov eax, 20
	imul ebx
	idiv ecx

	; QUESTION 7
	mov ebx,10
	mov ecx,var3
	mov edx, var2
	sub ecx, ebx
	neg edx
	mov eax,var1
	imul edx
	idiv ecx
	mov var3,eax
