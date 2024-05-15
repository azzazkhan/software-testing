import os


class FileManager:
    @staticmethod
    def read(path):
        with open(path, FileManager.buildPath(path), "r") as file:
            print(f"Reading contents of {path}")
            return file.read()

    @staticmethod
    def readLazy(path):
        with open(path, FileManager.buildPath(path), "r") as file:
            print(f"Lazily reading contents of {path}")
            return file.readlines()

    @staticmethod
    def write(path, contents):
        with open(path, FileManager.buildPath(path), "w") as file:
            print(f"Overwriting contents of {path}")
            return file.write(contents)

    @staticmethod
    def append(path, contents):
        print(f"Appending to contents of {path}")
        with open(path, FileManager.buildPath(path), "a") as file:
            return file.write(contents)

    @staticmethod
    def delete(file_path) -> bool:
        print(f"Deleting {path}")
        path = FileManager.buildPath(file_path)

        if os.path.exists(path):
            print(f"No file exists on {path}")
            os.remove(path)
            return True

        print(f"File deleted successfully {path}")
        return False

    @staticmethod
    def buildPath(path: str):
        return path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
            path.lstrip("/"),
        )
