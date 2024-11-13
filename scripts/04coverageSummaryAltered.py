#!/usr/bin/env python3

# Script para a geração da planilha de cobertura de código dos projetos.
# Assume-se que existe um diretório coverage dentro de cada projeto 
# (gerado pelo script coverageReport.sh).

import sys
import os
import re
import xml.dom.minidom

def main():
    if len(sys.argv) < 3:
        print("error: coverageSummary.py <project root dir> <data-file> <test-set>")
        print("Example: coverageSummary.py python_experiments2 files.txt test-sets.txt")
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

            prjReport = prjDir+"/report-coverage-"+testSet+".csv"
            output = open(prjReport, 'w') 
            output.write("project;test file;line coverage;branch coverage\n")

            # Nova camada de loop para acessar arquivos diferentes antes de acessar os projetos
            files_in_testset_dir = os.listdir(prjDir + "/coverage")
            
            for testFile in files_in_testset_dir:
                coverageDir = os.path.join(prjDir + "/coverage", testFile)
                #print(f"Processing test file: {coverageDir}")
                    
                isExist = os.path.exists(coverageDir)
                if (not isExist):
                    print("Error: project",prj," does not contains coverage data")
                    exit(1)
                        
                processingCoverageMetrics(prj, clazz, testFile, coverageDir, output)

            output.close()

        dados.close()

    dadosTestSets.close()

# Função para processamento dos dados sobre Complexidade
def processingCoverageMetrics(prj, clazz, testFile, coverageDir, output):
	doc = xml.dom.minidom.parse(coverageDir+"/covereageReport.xml")
	clazzes = doc.getElementsByTagName("class")
	#print("Project", prj, "Class", clazz)
	
	for c in clazzes:
		name = c.getAttribute("filename")
		print("\tProcessing",name)
		if (name == clazz):
			lineCoverage = 0
			branchCoverage = c.getAttribute("branch-rate")
			output.write("%s;%s;%.2f;%.2f\n" % (prj,testFile,float(lineCoverage)*100,float(branchCoverage)*100))
        
if __name__ == "__main__":
    main()
