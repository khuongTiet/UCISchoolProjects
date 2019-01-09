#!/bin/sh
# A simple script that utilizes the options in ls to sort and list the files by size

# lss is a script that is able to handle a multitude of options passed onto it. All options passed to lss are passed onwards to ls.
# With the exception of certain options, all options will be directly passed into ls, at the end of a -lS option

# The SHORT options that are not accepted and their reasonings are:
#    OPTION	 |      REASON
# -------------------------------------------------------------------------------------------------------------------
#	c		sorts by name, and/or by time if used with -lt (which is never the case in this script)
# 	f		disables sorting
#	r		reverses order of the sorting performed
#	t		sorts by time instead of file size
#	u		sorts by access time, and/or sorts if used with -lt (which is never the case in this script)
#	U		does not sort output of -l
#	v		sorts by version number instead of file size
#	X		sorts alphabetically instead of by file size

# The LONG options that are not accepted and their reasonings are:
#    	OPTION			   |	REASON
# -------------------------------------------------------------------------------------------------------------------
#	group-directories-first		Affects the sorted output
#	reverse				reverses sorting order
#	sort				sorts by name and not file size
#	time		

# String used to store all the options that ls will take on in addition to the default -l and -S options
# This string may potentially contain long options in addition to short ones
user_options=""

# String used to store all long options. Long options are added with a space at the end of them to account for additional long options being appended into the string
long_options=""

# getopts is used to parse through the options for a simple and clean implementation
# It utilizes a while loop and a spec string to specify which options can be taken by the script
while getopts 'aAbBcdDfFgGhHklLmnNopqQrRsStT:uUvw:xX1-:' OPTION; do
	# Parse through each valid option as declared in the above line
	case "$OPTION" in
		-)								
			# LONG OPTIONS HANDLING:
			# As a result of getopts not having a built in option to handle long options, this is a work around that makes use of how long options
			# are generally formatted.
			# We first check for a regular option that contains two '-' characters, as all long options do
			# We then use this option's argument (whatever follows the -) in order to parse as a long option
			# For long options that do not take any extra arguments, the script will either:
			# 	-Pass the short option version of it into the user_options string
			#	-Append the option into the long_options string
			# For long options that do take an additional argument, the script will:
			#	-Take the argument of the long option through use of the OPTIND argument position indicator
			#	-Increment the OPTIND position to account for any additional arguments
			#	-Append to the long_options string the option and its argument
			
			case "${OPTARG}" in					# OPTARG is the argument of the option that getopts parses, in this case it is the rest of the long option
				all)
					user_options+="a";;
				almost-all)
					user_options+="A";;
				author)
					long_options+="--author ";;
				escape)
					user_options+="b";;
				block-size)
					arg="${!OPTIND}";			# Get argument of long option if it exists
					OPTIND=$(($OPTIND + 1))			# Move the current argument position on to account for later arguments
					long_options+="--block-size=$arg ";;	# Append to long options string with space to account for additional ones
				color)
					arg="${!OPTIND}";
					OPTIND=$(($OPTIND + 1))
					if [[ ! "$arg" =~ ^(never|auto|always)$ ]]; then
						if [[ -z $arg ]]; then
							long_options+="--color "
						else
							echo "lss: --color error -- '$arg' is not a valid argument'"
							exit 1
						fi
					else
						long_options+="--color=$arg "
					fi;;
				ignore-backups)
					user_options+="B";;	
				directory)
					user_options+="d";;
				dired)
					user_options+="D";;
				classify)
					user_options+="F";;
				file-type)
					long_options+="--filetype ";;		# Simply append to long_options because it takes no arguments
				format)
					arg="${!OPTIND}";
					OPTIND=$(($OPTIND + 1))
					long_options+="--format=$arg ";;
				full-time)
					long_options+="--full-time ";;
				no-group)
					user_options+="G";;
				human-readable)
					user_options+="h";;
				si)
					long_options+="--si ";;
				dereference-command-line)
					user_options+="H";;
				dereference-commnad-line-symlink-to-dir)
					long_options+="--${OPTARG} ";;
				hide)
					arg="${!OPTIND}";
					OPTIND=$(($OPTIND + 1))
					long_options+="--hide=$arg ";;
				indicator-style)
					arg="${!OPTIND}";
					OPTIND=$((OPTIND + 1))
					if [[ ! "${arg}" =~ ^(none|slash|file-type|classify)$ ]]; then
						echo "lss: --indicator-style error -- '$arg' is not a valid argument"
						exit 1
					else
						long_options+="--indicator-style=$arg "
					fi;;
				inode)
					long_options+="--inode ";;
				ignore)
					arg="${!OPTIND}";
					OPTIND=$(($OPTIND + 1))
					long_options+="--ignore=$arg ";;
				kibibytes)
					user_options+="k";;
				dereference)
					user_options+="L";;
				numeric-uid-gid)
					user_options+="n";;
				literal)
					user_options+="N";;
				hide-control-chars)
					user_options+="q";;
				show-control-chars)
					long_options+="--${OPTARG} ";;
				quote-name)
					user_options+="Q";;
				quoting-style)
					arg="${!OPTIND}";
					OPTIND=$(($OPTIND + 1))
					if [[ ! "${arg}" =~ ^(literal|locale|shell|shell-always|c|escape)$ ]]; then
						echo "lss: --quoting-style error -- '$arg' is not a valid argument"
						exit 1
					else
						long_options+="--quoting-style=$arg "
					fi;;
				recursive)
					user_options+="R";;
				size)
					long_options+="--size ";;
				time)
					arg="${!OPTIND}";
					OPTIND=$(($OPTIND + 1))
					if [[ ! "${arg}" =~ ^(atime|access|use|ctime|status)$ ]]; then
						echo "lss: --time error: '$arg' is not a valid argument"
						exit 1
					else
						long_options+="--time=$arg "
					fi;;
				tabsize)
					arg="${!OPTIND}";
					OPTIND=$(($OPTIND + 1))
					if [[ "${arg}" =~ ^[0-9]+$ ]]; then
						long_options+="--tabsize=$arg "
					else
						echo "lss: --tabsize error -- '$arg' is not a valid argument"
						exit 1
					fi;;
				width)
					arg="${!OPTIND}";
					OPTIND=$(($OPTIND + 1))
					if [[ "${arg}" =~ ^[0-9]+$ ]]; then
						long_options+="--width=$arg "
					else
						echo "lss: --width error -- '$arg' is not a valid argument"
						exit 1
					fi;;
				# Ignore all other long options passed 
				*)
					echo "lss: Long option '${OPTARG}' is not supported, exiting"
					exit 1;;
			esac;;
		# SHORT OPTION HANDLING:
		# Short options have a much simpler execution case, this script will either:
		#	-Ignore the option and present an error message
		#	-Pass the option directly to ls -lS by appending it to the user_options string
		
		# Options that are not supported in lss since they affect the sorting order of the output
		[cfrtuUvX])						
			echo "lss: Option '"$OPTION"' not compatible with lss"	# Give error message
			exit 1							# End shell execution early
			;;
		T)
			arg=${OPTARG}
			long_options+="-T $arg";;
		w)
			arg=${OPTARG}
			long_options+="-w $arg";;
		# All other options in the specified string will get handled the same way, directly passed on to ls
		?)
			user_options+="$OPTION"
			;;
	esac
done
# Move current argument position in order to allow for handling of non-option arguments
# This is to account for parsing through the options with getopts
shift "$((OPTIND - 1))"
# Handle long options due to their different formatting
# If there are long options (if long_options is not an empty string), append the long options into the user_options string
if [[ ! -z $long_options ]]; then
	user_options+=" ${long_options::-1}"					# Append to user_options, add long_options and remove last character " "
fi
# Pass all options into ls
ls -lS$user_options "$@"
