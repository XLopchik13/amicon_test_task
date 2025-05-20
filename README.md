# Передача файлов через TCP и UDP

Этот проект содержит клиент-серверные
реализации для передачи файлов
с использованием сокетов TCP и UDP


## Использование:

### Auto Test mode:
1. Перейти на желаемую ветку (udp/tcp):
    ```bash
   git checkout <branch_name>
   
2. Запустить bash-скрипт:
    ```bash
    bash test/file_transfer_test.sh

### TCP Mode

1. Перейти на TCP ветку:
   ```bash
   git checkout tcp

2. Запустить TCP сервер:
   ```bash
   python3 src/server.py path/to/file

3. Запустить TCP клиент:
    ```bash
    python3 src/client.py path/to/output
   

### UDP Mode

1. Перейти на UDP ветку:
   ```bash
   git checkout udp

2. Запустить UDP сервер:
   ```bash
   python3 src/server.py path/to/file

3. Запустить UDP клиент:
    ```bash
    python3 src/client.py path/to/output
