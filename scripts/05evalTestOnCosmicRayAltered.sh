#!/usr/bin/bash
#######################################################################
# Script that runs Cosmic.Ray mutation tool in a set of programs
#######################################################################

if (($# < 3))
then
	echo "error: 05evalTestOnCosmicRay.sh <project root dir> <data-file> <test-set-file>"
	echo "Example: 05evalTestOnCosmicRay.sh temp/lucca/python_experiments files.txt test-sets.txt"
	exit
fi

baseDir=$1
dataFile=$2
testSetFile=$3

tool=cosmic-ray

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
		mkdir ./${tcDir}/${tool}

		# Encontrando e iterando por todos os arquivos .py no diretório de testes
		pyFiles=$(find "${tcDir}" -type f -name "*.py")

		for testFile in $pyFiles
		do
			echo -e "\tProcessing test file: $testFile"
			testFileName=$(basename "$testFile" .py)

			# Creating a directory for each test file's cosmic report
			mkdir -p ./${tcDir}/${tool}/${testFileName}

			# Generating cosmic configuration file
			echo "[cosmic-ray]" > ${tcDir}/${tool}/${testFileName}/${module}.toml
			echo "module-path = \"${module}.py\"" >> ${tcDir}/${tool}/${testFileName}/${module}.toml
			echo "timeout = 600.0" >> ${tcDir}/${tool}/${testFileName}/${module}.toml
			echo "excluded-modules = []" >> ${tcDir}/${tool}/${testFileName}/${module}.toml
			echo "test-command = \"python -m pytest --tb=no ./${testFile}\"" >> ${tcDir}/${tool}/${testFileName}/${module}.toml
			echo "" >> ${tcDir}/${tool}/${testFileName}/${module}.toml
			echo "[cosmic-ray.distributor]" >> ${tcDir}/${tool}/${testFileName}/${module}.toml
			echo "name = \"local\"" >> ${tcDir}/${tool}/${testFileName}/${module}.toml

			# Running cosmic registering the time 
			#cosmic-ray new-config ${module}.toml
			cosmic-ray init ${tcDir}/${tool}/${testFileName}/${module}.toml ${tcDir}/${tool}/${testFileName}/${module}.sqlite
			cosmic-ray --verbosity INFO baseline ${tcDir}/${tool}/${testFileName}/${module}.toml >& ${tcDir}/${tool}/${testFileName}/${tool}.baseline

			# Only executes if no test errors
			if [ $? -eq 0 ]
			then 
				/usr/bin/time -o ${tcDir}/${tool}/${testFileName}/${tool}.time --quiet -p cosmic-ray exec ${tcDir}/${tool}/${testFileName}/${module}.toml ${tcDir}/${tool}/${testFileName}/${module}.sqlite >& ${tcDir}/${tool}/${testFileName}/${tool}.out
				cr-report ${tcDir}/${tool}/${testFileName}/${module}.sqlite --show-pending >& ./${tcDir}/${tool}/${testFileName}/report_cosmicray.txt
				cr-html ${tcDir}/${tool}/${testFileName}/${module}.sqlite > ./${tcDir}/${tool}/${testFileName}/report_cosmicray.html
			else 
			echo "Error on test cases. Please, check ${tool}.baseline" 
			fi

			#mv ${module}.sqlite ${tool}.time ${tool}.baseline ${tool}.out ./${tcDir}/${tool}

			rm -rf .pytest_cache
			rm -rf __pycache__
			rm -rf ./${tcDir}/__pycache__

			#Removing unfinished python -m pytest process
			pkill -f 'python -m pytest'
		done
		rm -rf .pytest_cache
		rm -rf __pycache__
		rm -rf ./${tcDir}/__pycache__

		#Removing unfinished python -m pytest process
		pkill -f 'python -m pytest'
	done
done