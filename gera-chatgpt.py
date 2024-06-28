import sys
import os
import requests
import re
from openai import OpenAI
import datetime
import subprocess
import csv
import shutil

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
    usage = completion.usage.total_tokens

    print(f"Request success: {clazz}\n")
    return content, usage


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
    message_path_import = "module_dir = os.path.dirname(os.path.abspath(__file__)); project_dir = os.path.abspath(os.path.join(module_dir, '..')); sys.path.append(project_dir)" #; sys.setrecursionlimit(15000) for quicksort
    
    messages = [
        {"role": "system", "content": "You are a senior software tester specialized in mutation testing."},
        {"role": "user", "content": f"I am using mutation testing on the Python code below. I want to create tests that cover every module of the code. Do not leave any method untested. Give me more than one test per method. As a senior software tester, give me a set of test cases on the Pytest format. Correctly import the file {clazz} and its modules being tested, utilize {message_path_import} to correctly import the file. Please, no additional information. Just the test cases. \n\n{code}"}
    ]
    generated_tests, usage = request_test_generation(messages, temperature)
    generated_tests = remove_other_test_classes(generated_tests, clazz, n)
    return generated_tests, messages, usage

def get_test_path(prj, model, clazz, number, fix = ""):
    return os.path.join(".", prj, f"ts-{model}", f"test_{model}_{temperature_string}_{number}{fix}.py")

def set_temperature(i):
    if(i <= 30): return 0.0
    if(i <= 60): return 0.1
    if(i <= 90): return 0.2
    if(i <= 120): return 0.3
    if(i <= 150): return 0.4
    if(i <= 180): return 0.5
    if(i <= 210): return 0.6
    if(i <= 240): return 0.7
    if(i <= 270): return 0.8
    if(i <= 300): return 0.9
    return 1.0

def transform_temperature(temperature):    
    if temperature == 1.0:
        return "1-0"
    else:
        temperature = int(temperature*10)
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
        {"role": "user", "content": f"The following Pytest test set result in these error messages. \n#########\n {generated_tests} \n#########\n.  You must keep all the correct tests and fix the assertion in the failed tests according to the error below. \n\nError Message: {error_message} \n Give me the full test set with no comments, only the full python code."}
    ]
    corrected_tests, usage = request_test_generation(messages, temperature)
    corrected_tests = remove_other_test_classes(corrected_tests, clazz, n)
    return corrected_tests, usage

def run_pytest_and_check(prj, test_file_path, number):
    result = subprocess.run(['pytest', test_file_path, '--disable-warnings', '-q', '--tb=short'], capture_output=True, text=True)
    if result.returncode != 0:
        return result.stdout
    return None

def record_failed_tests(prj, model, clazz, number, attempt, failed_tests_count):
    failed_tests_path = os.path.join(".", prj, f"failed_tests_{model}.csv")
    with open(failed_tests_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        if attempt == -1:
            writer.writerow([f"test_{model}_{temperature_string}_{number}_orig.py", failed_tests_count])
        else:
            writer.writerow([f"test_{model}_{temperature_string}_{number}_p{attempt}.py", failed_tests_count]) 

def rename_test_files(prj, model, clazz, i, temperature_string):
    test_file_base = os.path.join(".", prj, f"ts-{model}", f"test_{model}_{temperature_string}_{i}.py")
    corrections = ["_c0", "_c1", "_c2", "_p0", "_p1", "_p2"]
    
    original_test_file = test_file_base
    latest_test_file = None
    
    for suffix in corrections:
        test_file_path = os.path.join(".", prj, f"ts-{model}", f"test_{model}_{temperature_string}_{i}{suffix}.py")
        if os.path.exists(test_file_path):
            # Renomeia arquivos intermediários para ".py.p{n}" ou ".py.c{n}"
            new_suffix = f".py{suffix}"
            new_test_file_path = test_file_path.replace(".py", new_suffix)
            os.rename(test_file_path, new_test_file_path)
            latest_test_file = new_test_file_path
    
    # Renomeia o arquivo original e o último arquivo gerado conforme especificado
    if latest_test_file:
        os.rename(original_test_file, original_test_file.replace(".py", ".py.orig"))
        os.rename(latest_test_file, test_file_base)
        print(f"Arquivos renomeados: {original_test_file} -> {original_test_file.replace('.py', '.py.orig')}, {latest_test_file} -> {test_file_base}")

def rename_test_files_with_error(prj, model, clazz, i, temperature_string):
    test_file_base = os.path.join(".", prj, f"ts-{model}", f"test_{model}_{temperature_string}_{i}.py")
    corrections = ["", "_c0", "_c1", "_c2", "_p0", "_p1", "_p2"]
    
    for suffix in corrections:
        test_file_path = os.path.join(".", prj, f"ts-{model}", f"test_{model}_{temperature_string}_{i}{suffix}.py")
        if os.path.exists(test_file_path):
            os.rename(test_file_path, test_file_path.replace(".py", ".py.err"))
            print(f"Arquivo renomeado devido a erro: {test_file_path} -> {test_file_path.replace('.py', '.py.err')}")

if len(sys.argv) < 1:
    print("error: gera-chatgpt.py")
    print("Example: gera-chatgpt.py")
    sys.exit(1)

dados = open('./files.txt', 'r')
for x in dados: 
    prj, clazz, _ = [part.strip() for part in x.split(':')]

    model="3-5"

    dir_path = os.path.join(".", prj, f"ts-{model}")

    # Verifica se o diretório existe
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

    failed_tests_path = os.path.join(".", prj, f"failed_tests_{model}.csv")
    if os.path.exists(failed_tests_path):
        os.remove(failed_tests_path)

    os.makedirs(dir_path, exist_ok=True)

    outputTime = open(os.path.join(".", prj, f"gpt-{model}-time.csv"), "w")
    outputTokens = open(os.path.join(".", prj, f"gpt-{model}-tokens.csv"), "w")
    
    outputTime.write(f"LABEL;#TS;TEMP;TIMESTAMP\n")
    outputTokens.write(f"LABEL;#TS;TEMP;TOKENS\n")

    source_path = os.path.join(".", prj)
    
    code = read_python_files(source_path)

    for i in range(1, 331):
        total_usage = 0
        temperature = set_temperature(i)
        temperature_string = transform_temperature(temperature)
        timestamp = datetime.datetime.now()
        outputTime.write(f"BEGIN_TS;{i};{temperature};{timestamp};")
       
        messages = [] 

        generated_tests, messages, usage = generate_tests(code, temperature, i)
        total_usage += usage
        
        test_file_path = get_test_path(prj, model, clazz, i)
        with open(test_file_path, "w") as file:
            file.write(generated_tests)

        print(f"Arquivo de testes numero {i} gerado. Projeto: {prj}\n")
        
        # Verifica compilação e execução
        for attempt in range(3):
            error_message = compile_and_test(test_file_path)
            if not error_message:
                break
            corrected_tests, usage = feed_error_to_api(generated_tests, error_message, clazz, i, temperature)
            total_usage += usage
            test_file_path = get_test_path(prj, model, clazz, i, f"_c{attempt}")
            with open(test_file_path, "w") as file:
                file.write(corrected_tests)
            print(f"Tentativa de correção {attempt + 1} para o arquivo de teste {i} gerada.\n")
        
        # Verifica se os testes passam no pytest
        if not error_message:
            pytest_error = None
            for attempt in range(3):
                pytest_error = run_pytest_and_check(prj, test_file_path, i)
                if not pytest_error:
                    break
                # Registrar número de falhas no teste
                match = re.search("(\d+) failed", pytest_error) 
                if match is not None:
                    failed_tests_count = match.group(1)
                    record_failed_tests(prj, model, clazz, i, attempt-1, failed_tests_count)
                # Realimentar erro
                corrected_tests, usage = feed_error_to_api(generated_tests, pytest_error, clazz, i, temperature)
                total_usage += usage
                generated_tests = corrected_tests
                test_file_path = get_test_path(prj, model, clazz, i, f"_p{attempt}")
                with open(test_file_path, "w") as file:
                    file.write(corrected_tests)
                print(f"Tentativa de correção {attempt + 1} para o pytest do arquivo de teste {i} gerada.\n")
            if pytest_error:
                # Registrar número de falhas da ultima iteração
                match = re.search("(\d+) failed", pytest_error) 
                if match is not None:
                    failed_tests_count = match.group(1)
                    record_failed_tests(prj, model, clazz, i, attempt, failed_tests_count)
      

        # Renomeia os arquivos conforme necessário
        if not error_message and not pytest_error:
            rename_test_files(prj, model, clazz, i, temperature_string)
        else:
            rename_test_files_with_error(prj, model, clazz, i, temperature_string)
        
        timestamp = datetime.datetime.now()
        outputTime.write(f"END_TS;{timestamp}\n")
        outputTokens.write(f"END_TS;{i};{temperature};{total_usage}\n")
    
    outputTime.close()
    outputTokens.close()
dados.close()
