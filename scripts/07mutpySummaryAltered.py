#!/usr/bin/env python3

# Script para a geração da planilha de relatório de mutantes para a MutPy.
# Assume-se que existe um arquivo de relatório html gerado pela ferramenta.

import sys
import os
import re

def main():
    if len(sys.argv) < 3:
        print("error: mutpySummary.py <project root dir> <data-file> <test-set-file>")
        print("Example: mutpySummary.py python_experiments2 files.txt test-sets.txt")
        sys.exit(1)

    baseDir = sys.argv[1]
    dataFile = sys.argv[2]
    testSetFile = sys.argv[3]
    prjList = baseDir+"/"+dataFile
    testSetList = baseDir+"/"+testSetFile

    dadosTestSets = open(testSetList, 'r')

    for testSet in dadosTestSets:
        testSet = testSet.strip()
        print("Processing test set: ", testSet)
        
        dados = open(prjList, 'r')
        
        for x in dados:
            x = x.strip()
            info = x.split(':')
            prj = info[0]
            clazz = info[1]
            
            print(f"Processing project: {prj}")
            prjDir = baseDir + "/" + prj + "/" + testSet

            prjReport = prjDir+"/report-mutpy-"+testSet+".csv"
            output = open(prjReport, 'w') 
            output.write("project;test file;mutants;killed;incompetent;timeout;survived;mutation score\n")

            # Nova camada de loop para acessar arquivos diferentes antes de acessar os projetos
            files_in_testset_dir = os.listdir(prjDir + "/mutpy")
            
            for testFile in files_in_testset_dir:
                mutpyDir = os.path.join(prjDir + "/mutpy", testFile)
                #print(f"Processing test file: {mutpyDir}")
                    
                isExist = os.path.exists(mutpyDir)
                if (not isExist):
                    print("Error: project",prj," does not contains mutpy data")
                    exit(1)
                        
                processingMutpyMetrics(prj, testFile, mutpyDir, output)

            output.close()

        dados.close()

    dadosTestSets.close()

def processingMutpyMetrics(prj, testFile, mutpyDir, output):
    reportFile = mutpyDir + "/index.html"
    with open(reportFile, 'r') as f:
        for linha in f:
            matchKilled = re.search(r'killed - (\d+)', linha)
            if matchKilled:
                killedMutants = int(matchKilled.group(1))

            matchSurviving = re.search(r'survived - (\d+)', linha)
            if matchSurviving:
                survivingMutants = int(matchSurviving.group(1))

            matchIncompetent = re.search(r'incompetent - (\d+)', linha)
            if matchIncompetent:
                incompetentMutants = int(matchIncompetent.group(1))

            matchTimeout = re.search(r'timeout - (\d+)', linha)
            if matchTimeout:
                timeoutMutants = int(matchTimeout.group(1))

        totalMutants = killedMutants + survivingMutants + incompetentMutants + timeoutMutants
        mutationScore = ((killedMutants+incompetentMutants+timeoutMutants)/totalMutants)*100
        output.write("%s;%s;%d;%d;%d;%d;%d;%.2f\n" % (prj,testFile,totalMutants,killedMutants, incompetentMutants, timeoutMutants, survivingMutants, mutationScore))
        
if __name__ == "__main__":
    main()