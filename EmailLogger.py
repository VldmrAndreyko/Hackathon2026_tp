from datetime import datetime 
class EmailLogger:
    status_success = "прочитан"
    status_unreadable = "непрочитан"
    status_skipped = "пропущен"

    def __init__(self, log_file):
        self.log_file = log_file
        self.log_start()

    def add_log(self, message):
        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]: {message}\n")

    def log_start(self):
        self.add_log("Начало записи")

    def log_processed_file(self, file_name, status, classification):
        self.add_log(f"Обработан файл {file_name}, состояние: {status}, классификация: {classification}")
    
    def log_error(self, file_name, error_message):
        self.add_log(f"Ошибка при обработке файла {file_name}: {error_message}")

    def log_stats(self, count_dict):
        self.add_log("Статистика после обработки:")
        for category, count in count_dict.items():
            self.add_log(f"{category}: {count}")
        
    def log_end(self):
        self.add_log("Конец записи")