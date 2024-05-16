from app.filemanager import FileManager
from time import time
import pytest
import os


def get_filename():
    return f"{int(time())}.txt"


def get_realpath(path):
    return (
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
        + "/temp/"
        + path.lstrip("/")
    )


def test_files_can_be_written():
    filename = get_filename()
    contents = "Test contents"

    FileManager.write(filename, contents)
    file = open(get_realpath(filename), "r")
    assert file.read() == contents

    file.close()
    FileManager.delete(filename)


def test_contents_can_be_appended():
    filename = get_filename()
    contents = "Test contents"
    FileManager.write(filename, contents)

    new_contents = "\nNew contents"
    FileManager.append(filename, new_contents)

    file = open(get_realpath(filename), "r")
    assert file.read() == f"{contents}{new_contents}"

    file.close()
    FileManager.delete(filename)


def test_contents_can_be_read_lazily():
    filename = get_filename()
    contents = ["First line", "Second line", "Third line"]
    FileManager.write(filename, "\n".join(contents))

    for i, line in enumerate(FileManager.readLazy(filename)):
        assert line.replace("\n", "") == contents[i]

    FileManager.delete(filename)


def test_files_can_be_deleted():
    filename = get_filename()
    with open(get_realpath(filename), "w") as file:
        file.write("")

    FileManager.delete(filename)

    assert os.path.exists(get_realpath(filename)) == False


def test_raises_error_when_deleting_non_existing_file():
    filename = get_filename() + "-non-existing.txt"

    with pytest.raises(FileNotFoundError):
        FileManager.delete(get_realpath(filename))
