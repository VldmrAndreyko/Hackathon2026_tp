#!/usr/bin/env bash

set -u

cd "$(dirname "$0")" || { echo "Не удалось перейти в папку проекта."; exit 1; }

LOG_FILE="run.log"
INBOX_DIR="inbox"

if command -v python3 >/dev/null 2>&1; then
    PYTHON="python3"
elif command -v python >/dev/null 2>&1; then
    PYTHON="python"
else
    echo "Python не найден"
    exit 1
fi

if ! "$PYTHON" -c "import pymorphy3" >/dev/null 2>&1; then
    if [ -f "requirements.txt" ]; then
        "$PYTHON" -m pip install -r requirements.txt
    else
        "$PYTHON" -m pip install pymorphy3
    fi
fi

if [ ! -d "$INBOX_DIR" ]; then
    echo "Папка '$INBOX_DIR' не найдена"
    exit 1
fi

mail_count=$(find "$INBOX_DIR" -maxdepth 1 -type f | wc -l)
if [ "$mail_count" -eq 0 ]; then
    echo "Папка '$INBOX_DIR' пуста"
fi

echo "Писем во входящих: $mail_count"

"$PYTHON" main.py 2>&1 | tee "$LOG_FILE"
status=${PIPESTATUS[0]}

if [ "$status" -eq 0 ]; then
    echo "Обработка завершена успешно. Лог сохранён в $LOG_FILE"
else
    echo "Ошибка. Код ошибки: $status. Подробности в $LOG_FILE"
fi

exit "$status"
