import pytest
from pathlib import Path
from FileManager import FileManager
from FileReader import FileReader


@pytest.fixture
def setup(tmp_path):
    inbox = tmp_path/"test_inbox"
    inbox.mkdir()

    manager = FileManager(str(tmp_path/"test_sorted_inbox"))
    reader = FileReader(manager)

    return reader, manager, inbox

def test_read_valid_email(setup):
    reader, manager, inbox = setup

    s = inbox/"email.txt"
    s.write_text("sdssdcs \n fsdcscsc")

    emails = reader.read_directory(str(inbox))

    assert len(emails) == 1
    assert emails[0].Text == ["sdssdcs ", " fsdcscsc"]
    assert reader.get_stats()['files_read'] == 1

def test_read_empty_file(setup):
    reader, manager, inbox = setup

    s = inbox / "empty.txt"
    s.write_text("            ")

    emails = reader.read_directory(str(inbox))

    assert len(emails) == 0
    assert (Path(manager.base_dir)/"non_classified"/"empty.txt").exists()
    assert reader.get_stats()['files_failed'] == 1

def test_read_wrong_extension_file(setup):
    reader, manager, inbox = setup

    s = inbox/"file.jpg"
    s.write_text("cscsd")

    emails = reader.read_directory(str(inbox))

    assert len(emails) == 0
    assert (Path(manager.base_dir)/"non_classified"/"file.jpg").exists()

def test_get_counts_of_each_category(setup):
    reader, manager, inbox = setup

    (inbox/"first.txt").write_text("cdsc")
    (inbox/"second.txt").write_text("cscscsc")

    manager.move_email(str(inbox/"first.txt"), "urgent")

    counts = manager.count_files_in_each_category()
    assert counts['urgent'] == 1
    assert counts['spam'] == 0
    assert counts['non_urgent'] == 0

