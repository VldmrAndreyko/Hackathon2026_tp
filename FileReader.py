from pathlib import Path

from Email import Email


class FileReader:
    def __init__(self, file_manager):
        self.stats = {'files_read': 0, 'files_failed': 0}
        self.extension = ".txt"
        self.file_manager = file_manager

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
            self.file_manager.move_email(path, "non_classified")
            return None
        try:
            with open (path, 'r') as file:
                text = file.read()
            if text.strip() == "":
                self.stats['files_failed'] += 1
                self.file_manager.move_email(path, "non_classified")
                return None

            lines = text.splitlines()
            email = Email(lines, str(path))
            self.stats['files_read'] += 1
            return email
        except:
            self.stats['files_failed'] += 1
            self.file_manager.move_email(path, "non_classified")
            return None

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

            email = self.read_file(str(file_path))

            if email is not None:
                emails.append(email)

        return emails

    def get_stats(self):
        return self.stats

    def reset_stats(self):
        self.stats = {'files_read': 0, 'files_failed': 0}
