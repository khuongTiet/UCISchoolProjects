;// Lab 9(Lab9.asm)

;// Program Description:
;// Author:
;// Creation Date:
;// Revisions:
;// Date:              Modified by:

;// Define a structure for a linked list node that contains an integer value, 
;// and a pointer to the next node in the list

;// Create a global variable that represents the head of the linked list
;// Create five additional nodes in the data area to be added into the list later
;//  NOTE: our final lab will extend this program to dynamically allocate nodes

Node STRUCT
	nodeValue DWORD ?
	ptrNext DWORD ?
Node ENDS


;// Write a function: DISPLAY_MENU that:
;// * Displays a menu of user choices(as shown below)
;//        1) Insert a node
;//        2) Delete a node
;//        3) Print the list
;//        4) Exit program
;// * Validates the user's input (1-4)
;// * If invalid, prints an error message and requests new input
;// * Returns the user's choice

;// Write a function: PRINT_LIST that:
;// * Passed the head pointer to a list, will print the integer value 
;//   of each node in the list on a separate line
;// * If the list is empty, prints a "List is Empty" message 

;// Write a function: INSERT_NODE that:
;// * Passed the head pointer to a list, the node & the value to be inserted
;// * Will insert the new node at the head of the list

;// Write a function: DELETE_NODE that:
;// * Passed the head pointer to a list, & the value of the node to be removed
;// * Will search the list for the node to delete
;//       if not found : prints "Not found" message
;//       if found: remove from list and print "Node removed" message



.386 
.model flat, stdcall
.stack 4096

ExitProcess PROTO, dwExitCode : DWORD
include io_asm.h


.DATA

;//DATA DEFINITIONS HERE

integerInput DWORD ? 
inputIntMessage BYTE "Enter an integer: ", 0
ErrorMessage BYTE 0dh, 0ah, "ERROR: Invalid input. Re-enter an integer", 0dh, 0ah, 0
EmptyList BYTE 0dh, 0ah, "List is Empty", 0dh, 0ah, 0


MenuOutput1 BYTE 0dh, 0ah, "1) Insert a node", 0dh, 0ah, 0
MenuOutput2 BYTE "2) Delete a node", 0dh, 0ah, 0
MenuOutput3 BYTE "3) Print the list", 0dh, 0ah, 0
MenuOutput4 BYTE "4) Exit program", 0dh, 0ah, 0dh, 0ah, 0


displayOutput DWORD ?

LinkedList Node 5 DUP(<0,0>)
head Node <0,Node PTR LinkedList[0]>

checkNode Node <0,0>


.CODE

;//FUNCTION PROTOTYPES

PRINT_LIST PROTO, headNode: Node
INSERT_NODE PROTO,  headNode: Node, insert:PTR Node, int_value: DWORD

	
main PROC

;// MAIN PROCEDURE IMPLEMENTATION

;// Implement functionality to allow user to 
;// loop through adding, deleting & printing nodes
;// in a list. 
;// Implement any additional I/O operations to 
;// print prompts & receive values from users as necessary

display:
	call DISPLAY_MENU
	;intOutput displayOutput
	mov eax, displayOutput
	cmp eax, 1
	je insertNode
	cmp eax, 2
	je deleteNode
	cmp eax, 3
	je printNode
	cmp eax, 4
	je exitProgram


insertNode:
	intInput inputIntMessage, integerInput
	mov eax, integerInput
	mov edi, 0
	mov (Node PTR LinkedList[edi]).nodeValue, eax
	INVOKE INSERT_NODE, head, ADDR LinkedList[edi].nodeValue,eax
	add edi, TYPE Node
	jmp display

deleteNode:
	jmp display

printNode:
	INVOKE PRINT_LIST, head
	jmp display

exitProgram:
	jmp finish

finish:

INVOKE ExitProcess, 0

main ENDP

;//FUNCTION IMPLEMENTATIONS

DISPLAY_MENU PROC
	push eax

	output MenuOutput1
	output MenuOutput2
	output MenuOutput3
	output MenuOutput4

	prompt:
		intInput inputIntMessage, integerInput
		mov eax, integerInput
		cmp eax, 4
		jle nextCheck
		jg reprompt

	nextCheck:
		cmp eax, 1
		jge return
		jl reprompt

	reprompt:
		output ErrorMessage
		jmp prompt

	return:
		mov displayOutput, eax
		pop eax
		ret 

DISPLAY_MENU ENDP

PRINT_LIST PROC,
    headNode: Node

    push eax
    push esi

	working:
		mov esi, headNode.ptrNext
		mov eax, [esi]
		cmp eax, 0
		je printFail
		jmp print

	printFail:
		output EmptyList
		pop esi
		pop eax
		ret

	print:
		intOutput eax
		

    pop eax
    pop ebx
    ret


PRINT_LIST ENDP

INSERT_NODE PROC,
    headNode: Node, insert:PTR Node, int_value: DWORD

    push eax
	push ebx
	push edx
	push esi
	
	mov eax, int_value
	mov headNode.nodeValue, eax
	mov ebx, insert
	mov headNode.ptrNext, ebx

	pop esi
	pop edx
	pop ebx
    pop eax
    ret
INSERT_NODE ENDP


; *************** setup for Win32 I / O ****************

STD_OUTPUT EQU - 11
STD_INPUT  EQU - 10

GetStdHandle PROTO NEAR32 stdcall, nStdHandle:DWORD

ReadFile PROTO NEAR32 stdcall, hFile : DWORD, lpBuffer : NEAR32, nNumberOfCharsToRead : DWORD,
lpNumberOfBytesRead : NEAR32, lpOverlapped : NEAR32

					  WriteFile PROTO NEAR32 stdcall, hFile : DWORD, lpBuffer : NEAR32, nNumberOfCharsToWrite : DWORD,
				  lpNumberOfBytesWritten : NEAR32, lpOverlapped : NEAR32

										   ;;//DATA SEGMENT
.DATA
written    DWORD ?
read       DWORD ?
strAddr    DWORD ?
strLength  DWORD ?
hStdOut    DWORD ?
hStdIn     DWORD ?
RegValue    BYTE	12 DUP(0)
EAX_str		BYTE	"EAX: ", 0
EBX_str		BYTE	"EBX: ", 0
ECX_str		BYTE	"ECX: ", 0
EDX_str		BYTE	"EDX: ", 0
newline     BYTE    0dh, 0ah, 0
inputValue	BYTE   16 DUP(0)

.CODE

; itoaproc(source, dest)
; convert integer(source) to string of 6 characters at given destination address
itoaproc    PROC   NEAR32
push   ebp; save base pointer
mov    ebp, esp; establish stack frame
push   eax; Save registers
push   ebx;   used by
push   ecx;   procedure
push   edx
push   edi
pushf; save flags

mov    ax, [ebp + 12]; first parameter(source integer)
mov    edi, [ebp + 8]; second parameter(dest offset)
ifSpecial:  cmp    ax, 8000h; special case -32, 768 ?
			jne    EndIfSpecial; if not, then normal case
			mov    BYTE PTR[edi], '-'; manually put in ASCII codes
			mov    BYTE PTR[edi + 1], '3';   for - 32, 768
			mov    BYTE PTR[edi + 2], '2'
			mov    BYTE PTR[edi + 3], '7'
			mov    BYTE PTR[edi + 4], '6'
			mov    BYTE PTR[edi + 5], '8'
			jmp    ExitIToA; done with special case
		EndIfSpecial:
mov    dx, ax; save source number
mov    al, ' '; put blanks in
mov    ecx, 5;   first five
cld;   bytes of
rep stosb;   destination field

mov    ax, dx; copy source number
mov    cl, ' '; default sign(blank for + )
IfNeg:      cmp    ax, 0; check sign of number
			jge    EndIfNeg; skip if not negative
			mov    cl, '-'; sign for negative number
			neg    ax; number in AX now >= 0
		EndIfNeg:
mov    bx, 10; divisor

WhileMore : mov    dx, 0; extend number to doubleword
			div    bx; divide by 10
			add    dl, 30h; convert remainder to character
			mov[edi], dl; put character in string
			dec    edi; move forward to next position
			cmp    ax, 0; check quotient
			jnz    WhileMore; continue if quotient not zero

			mov[edi], cl; insert blank or "-" for sign

		ExitIToA : popf; restore flags and registers
				   pop    edi
				   pop    edx
				   pop    ecx
				   pop    ebx
				   pop    eax
				   pop    ebp
				   ret    6; exit, discarding parameters
itoaproc    ENDP

; dtoaproc(source, dest)
; convert double(source) to string of 11 characters at given offset in DS(dest)
dtoaproc    PROC   NEAR32
push   ebp; save base pointer
mov    ebp, esp; establish stack frame
push   eax; Save registers
push   ebx;   used by
push   ecx;   procedure
push   edx
push   edi
pushf; save flags

mov    eax, [ebp + 12]; first parameter(source double)
mov    edi, [ebp + 8]; second parameter(dest addr)
ifSpecialD: cmp    eax, 80000000h; special case -2, 147, 483, 648 ?
			jne    EndIfSpecialD; if not, then normal case
			mov    BYTE PTR[edi], '-'; manually put in ASCII codes
			mov    BYTE PTR[edi + 1], '2';   for - 2, 147, 483, 648
			mov    BYTE PTR[edi + 2], '1'
			mov    BYTE PTR[edi + 3], '4'
			mov    BYTE PTR[edi + 4], '7'
			mov    BYTE PTR[edi + 5], '4'
			mov    BYTE PTR[edi + 6], '8'
			mov    BYTE PTR[edi + 7], '3'
			mov    BYTE PTR[edi + 8], '6'
			mov    BYTE PTR[edi + 9], '4'
			mov    BYTE PTR[edi + 10], '8'
			jmp    ExitDToA; done with special case
		EndIfSpecialD:

mov    edx, eax; save source number

mov    al, ' '; put blanks in
mov    ecx, 10;   first ten
cld;   bytes of
rep stosb;   destination field

mov    eax, edx; copy source number
mov    cl, ' '; default sign(blank for + )
IfNegD:     cmp    eax, 0; check sign of number
			jge    EndIfNegD; skip if not negative
			mov    cl, '-'; sign for negative number
			neg    eax; number in EAX now >= 0
		EndIfNegD:

mov    ebx, 10; divisor

WhileMoreD : mov    edx, 0; extend number to doubleword
			 div    ebx; divide by 10
			 add    dl, 30h; convert remainder to character
			 mov[edi], dl; put character in string
			 dec    edi; move forward to next position
			 cmp    eax, 0; check quotient
			 jnz    WhileMoreD; continue if quotient not zero

			 mov[edi], cl; insert blank or "-" for sign

		 ExitDToA : popf; restore flags and registers
					pop    edi
					pop    edx
					pop    ecx
					pop    ebx
					pop    eax
					pop    ebp
					ret    8; exit, discarding parameters
					dtoaproc    ENDP


					; atodproc(source)
					; Procedure to scan data segment starting at source address, interpreting
					; ASCII characters as an integer value which is returned in EAX.
					; Leading blanks are skipped.A leading - or + sign is acceptable.
					; Digit(s) must immediately follow the sign(if any).
					; Memory scan is terminated by any non - digit, and the address of
					; the terminating character is in ESI.
					; The following flags are affected :
;   AC is undefined
;   PF, SF and ZF reflect sign of number returned in EAX.
;   CF reset to 0
;   OF set to indicate error.Possible error conditions are :
;     -no digits in input
;     -value outside range - 2, 147, 483, 648 to 2, 147, 483, 647
;   (EAX)will be 0 if OF is set.
atodproc    PROC   NEAR32
		push   ebp; save base pointer
		mov    ebp, esp; establish stack frame
		sub    esp, 4; local space for sign
		push   ebx; Save registers		
		push   ecx
		push   edx
		pushf; save flags

		mov    esi, [ebp + 8]; get parameter(source addr)

		WhileBlankD:cmp    BYTE PTR[esi], ' '; space ?
			jne    EndWhileBlankD; exit if not
			inc    esi; increment character pointer
			jmp    WhileBlankD; and try again
		EndWhileBlankD :
			mov    eax, 1; default sign multiplier
		IfPlusD : cmp    BYTE PTR[esi], '+'; leading + ?
		  je     SkipSignD; if so, skip over
		IfMinusD : cmp    BYTE PTR[esi], '-'; leading - ?
				 jne    EndIfSignD; if not, save default +
				 mov    eax, -1; -1 for minus sign
		SkipSignD : inc    esi; move past sign
		EndIfSignD :
			mov[ebp - 4], eax; save sign multiplier
			mov    eax, 0; number being accumulated
			mov    cx, 0; count of digits so far

		WhileDigitD : cmp    BYTE PTR[esi], '0'; compare next character to '0'
			  jl     EndWhileDigitD; not a digit if smaller than '0'
			  cmp    BYTE PTR[esi], '9'; compare to '9'
			  jg     EndWhileDigitD; not a digit if bigger than '9'
			  imul   eax, 10; multiply old number by 10
			  jo     overflowD; exit if product too large
			  mov    bl, [esi]; ASCII character to BL
			  and    ebx, 0000000Fh; convert to single - digit integer
			  add    eax, ebx; add to sum
			  jc     overflowD; exit if sum too large
			  inc    cx; increment digit count
			  inc    esi; increment character pointer
			  jmp    WhileDigitD; go try next character
		  EndWhileDigitD :		

			cmp    cx, 0; no digits ?
			jz     overflowD; if so, set overflow error flag

			; if value is 80000000h and sign is '-', want to return 80000000h (-2 ^ 32)

			cmp    eax, 80000000h; 80000000h ?
			jne    TooBigD
			cmp    DWORD PTR[ebp - 4], -1; multiplier - 1 ?
			je     ok1D; if so, return 8000h

			TooBigD: test   eax, eax; check sign flag
			jns    okD; will be set if number > 2 ^ 32 - 1

	 overflowD:  pop    ax; get flags
				 or     ax, 0000100001000100B; set overflow, zero & parity flags
				 and    ax, 1111111101111110B; reset sign and carry flags
				 push   ax; push new flag values
				 mov    eax, 0; return value of zero
				 jmp    AToDExit; quit

	 okD : imul   DWORD PTR[ebp - 4]; make signed number
	ok1D : popf; get original flags
					  test   eax, eax; set flags for new number
					  pushf; save flags

	AToDExit : popf; get flags
			 pop    edx; restore registers
			 pop    ecx
			 pop    ebx
			 mov    esp, ebp; delete local variable space
			 pop    ebp
			 ret    4; exit, removing parameter
 atodproc    ENDP

 ; outproc(source)
 ; Procedure to display null - terminated string
 ; No registers are changed; flags are not affected.

 outproc     PROC   NEAR32
			push   ebp; save base pointer
			mov    ebp, esp; establish stack frame
			pushad
			pushfd; save flags

			mov    esi, [ebp + 8]; source address
			mov    strAddr, esi
			; find string length
			mov    strLength, 0; initialize string length
		 WhileChar : cmp    BYTE PTR[esi], 0; character = null ?
					 jz     EndWhileChar; exit if so
					 inc    strLength; increment character count
					 inc    esi; point at next character
					 jmp    WhileChar
		 EndWhileChar :
			INVOKE GetStdHandle, ; get handle for console output
					STD_OUTPUT
			mov    hStdOut, eax

			INVOKE WriteFile,
				hStdOut, ; file handle for screen
				strAddr, ; address of string
				strLength, ; length of string
				NEAR32 PTR written, ; bytes written
				0; overlapped mode

			popfd; restore flags
			popad; restore registers
			pop    ebp
			ret    4; exit, discarding parameter
outproc     ENDP

; inproc(dest, length)
; Procedure to input a string from keyboard.
; The string will be stored at the address given by dest.
; The length parameter gives the size of the user's buffer.  It is assumed 
; that there will be room for the string and a null byte.
; The string will be terminated by a null character(00h).
; Flags are unchanged.
inproc      PROC   NEAR32
			push   ebp; save base pointer
			mov    ebp, esp; establish stack fr			ame
			pushad; save all registers
			pushfd; save flags

			INVOKE GetStdHandle, ; get handle for console
			STD_INPUT
			mov    hStdIn, eax

			mov    ecx, [ebp + 8]; string length
			mov    strLength, ecx

			mov    esi, [ebp + 12]; source address
			mov    strAddr, esi

			INVOKE ReadFile,
			hStdIn, ; file handle for keyboard
			strAddr, ; address of string
			strLength, ; length of string
			NEAR32 PTR read, ; bytes read
			0; overlapped mode

			mov    ecx, read; number of bytes read
			mov    BYTE PTR[esi + ecx - 2], 0; replace CR / LF by trailing null

			popfd; restore flags
			popad; restore registers
			pop    ebp
			ret    8; exit, discarding parameters
inproc      ENDP


intOutputProc      PROC   NEAR32
push   ebx;; save EBX
mov    ebx, EAX
push   ebx;; source parameter
lea    ebx, RegValue;; destination address
push   ebx;; destination parameter
call   dtoaproc;; call dtoaproc(source, dest)
pop    ebx;; restore EBX

push   eax;; save EAX
lea    eax, RegValue;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

push   eax;; save EAX
lea    eax, newline;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX
ret
intOutputProc      ENDP

; printRegisters
; Procedure to print registers to the screen.
; Prints EAX, EBX, ECX, and EDX
printRegisters    PROC   NEAR32
push   ebp		; save base pointer
mov    ebp, esp ; establish stack frame
pushad			; save all registers
pushfd			; save flags

push   eax;; save EAX
lea    eax, EAX_str;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

; dtoa RegValue, EAX
push   ebx;; save EBX
mov    ebx, EAX
push   ebx;; source parameter
lea    ebx, RegValue;; destination address
push   ebx;; destination parameter
call   dtoaproc;; call dtoaproc(source, dest)
pop    ebx;; restore EBX


push   eax;; save EAX
lea    eax, RegValue;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

push   eax;; save EAX
lea    eax, newline;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX


push   eax;; save EAX
lea    eax, EBX_str;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

;			dtoa RegValue, EBX
push   ebx;; save EBX
mov    ebx, EBX
push   ebx;; source parameter
lea    ebx, RegValue;; destination address
push   ebx;; destination parameter
call   dtoaproc;; call dtoaproc(source, dest)
pop    ebx;; restore EBX

push   eax;; save EAX
lea    eax, RegValue;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

push   eax;; save EAX
lea    eax, newline;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

push   eax;; save EAX
lea    eax, ECX_str;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

; dtoa RegValue, ECX
push   ebx;; save EBX
mov    ebx, ECX
push   ebx;; source parameter
lea    ebx, RegValue;; destination address
push   ebx;; destination parameter
call   dtoaproc;; call dtoaproc(source, dest)
pop    ebx;; restore EBX

push   eax;; save EAX
lea    eax, RegValue;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

push   eax;; save EAX
lea    eax, newline;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

push   eax;; save EAX
lea    eax, EDX_str;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

push   ebx;; save EBX
mov    ebx, EDX
push   ebx;; source parameter
lea    ebx, RegValue;; destination address
push   ebx;; destination parameter
call   dtoaproc;; call dtoaproc(source, dest)
pop    ebx;; restore EBX

push   eax;; save EAX
lea    eax, RegValue;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

push   eax;; save EAX
lea    eax, newline;; string address
push   eax;; string parameter on stack
call   outproc;; call outproc(string)
pop    eax;; restore EAX

popfd; restore flags
popad; restore registers
pop    ebp
ret    ; exit
printRegisters    ENDP

intInputProc	PROC	NEAR32
push   ebp; save base pointer
mov    ebp, esp; establish stack frame

; input  inputValue, 16;//Converts ascii input

push   ebx;; save EBX

lea    ebx, inputValue;; destination address
push   ebx;; dest parameter on stack
mov    ebx, 16;; length of buffer
push   ebx;; length parameter on stack
call   inproc;; call inproc(dest, length)

pop    ebx;; restore EBX


; atod   inputValue
lea    eax, inputValue;; source address to EAX
push   eax;; source parameter on stack
call   atodproc;; call atodproc(source)

pop   ebp; restore base pointer

ret; exit, discarding parameters
intInputProc	ENDP


END main