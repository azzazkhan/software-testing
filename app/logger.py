from time import gmtime, strftime
from .filemanager import FileManager


class Logger:
    @staticmethod
    def log(message: str):
        if len(message) == 0:
            raise ValueError("Message should not be empty!")

        FileManager.append("application.log", Logger.format(message))

    @staticmethod
    def search(phrase: str):
        search_terms = phrase.lower().split(" ")
        results = []

        for line in FileManager.readLazy("application.log"):
            line = line.replace("\n", "")
            if not line or len(line) < 23:
                continue

            contents = line[22:].lower().replace("\n", "")

            # Python does not support interacting with outer loop
            # so we will use this hacky syntax of throwing an exception
            try:
                for term in search_terms:
                    if contents.find(term) != -1:
                        results.append(line)

                        raise InterruptedError

            except InterruptedError:
                pass

        return results

    @staticmethod
    def getTime():
        return strftime("%Y-%m-%d %H:%M:%S", gmtime())

    @staticmethod
    def format(message: str):
        time = Logger.getTime()

        return f"[{time}] {message}\n"
