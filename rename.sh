#!/bin/bash

dir=$1
cha=$2
pre=$3
if [ $# -ne 3 ]; then
	echo "ERROR! You need to provide three parameter"
	exit 1
else
	cd $dir
	for filename in *$cha
	do
		let total=$total+1
	done
	if [ ${#dir} -eq 1 ]; then
		echo "There are $total $cha files in current directory!"
		
		read -p "Proceed? (Y/N)" reply
		
		if [ $reply = "Y" ]; then
			
			for filename in *$cha
			do
				let num=$num+1

				if [ $num -lt 10 ]; then
					mv $filename $pre"00"$num"."$cha
				elif [[ $num -ge 10 && $num -le 100 ]]; then
					mv $filename $pre"0"$num"."$cha
				else
					mv $filename $pre$num"."$cha
				fi
			done
			echo "DONE"
		else
			exit 1
		fi
	elif [ ${#dir} -eq 2 ]; then
		echo "There are $total $cha files in parent directory!"
		read -p "Proceed? (Y/N)" reply
		if [ $reply = "Y" ]; then
			for filename in *$cha
			do 
				let num=$num+1
			
				if [ $num -lt 10 ]; then
					mv $filename $pre"00"$num"."$cha
				elif [[ $num -ge 10 && $num -le 100 ]]; then
					mv $filename $pre"0"$num"."$cha
				else
					mv $filename $pre$num"."$cha
				fi
			done
		else
			exit 1
		fi
	fi
fi
