;// AddTwo.asm - adds two 32-bit integers.

.386
.model flat, stdcall
.stack 4096
ExitProcess proto, dwExitCode:dword

.data
val1     dword  10000h
val2     dword  40000h
val3     dword  20000h
finalVal dword ?

.code
main proc
mov		eax, val1;// start with 10000h
add		eax, val2;// add 40000h
sub		eax, val3;// subtract 20000h
mov		finalVal, eax;// store the result (30000h)
invoke	ExitProcess, 0
main endp
end main