### Радиочастотные системы. Тестовое задание

#### 1. Linux команды 

#### 2. Linux команда для вывода "Hello, DevOps!"
Печатает строку "Hello, DevOps!", записывает её в файл hello.txt в домашней директории, и выводит содержимое 
файла на экран.

```echo "Привет, мир!" | tee -a output.txt && cat output.txt```

#### 3. Linux команда для вывода строк из логов
Выводит первые 5 строк со словом "error" из /var/log/syslog

```grep -w "error" /var/log/syslog | head -n 5```

#### 4. Bash/python-скрипт

Для исходного файла

```
name: test_server
path: /home/user/data
file: data.txt
port: 8080
log path: /var/log/app
```

Напишем python скрипт, который будет выводить строки из файла, содержащие слово, указанное как параметр

``python3 wordsearch.py -f ~/config.txt -w path``

```python
import argparse
import sys

parser = argparse.ArgumentParser(description='Search a word in a file')

parser.add_argument('-f', '--file', required=True, help='Path to file to parse')
parser.add_argument('-w', '--word', required=True, help='Word to search in file')

args = parser.parse_args()

file_path = args.file
search_word = args.word

try:
    with open(file_path, 'r') as f:
        file_lines = f.readlines()
        for line in file_lines:
            if search_word in line:
                print(line, end='')
        print('')
except FileNotFoundError:
    print(f'ERROR: file {file_path} not found')
    sys.exit(1)
except Exception as e:
    print(f'ERROR: unhandled exception {type(e).__name__} was acquired')
    sys.exit(1)

```