.386

dtoa        MACRO  dest, source, xtra;; convert double to ASCII string

		IFB    <source>
		.ERR <missing operand(s) in DTOA>
		EXITM
		ENDIF

		IFNB   <xtra>
		.ERR <extra operand(s) in DTOA>
		EXITM
		ENDIF

		push   ebx;; save EBX
		mov    ebx, source
		push   ebx;; source parameter
		lea    ebx, dest;; destination address
		push   ebx;; destination parameter
		call   dtoaproc;; call dtoaproc(source, dest)
		pop    ebx;; restore EBX
ENDM

atod        MACRO  source, xtra;; convert ASCII string to integer in EAX
;; offset of terminating character in ESI

		IFB    <source>
		.ERR <missing operand in ATOD>
		EXITM
		ENDIF

		IFNB   <xtra>
		.ERR <extra operand(s) in ATOD>
		EXITM
		ENDIF

		lea    eax, source;; source address to EAX
		push   eax;; source parameter on stack
		call   atodproc;; call atodproc(source)
		;; parameter removed by ret
ENDM

input       MACRO  dest, length, xtra;; read string from keyboard

		IFB    <length>
		.ERR <missing operand(s) in INPUT>
		EXITM
		ENDIF

		IFNB   <xtra>
		.ERR <extra operand(s) in INPUT>
		EXITM
		ENDIF

		push   ebx;; save EBX
		lea    ebx, dest;; destination address
		push   ebx;; dest parameter on stack
		mov    ebx, length;; length of buffer
		push   ebx;; length parameter on stack
		call   inproc;; call inproc(dest, length)
		pop    ebx;; restore EBX
ENDM

output      MACRO  string, xtra;; display string

		IFB    <string>
		.ERR <missing operand in OUTPUT>
		EXITM
		ENDIF

		IFNB   <xtra>
		.ERR <extra operand(s) in OUTPUT>
		EXITM
		ENDIF

		push   eax;; save EAX
		lea    eax, string;; string address
		push   eax;; string parameter on stack
		call   outproc;; call outproc(string)
		pop    eax;; restore EAX
ENDM

intInput	MACRO	msg, dest;//User Integer Input
		output msg;//Prints a message
		push eax
		call intInputProc
		mov    dest, eax;//Stores into variable
		pop eax
ENDM

intOutput	MACRO	source;//Program Integer Output
		push eax
		mov eax, source
		call intOutputProc
		pop eax
ENDM

stringInput	MACRO	msg, dest, count;//User String Input
		output msg;//Prints a message

		push   ebx;; save EBX

		lea    ebx, dest;; destination address
		push   ebx;; dest parameter on stack
		mov    ebx, count;; length of buffer
		push   ebx;; length parameter on stack
		call   inproc;; call inproc(dest, length)

		pop    ebx;; restore EBX
ENDM
