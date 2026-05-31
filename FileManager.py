from pathlib import Path


class FileManager:
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.categories = ['spam', 'urgent', 'non-urgent', 'non-classified']

        self.create_folders()

    def create_folders(self):
        self.base_dir.mkdir(parents=True, exist_ok=True)

        for folder_name in self.categories:
            folder_path = self.base_dir/folder_name
            folder_path.mkdir(parents=True, exist_ok=True)




