#!/usr/bin/env python3

# Script para a geração da planilha de relatório de sucesso dos testes gerados pelo LLM.

import sys
import os
import re
import csv

def main():
    if len(sys.argv) < 3:
        print("error: llm-success-report.py <project root dir> <data-file> <test-set-file>")
        print("Example: llm-success-report.py python_experiments2 files.txt test-sets.txt")
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
        prjReport = baseDir+"/report-success-llm-3-5.csv"

        dados = open(prjList, 'r')
        output = open(prjReport, 'w') 
    

        output.write("filename;0.0;0.1;0.2;0.3;0.4;0.5;0.6;0.7;0.8;0.9;1.0;total\n")

        for x in dados:
            x = x.strip()
            info = x.split(':')
            prj = info[0]
            clazz = info[1]
            
            prjDir = baseDir + "/" + prj
            
            isExist = os.path.exists(prjDir)
            if (not isExist):
                print("Error: project",prj," does not contains success data")
                exit(1)
                
            processingSuccessMetrics(prj, clazz, prjDir, output)

        dados.close()
        output.close()
    dadosTestSets.close()

def processingSuccessMetrics(prj, testFile, prjDir, output):
    reportFile = prjDir+"/file_counts_3-5_by_temperature.csv"
    with open(reportFile, mode='r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            next(reader)  # Pular o cabeçalho
            
            percentages = []
            istotal = 0
            
            for row in reader:
                value = int(row[1])
                
                if (istotal == 11):
                    total_percentage = value / 330 * 100
                else:
                    percentage_by_temp = value / 30 * 100
                    percentages.append(f"{percentage_by_temp:.2f}")
                    istotal += 1
            
            output.write(f"{testFile};" + ";".join(percentages) + f";{total_percentage:.2f}\n")
        
if __name__ == "__main__":
    main()