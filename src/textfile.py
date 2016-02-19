# encoding=UTF-8


class textfile:
    __encoding = "utf-8"
    __name = ""
    __fp = None

    def __init__(self, name, encoding="utf-8"):
        self.__name = name
        self.__encoding = encoding

    def open(self, option="r"):
        self.__fp = open(self.__name, option)

    def close(self):
        if self.__fp is not None:
            self.__fp.close()
            self.__fp = None

    def write(self, content):
        if self.__fp is not None:
            self.__fp.write(content.encode(self.__encoding))
        else:
            print "file not open !\n"

    def read(self):
        pass

    def get_encoding(self):
        return self.__encoding
