import unittest
from app.filemanager import FileManager
from app.logger import Logger


class FileManagerTest(unittest.TestCase):
    def test_messages_can_be_logged(self):
        Logger.log("My message")

        assert True
        FileManager.delete("application.log")

    def test_logged_messages_are_written_to_log_file(self):
        contents = "My message"
        Logger.log(contents)

        line = FileManager.readLazy("application.log")[0]

        assert line.find(contents) != -1
        FileManager.delete("application.log")

    def test_logged_messages_are_appended_to_log_file(self):
        messages = ["First log statement", "Second log statement"]

        [Logger.log(message) for message in messages]

        for i, line in enumerate(FileManager.readLazy("application.log")):
            # Using [22:-1] to skip timestamp and line break
            assert messages[i] == line[22:-1]

        FileManager.delete("application.log")

    def test_empty_line_is_added_at_end_of_logged_message(self):
        Logger.log("Dummy message")

        lines = FileManager.readLazy("application.log")

        assert lines[0][-1] == "\n"

        FileManager.delete("application.log")

    def test_logged_messages_can_be_searched(self):
        Logger.log("LoReM IPsum DOlEr")

        assert len(Logger.search("ipsum")) == 1

        FileManager.delete("application.log")
