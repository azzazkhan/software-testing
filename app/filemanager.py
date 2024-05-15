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
    def delete(path):
        if not FileManager.exists(path):
            raise FileNotFoundError

        os.remove(FileManager.buildPath(path))

    def exists(path) -> bool:
        return os.path.exists(FileManager.buildPath(path))

    @staticmethod
    def buildPath(path: str):
        return (
            os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
            + "/temp/"
            + path.lstrip("/")
        )
