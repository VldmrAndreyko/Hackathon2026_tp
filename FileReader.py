from pathlib import Path

from Email import Email


class FileReader:
    def __init__(self):
        self.stats = {'files_read': 0, 'files_failed': 0}
        self.extension = ".txt"

    def read_file(self, file_path: str):
        path = Path(file_path)

        if not path.exists():
            self.stats['files_failed'] += 1
            raise ValueError(f"Указан неверный путь к файлу {path}")

        if not path.is_file():
            self.stats['files_failed'] += 1
            raise ValueError(f"По данному пути находится не файл {path}")

        if path.suffix != self.extension:
            self.stats['files_failed'] += 1
            raise ValueError(f"Расширение данного файла не поддерживается {path}")

        try:
            with open (path, 'r') as file:
                text = file.read()
                if text.strip() == "":
                    self.stats['files_failed'] += 1
                    raise ValueError(f"Файл пустой {path}")

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
            raise ValueError(f"Указан неверный путь к директории {path}")

        if not path.is_dir():
            self.stats['files_failed'] += 1
            raise ValueError(f"По данному пути находится не директория {path}")


        emails = []
        for file_path in path.glob("*"):
            if file_path.is_dir():
                continue
            try:
                email = self.read_file(file_path)
                emails.append(email)
            except Exception as error:
                print(f"Ошибка чтения файла {file_path}: {error}")

        return emails

    def get_stats(self):
        return self.stats

    def reset_stats(self):
        self.stats = {'files_read': 0, 'files_failed': 0}
