;// Lab 4(Lab4.asm)
;// Program Description:
;// Author:
;// Creation Date:
;// Revisions:
;// Date: Modified by:

.386
.model flat, stdcall
.stack 4096
ExitProcess PROTO, dwExitCode : DWORD

.data
u_Byte	    BYTE	 1
s_Byte	    SBYTE	 -1
u_Word	    WORD	 0FFFFh
s_Word	    SWORD	 0FFFFh
u_DWord	    DWORD	 12345678h
s_DWord	    SDWORD 09ABCDEFh

.code
main PROC

MOV AL, u_Byte
ADD AL, s_Byte

MOV EAX, 0
MOV EBX, 0

MOV AX, u_Word
MOV BX, s_Word
ADD AX, BX

MOV EAX, u_Dword
MOV EBX, s_DWord

INVOKE ExitProcess, 0

main ENDP

END main