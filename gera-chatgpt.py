import sys
import os
import requests
import re
from openai import OpenAI
import datetime
import subprocess
import csv

def read_python_files(folder_path):
    print(f"Lendo códigos fonte {clazz} \n")
    python_files = []
    for file_name in os.listdir(folder_path):
        if (file_name == f"{clazz}"):
            file_path = os.path.join(folder_path, file_name)
            with open(file_path, "r") as file:
                text = file.read()
                python_files.append(f"```{text}```")
    return python_files
    

def request_test_generation(messages, temperature):
    # API_KEY must be set in an environment variable called OPENAI_API_KEY"
    # export OPENAI_API_KEY=<<your-key>>
    client = OpenAI()

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      #model="gpt-4o",
      #model="gpt-4-turbo",
      temperature=temperature,
      messages=messages
    )

    content = completion.choices[0].message.content

    print(f"Request success: {clazz}\n")
    return content


def extract_code(code, clazz, n, only_code):
    code_blocks = []
    is_code = only_code

    lines = code.split("\n")
    for line in lines:
        if "```" in line:
            is_code = not is_code
        elif is_code:
            code_blocks.append(line)
    
    extracted_code = "\n".join(code_blocks)
    return extracted_code

def remove_other_test_classes(code, clazz, n):
    if "```" in code:
        return extract_code(code, clazz, n, False)
    else:
        return extract_code(code, clazz, n, True)
        
def generate_tests(code, temperature, n):
    message_path_import = "module_dir = os.path.dirname(os.path.abspath(__file__)); project_dir = os.path.abspath(os.path.join(module_dir, '..')); sys.path.append(project_dir)"
    
    messages = [
        {"role": "system", "content": "You are a senior software tester specialized in mutation testing."},
        {"role": "user", "content": f"I am using mutation testing on the Python code below. I want to create tests that cover every module of the code. Do not leave any method untested. Give me more than one test per method. As a senior software tester, give me a set of test cases on the Pytest format. Correctly import the file {clazz} and its modules being tested, utilize {message_path_import} to correctly import the file. Please, no additional information. Just the test cases. \n\n{code}"}
    ]
    generated_tests = request_test_generation(messages, temperature)
    generated_tests = remove_other_test_classes(generated_tests, clazz, n)
    return generated_tests, messages

def get_test_path(prj, model, clazz, number):
    return os.path.join(".", prj, f"ts-{model}", f"test_{model}_{temperature_string}_{number}.py")

def set_temperature(i):
    if(i <= 3): return 0.0
    if(i <= 6): return 0.1
    if(i <= 9): return 0.2
    if(i <= 12): return 0.3
    if(i <= 15): return 0.4
    if(i <= 18): return 0.5
    if(i <= 21): return 0.6
    if(i <= 24): return 0.7
    if(i <= 27): return 0.8
    if(i <= 30): return 0.9
    return 1.0

def transform_temperature(temperature):
    temperature = int(temperature*10)
    if temperature == 1.0:
        return "1-0"
    else:
        return "0-" + str(temperature)

def compile_and_test(file_path):
    try:
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        if result.stderr:   
            return result.stderr  
    except Exception as e:
        return str(e)  
    return None  

def feed_error_to_api(generated_tests, error_message, clazz, n, temperature):
    messages = [
        {"role": "user", "content": f"The following error was encountered when executing the test code for the file {clazz}. Return me the full test set with the necessary corrections based on the error message. \n\n Tests: {generated_tests} \n\nError Message: {error_message}"}
    ]
    print(messages)
    corrected_tests = request_test_generation(messages, temperature)
    corrected_tests = remove_other_test_classes(generated_tests, clazz, n)
    return corrected_tests, messages

def run_pytest_and_check(prj, number):
    test_path = os.path.join(".", f"ts-{model}", f"test_{model}_{temperature_string}_{number}.py")
    result = subprocess.run(['pytest', test_path, '--disable-warnings', '-q', '--tb=short'], capture_output=True, text=True, cwd=prj)
    if result.returncode != 0:
        print(f"Pytest stdout:\n{result.stdout}")
        return result.stdout
    return None

def record_failed_tests(prj, model, clazz, number, failed_tests_count):
    failed_tests_path = os.path.join(".", prj, f"failed_tests_{model}.csv")
    with open(failed_tests_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"test_{model}_{temperature_string}_{number}.py", failed_tests_count])

if len(sys.argv) < 1:
    print("error: gera-chatgpt.py")
    print("Example: gera-chatgpt.py")
    sys.exit(1)

dados = open('./files.txt', 'r')
for x in dados: 
    prj, clazz, _ = [part.strip() for part in x.split(':')]

    model="3-5"

    os.makedirs(os.path.join(".", prj, f"ts-{model}"), exist_ok=True)

    outputTime = open(os.path.join(".", prj, f"gpt-{model}-time.csv"), "w")
    
    outputTime.write(f"LABEL;#TS;TEMP;TIMESTAMP\n")

    source_path = os.path.join(".", prj)
    
    code = read_python_files(source_path)

    for i in range(1, 31):
        temperature = 0.7
        temperature_string = transform_temperature(temperature)
        timestamp = datetime.datetime.now()
        outputTime.write(f"BEGIN_TS;{i};{temperature};{timestamp};")
       
        messages = [] 

        generated_tests, messages = generate_tests(code, temperature, i)
        
        test_file_path = get_test_path(prj, model, clazz, i)
        with open(test_file_path, "w") as file:
            file.write(generated_tests)

        print(f"Arquivo de testes numero {i} gerado. Projeto: {prj}\n")
        
        # Verifica compilação e execução
        for attempt in range(3):
            error_message = compile_and_test(test_file_path)
            if not error_message:
                break
            corrected_tests, messages = feed_error_to_api(generated_tests, error_message, clazz, i, temperature)
            with open(test_file_path, "w") as file:
                file.write(corrected_tests)
            print(f"Tentativa de correção {attempt + 1} para o arquivo de teste {i} gerada.\n")
        
        # Verifica se os testes passam no pytest
        if not error_message:
            for attempt in range(3):
                pytest_error = run_pytest_and_check(prj, i)
                if not pytest_error:
                    break
                corrected_tests, messages = feed_error_to_api(generated_tests, pytest_error, clazz, i, temperature)
                with open(test_file_path, "w") as file:
                    file.write(corrected_tests)
                print(f"Tentativa de correção {attempt + 1} para o pytest do arquivo de teste {i} gerada.\n")
                messages.pop()
            
            # Registra erros no pytest se ainda houver falhas após 3 tentativas
            if pytest_error:
                failed_tests_count = pytest_error.count('= FAILURES =')
                record_failed_tests(prj, model, clazz, i, failed_tests_count)
        
        timestamp = datetime.datetime.now()
        outputTime.write(f"END_TS;{timestamp}\n")
    outputTime.close()
dados.close()
