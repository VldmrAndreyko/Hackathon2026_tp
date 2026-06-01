from pathlib import Path
from FileReader import FileReader
from FileManager import FileManager
from EmailClassifier import EmailClassifier

manager = FileManager("sorted_inbox")
reader = FileReader(manager)

try:
    emails = reader.read_directory("inbox")
except Exception as error:
    print(f"Ошибка: {error}")

for email in emails:
    classifier = EmailClassifier(email)
    category = classifier.classify()

    try:
        manager.move_email(email, category)
    except Exception as error:
        print(f"Не удалось переместить файл {email.path}: {error}")

reader_stats = reader.get_stats()
manager_stats = manager.count_files_in_each_category()

print("Итоговая статистика:")

print(f"Успешно прочитано: {reader_stats['files_read']} файлов")
print(f"Не удалось прочитать: {reader_stats['file_failed']} файлов, они отправлены в папку 'non_classified'")

for category, count in manager_stats:
    print(f"В папке {category}: {count} файлов")
