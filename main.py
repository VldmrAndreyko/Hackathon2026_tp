from pathlib import Path
from FileReader import FileReader
from FileManager import FileManager
from EmailClassifier import EmailClassifier
from EmailLogger import EmailLogger

logger = EmailLogger("logs/email_processing.log")
logger.log_start()

manager = FileManager("sorted_inbox", logger=logger)
reader = FileReader(manager, logger=logger)

try:
    emails = reader.read_directory("inbox")
except Exception as error:
    logger.log_error("inbox", str(error))
    emails = []

for email in emails:
    classifier = EmailClassifier(email)
    category = classifier.classify()

    try:
        manager.move_email(email.path, category)
        logger.log_processed_file(email.path, EmailLogger.status_success, category)
    except Exception as error:
        logger.log_error(email.path, str(error))

reader_stats = reader.get_stats()
manager_stats = manager.count_files_in_each_category()

stats = {}
stats["Прочитано файлов"] = reader_stats['files_read']
stats["Не удалось прочитать"] = reader_stats['files_failed']
for category, count in manager_stats.items():
    stats[f"Файлов в папке {category}"] = count
logger.log_stats(stats)
logger.log_end()

print("Итоговая статистика:")

print(f"Успешно прочитано: {reader_stats['files_read']} файлов")
print(f"Не удалось прочитать: {reader_stats['files_failed']} файлов, они отправлены в папку 'non_classified'")

for category, count in manager_stats.items():
    print(f"В папке {category}: {count} файлов")