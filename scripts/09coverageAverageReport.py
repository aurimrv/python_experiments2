#!/usr/bin/env python3

# Script para a combinação das planilhas de relatório de desempenho de mutação por ferramenta.

import sys
import os
import csv
from collections import defaultdict

def main():
    if len(sys.argv) < 3:
        print("error: averageReport.py <project root dir> <data-file> <test-set-file>")
        print("Example: averageReport.py python_experiments2 files.txt test-sets.txt")
        sys.exit(1)

    baseDir = sys.argv[1]
    dataFile = sys.argv[2]
    testSetFile = sys.argv[3]
    prjList = baseDir + "/" + dataFile
    testSetList = baseDir + "/" + testSetFile

    dadosTestSets = open(testSetList, 'r')

    # Dicionário para armazenar valores float de cada projeto
    combined_data = defaultdict(list)

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
            
            csv_file_path = os.path.join(prjDir, "coverage_average_report.csv")
            
            # Verifica se o arquivo CSV existe
            if not os.path.isfile(csv_file_path):
                print(f"Warning: {csv_file_path} not found.")
                break
            
            with open(csv_file_path, mode='r', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)  # Pular o cabeçalho

                for row in reader:
                    # Adiciona o valor float da segunda coluna ao projeto
                    combined_data[prj].append(float(row[1]))

            # Caminho para o arquivo combinado de saída
            combined_csv_path = os.path.join(baseDir, "combined_coverage_report.csv")

            # Grava os dados combinados em um novo CSV
            with open(combined_csv_path, mode='w', newline='') as outfile:
                writer = csv.writer(outfile)
                max_len = max(len(v) for v in combined_data.values())
                # Cabeçalho
                header = ["Project"] + [f"{0}.{i}" if i < 10 else "1.0" for i in range(max(len(v) for v in combined_data.values()))]
                writer.writerow(header)

                # Dados
                for prj, values in combined_data.items():
                    row = [prj] + [f"{value:.2f}" for value in values] + ["0.00"] * (max_len - len(values))
                    writer.writerow(row)

            print(f"Combined report created at: {combined_csv_path}")

if __name__ == "__main__":
    main()