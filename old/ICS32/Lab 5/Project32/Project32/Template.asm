;// Lab 4(Lab4.asm)

;// Program Description:
;// Author:
;// Creation Date:
;// Revisions:
;// Date:              Modified by:

.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode : DWORD

.data
u_Byte	BYTE	 1		; declare variables here
s_Byte	SBYTE	-1		; declare variables here
u_Word	WORD	0FFFFh
s_Word	SWORD	0FFFFh
u_DWord	DWORD	12345678h
s_DWord	SDWORD	09ABCDEFh
myByte BYTE 0FFh, 0
var1 SDWORD 5
var2 SDWORD 20
var3 SDWORD -5
.code
main PROC


mov al,myByte ; AL =??
mov ah,[myByte+1] ; AH = ??
dec ah ; AH = ??
inc al ; AL = ??
dec ax ; AX = ??

mov ax,00FFh
add ax,1 ; AX= 0100h SF= 0 ZF= 0 CF= 0
sub ax,1 ; AX= ?? SF=?? ZF=?? CF=??
add al,1 ; AL= ?? SF=?? ZF=?? CF=??
mov bh,6Ch
add bh,95h ; BH= ?? SF=?? ZF=?? CF=??
mov al,2
sub al,3 ; AL= ?? SF=?? ZF=?? CF=??

mov al,-128
neg al ; CF =  1 OF =  1
mov ax,8000h
add ax,2 ; CF = ?? OF = ??
mov ax,0
sub ax,2 ; CF = ?? OF = ??
mov al,-5
sub al,+125 ; OF = ??

mov ax,0FDFFh ; -513
cwd
mov bx,100h
idiv bx ;After idiv: DX = ??, AX = ??
mov eax,00128765h
mov ecx,10000h
mul ecx ;After mul: EDX = ??, EAX = ??,CF = ??

mov ebx,10
mov ecx,2
mov eax,20
imul ebx
idiv ecx



mov ebx,10
mov ecx,var3
sub ecx, ebx
neg var2
mov eax,var1
imul var2
idiv ecx
mov var3,eax


COMMENT @
MOV	AL,	u_Byte
ADD	AL,	s_Byte

MOV EAX, 0
MOV EBX, 0

MOV	AX, u_Word
MOV	BX, s_Word
ADD AX, BX

MOV EAX, u_Dword
MOV EBX, s_DWord
@


INVOKE ExitProcess, 0

main ENDP


END main
