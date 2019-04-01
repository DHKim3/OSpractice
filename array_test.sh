#!/bin/bash
declare -a words

while true; do
	read -p "Enter a new word: " word
	if [ $word = list ]; then
		echo ${words[*]}
	elif [ $word = quit ]; then
		echo "Exit the program"
		exit 1
	else
		words[i]=$word
		let i++
		echo "Length: "$i
	fi
done
