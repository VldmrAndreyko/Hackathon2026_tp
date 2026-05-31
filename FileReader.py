from pathlib import Path

from Email import Email


class FileReader:
    def __init__(self):
        self.stats = {'files_read': 0, 'files_failed': 0}

    def read_file(self, file_path: str):
        path = Path(file_path)

        if not path.exists():
            self.stats['files_failed'] += 1
            raise ValueError("Указан неверный путь к файлу")

        if not path.is_file():
            self.stats['files_failed'] += 1
            raise ValueError("По данному пути находится не файл")

        try:
            with open (path, 'r') as file:
                text = file.read()
                if text is None:
                    self.stats['files_failed'] += 1
                    raise ValueError("Текст в файле не может быть равен None")

                lines = text.splitlines()
                email = Email(lines)

                self.stats['files_read'] += 1
                return email
        except Exception as error:
            self.stats['files_failed'] += 1
            raise error

    def read_directory(self, dir_path: str):
        path = Path(dir_path)

        if not path.exists():
            self.stats['files_failed'] += 1
            raise ValueError("Указан неверный путь к директории")

        if not path.is_dir():
            self.stats['files_failed'] += 1
            raise ValueError("По данному пути находится не директория")


        emails = []
        for file_path in path.glob("*"):
            email = self.read_file(file_path)
            emails.append(email)

        return emails






