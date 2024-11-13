#!/usr/bin/bash
#######################################################################
# Script that runs Mut.Py mutation tool on each Python file in a set of programs
#######################################################################

if (($# < 3))
then
	echo "error: 05evalTestOnMutpy.sh <project root dir> <data-file> <test-set-file>"
	echo "Example: 05evalTestOnMutpy.sh temp/lucca/python_experiments files.txt test-sets.txt"
	exit
fi

baseDir=$1
dataFile=$2
testSetFile=$3

tool=mutpy

# Iterando sobre o arquivo de test-sets
testSetData=$(cat "${baseDir}/${testSetFile}")
for tcDir in $testSetData
do
	echo "Processing test set: $tcDir"

	projectsData=$(cat "${baseDir}/${dataFile}")

	for project in $projectsData
	do
		prjArr=($(echo $project | tr ":" "\n"))
		prjDir="${prjArr[0]}"
		clazz="${prjArr[1]}"
		module="${clazz%%.*}"

		echo -e "\tProcessing program $clazz"
		cd "${baseDir}/${prjDir}"

		# Cleaning previous report
		rm -rf ./${tcDir}/${tool}
		mkdir -p ./${tcDir}/${tool}

		# Encontrando e iterando por todos os arquivos .py no diretório de testes
		pyFiles=$(find "${tcDir}" -type f -name "*.py")

		for testFile in $pyFiles
		do
			echo -e "\tProcessing test file: $testFile"
			testFileName=$(basename "$testFile" .py)

			# Creating a directory for each test file's mutpy report
			mkdir -p ./${tcDir}/${tool}/${testFileName}

			# Running mutpy for each individual Python file
			cmd="mut.py -e -m -c --debug -t ${module}.py -u ${testFile} --runner pytest --report-html ./${tcDir}/${tool}/${testFileName}"

			/usr/bin/time -o ${testFileName}.time --quiet -p $cmd >& ${testFileName}.out

			# Move the output to the respective folder for this file
			mv ${testFileName}.time ${testFileName}.out ./${tcDir}/${tool}/${testFileName}

			# Clean up __pycache__ after processing each file
			rm -rf __pycache__
			rm -rf ./${tcDir}/__pycache__
		done

		# Clean up any remaining __pycache__
		rm -rf __pycache__
		rm -rf ./${tcDir}/__pycache__
	done
done

