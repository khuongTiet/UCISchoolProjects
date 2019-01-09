;// Program Template(Template.asm)

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
; declare variables here

.code
main PROC

.code
; instructions here

INVOKE ExitProcess, 0

main ENDP

; (insert additional procedures here)

END main
