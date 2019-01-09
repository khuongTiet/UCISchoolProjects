.data
	myByte BYTE 0FFh, 0
.code
	; QUESTION 1
	mov al, myByte		; AL = 0FFh
	mov ah, [myByte+1]		; AH = 100h
	dec ah				; AH = 
	inc al				; AL = 
	dec ax				; AX =