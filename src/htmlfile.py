# encoding=UTF-8
import os
from textfile import textfile
from htmltable import htmltable


class htmlfile(textfile):
    __head = "<html>\n"
    __tail = "</html>\n"
    __title = ""

    def __init__(self, name, encoding="utf-8"):
        textfile.__init__(self, name, encoding)

    def head(self):
        self.write(self.__head)
        self.meta("content-type", 'text/html;charset=' + self.get_encoding())
        self.title()

    def meta(self, http_equiv, content):
        metaline = '<meta http-equiv="' + http_equiv + '" content="'\
         + content + '">\n'
        self.write(metaline)

    def title(self):
        titleline = "<title>" + self.__title + "</title>"
        self.write(titleline)

    def set_title(self, title):
        self.__title = title

    def tail(self):
        self.write(self.__tail)

    def header(self, text, level):
        headerline = "<h" + str(level) + ">" + text\
         + "</h" + str(level) + ">\n"
        self.write(headerline)

    def paragraph(self, text):
        paragraph_text = "<p>" + text + "</p>\n"
        self.write(paragraph_text)


def test():
    scriptpath = os.path.split(os.path.realpath(__file__))[0] + '/'
    print(scriptpath)
    testfolder = "../test/"
    testfilename = "test.htm"
    testfile = scriptpath + testfolder + testfilename
    f = htmlfile(testfile, "utf-8")
    f.open('w')
    f.set_title(u"test html 测试网页生成代码")
    f.head()
    f.header("header1", 1)
    f.header("header2", 2)
    f.header("header3", 3)
    f.header(u"测试中文标题1", 1)
    f.header(u"测试中文标题2", 2)
    f.header(u"测试中文标题3", 3)
    f.paragraph("babababa dfjafabfhabfa")
    f.paragraph(u"测试中文段落")

    listvals = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    table = htmltable()
    table.fromlist(listvals)
    tablehtml = table.tohtml()

    f.write(tablehtml)

    f.tail()
    f.close()

if __name__ == '__main__':
    test()
