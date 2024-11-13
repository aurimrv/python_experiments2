#!/usr/bin/bash
#######################################################################
# This script executes pynguin test generator in a set of projects
# to create test sets based on a list of supported algorithms:
# DYNAMOSA, MIO, MOSA, WHOLE_SUITE
#######################################################################
if (($# < 2))
then
	echo "error: runPynguin.sh <project root dir> <seeds.txt> [max_timeout(s)]"
	echo "Example: runPynguin.sh temp/lucca/python_experiments seeds.txt 300"
	exit
fi

baseDir=$1
seedsFile=$2
maxTimeout=300

if (($# >= 3))
then
	maxTimeout=$3
fi

# Predefined algorithms vector
algorithms=("DYNAMOSA" "MIO" "MOSA" "WHOLE_SUITE")

# Read all seeds from seeds.txt file
seeds=$(cat "$seedsFile")

projectsData=$(cat "${baseDir}/files.txt")

for algorithm in "${algorithms[@]}"
do
    echo "Running Pynguin with algorithm: $algorithm"
    for seed in $seeds
    do
        echo "Using seed: $seed"
        for project in $projectsData
        do
            prjArr=($(echo $project | tr ":" "\n"))
            prjDir="${prjArr[0]}"
            clazz="${prjArr[1]}"
            module="${clazz%%.*}"

            echo "Processing program $clazz with algorithm $algorithm and seed $seed"
            cd "${baseDir}/${prjDir}"

            mkdir -p ./$algorithm/seed_$seed
            
            pynguin --project-path ./ --output-path ./$algorithm/seed_$seed --module-name $module -v --create-coverage-report True --algorithm=$algorithm --seed $seed --maximum-search-time $maxTimeout
        done
    done
done
