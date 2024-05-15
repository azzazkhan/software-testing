import os


class FileManager:
    @staticmethod
    def read(path):
        with open(FileManager.buildPath(path), "r") as file:
            return file.read()

    @staticmethod
    def readLazy(path):
        with open(FileManager.buildPath(path), "r") as file:
            return file.readlines()

    @staticmethod
    def write(path, contents):
        with open(FileManager.buildPath(path), "w") as file:
            return file.write(contents)

    @staticmethod
    def append(path, contents):
        with open(FileManager.buildPath(path), "a") as file:
            return file.write(contents)

    @staticmethod
    def delete(path) -> bool:
        path = FileManager.buildPath(path)

        if os.path.exists(path):
            os.remove(path)
            return True

        return False

    @staticmethod
    def buildPath(path: str):
        return (
            os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            + "/temp/"
            + path.lstrip("/")
        )
