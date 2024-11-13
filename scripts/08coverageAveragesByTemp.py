#!/usr/bin/env python3

# Script para a geração da planilha de relatório de desempenho de mutação por ferramenta.

import sys
import os
import csv
from collections import defaultdict

def main():
    if len(sys.argv) < 4:
        print("error: averagesByTemp.py <project root dir> <data-file> <test-set-file>")
        print("Example: averagesByTemp.py python_experiments2 files.txt test-sets.txt")
        sys.exit(1)

    baseDir = sys.argv[1]
    dataFile = sys.argv[2]
    testSetFile = sys.argv[3]
    prjList = baseDir + "/" + dataFile
    testSetList = baseDir + "/" + testSetFile

    # Lista com todas as chaves possíveis de 0-0 a 1-0
    todas_chaves = [f"0-{j}" for j in range(10)] + ["1-0"]

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
            
            csv_file_path = os.path.join(prjDir, "report-coverage-ts-3-5.csv")

            # Inicializar o media_dict com todas as chaves possíveis e valores padrão (soma=0, contagem=0)
            media_dict = defaultdict(lambda: {'soma': 0, 'contagem': 0})
            for chave in todas_chaves:
                media_dict[chave]  # Garante que todas as chaves estejam no dicionário

            # Verifica se o arquivo CSV existe
            if not os.path.isfile(csv_file_path):
                print(f"Warning: {csv_file_path} not found.")
                continue
            
            with open(csv_file_path, mode='r', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                next(reader)  # Pular o cabeçalho
                
                for row in reader:
                    nome_teste = row[1]
                    valor_coluna_8 = float(row[3])  
                    chave_media = nome_teste.split('_')[2] 

                    media_dict[chave_media]['soma'] += valor_coluna_8
                    media_dict[chave_media]['contagem'] += 1

            # Criar um novo CSV para as médias
            output_file_path = os.path.join(prjDir, "coverage_average_report.csv")
            with open(output_file_path, mode='w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerow(["Temperature", "Average"])  # Cabeçalho do CSV

                # Ordenar e escrever as médias no novo arquivo
                for chave in sorted(media_dict.keys(), key=lambda x: tuple(map(int, x.split('-')))):
                    valores = media_dict[chave]
                    media = valores['soma'] / valores['contagem'] if valores['contagem'] > 0 else 0
                    writer.writerow([chave, media])

            print(f"Media report saved to {output_file_path}")

if __name__ == "__main__":
    main()
