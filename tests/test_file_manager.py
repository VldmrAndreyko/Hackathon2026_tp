import pytest
from pathlib import Path
from hackathon_tp.FileManager import FileManager
from hackathon_tp.FileReader import FileReader





def test_create_folders(tmp_path):
    base_dir = tmp_path / "hackathon_tp"

    manager = FileManager(str(base_dir))

    for category in ['spam', 'urgent', 'non_urgent', 'non_classified']:
        assert (base_dir/category).exists()
        assert (base_dir/category).is_dir()

def test_move_email(tmp_path):
    base_dir = tmp_path / "hackathon_tp"

    manager = FileManager(str(base_dir))

    inbox = tmp_path/"inbox"
    inbox.mkdir()
    test_file = inbox/"test.txt"
    test_file.write_text("Реклама купи айфон")

    manager.move_email(str(test_file), "spam")

    assert not (inbox/"test.txt").exists()
    assert (base_dir/"spam"/"test.txt").exists()