import shutil
from pathlib import Path


class FileManager:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.categories = ['spam', 'urgent', 'non_urgent', 'non_classified']

        self.create_folders()

    def create_folders(self):
        self.base_dir.mkdir(parents=True, exist_ok=True)

        for folder_name in self.categories:
            folder_path = self.base_dir/folder_name
            folder_path.mkdir(parents=True, exist_ok=True)

    def move_email(self, email_path: str, category: str):
        source = Path(email_path)

        if category not in self.categories:
            raise ValueError(f"Категории {category} не существует")

        if not source.exists():
            raise ValueError(f"Файл для перемещения не найден: {source}")

        if not source.is_file():
            raise ValueError(f"Перемещать можно только файлы. Это не файл: {source}")

        target = self.base_dir/category/source.name

        try:
            shutil.move(source, target)

        except Exception as error:
            raise ValueError(f"Ошибка перемещения: {error}")

