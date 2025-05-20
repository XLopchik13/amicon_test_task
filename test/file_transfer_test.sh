#!/bin/bash

set -e

FILE="test/random_data.bin"
RECEIVED="test/received_data.bin"

mkdir -p test
head -c 2000000 /dev/urandom > $FILE

# Запуск UDP сервера
python3 src/server.py $FILE &
SERVER_PID=$!
sleep 1

# Запуск UDP клиента
python3 src/client.py $RECEIVED

# Проверка
if cmp -s "$FILE" "$RECEIVED"; then
    echo "Test passed: files match"
else
    echo "Test failed: files do not match"
    exit 1
fi

kill $SERVER_PID
