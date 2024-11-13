#!/usr/bin/bash

if (($# < 1))
then
	echo "error: parsePynguinRunAll.sh <project root dir>"
	echo "Example: parsePynguinRunAll.sh temp/lucca/python_experiments"
	exit
fi

baseDir=$1
scriptDir=$1
algorithm1="DYNAMOSA"
algorithm2="MOSA"
algorithm3="MIO"
algorithm4="WHOLE_SUITE"

./01parsePynguin.sh $baseDir $algorithm1
./01parsePynguin.sh $baseDir $algorithm2
./01parsePynguin.sh $baseDir $algorithm3
./01parsePynguin.sh $baseDir $algorithm4