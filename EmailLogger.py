from datetime import datetime
from pathlib import Path

class EmailLogger:
    status_success = "прочитан"
    status_unreadable = "непрочитан"
    status_skipped = "пропущен"
    status_invalid = "некорректный"

    def __init__(self, log_file):
        self.log_file = Path(log_file)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def add_log(self, message):
        with self.log_file.open("a", encoding="utf-8") as file:
            file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: {message}\n")

    def log_start(self):
        self.add_log("Начало записи")

    def log_session_start(self, source=None, destination=None):
        self.add_log("Начало обработки")
        if source is not None:
            self.add_log(f"Исходная папка: {source}")
        if destination is not None:
            self.add_log(f"Папка назначения: {destination}")

    def log_file_read(self, file_name):
        self.add_log(f"Файл прочитан: {file_name}")

    def log_file_failed(self, file_name, reason, action=None):
        message = f"Файл не прочитан: {file_name}, причина: {reason}"
        if action is not None:
            message += f", действие: {action}"
        self.add_log(message)

    def log_processed_file(self, file_name, status, classification):
        self.add_log(f"Обработан файл {file_name}, состояние: {status}, классификация: {classification}")

    def log_error(self, file_name, error_message, exception=None):
        message = f"Ошибка при обработке файла {file_name}: {error_message}"
        if exception is not None:
            message += f" ({exception})"
        self.add_log(message)

    def log_file_moved(self, source_path, target_path, category):
        self.add_log(f"Файл перемещён: {source_path} => {target_path}, категория: {category}")

    def log_stats(self, count_dict):
        self.add_log("Статистика после обработки:")
        for category, count in count_dict.items():
            self.add_log(f"{category}: {count}")

    def log_end(self):
        self.add_log("Конец записи")