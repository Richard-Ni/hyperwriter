# encoding=UTF-8
class htmlcell:
    __value = ""
    __row = 1
    __col = 1
    __rowspan = 1
    __colspan = 1
    __align = "center"
    __valign = "middle"
    __ishead = False

    def __init__(self, row, col, value, rowspan=1, colspan=1, ishead=False):
        self.__row = row
        self.__col = col
        self.__value = value
        self.__rowspan = rowspan
        self.__colspan = colspan
        self.__ishead = ishead

    def tohtml(self):
        attr_rowspan = ""
        attr_colspan = ""
        attr_align = ""
        attr_valign = ""
        attr_value = str(self.__value)
        attr_type = 'td'
        if self.__ishead:
            attr_type = 'th'

        if self.__rowspan != 1:
            attr_rowspan = ' rowspan="' + str(self.__rowspan) + '"'

        if self.__colspan != 1:
            attr_colspan = ' colspan="' + str(self.__colspan) + '"'

        if self.__align != "center":
            attr_align = ' align="' + self.__align + '"'

        if self.__valign != "middle":
            attr_valign = ' valign="' + self.valign + '"'

        td_text = '<' + attr_type + attr_colspan + attr_rowspan + attr_valign\
            + attr_align + '>'
        td_text += attr_value
        td_text += '</' + attr_type + '>\n'
        return td_text

    def rows(self):
        '''
        the range of row
        '''
        return range(self.__row, self.__row + self.__rowspan)

    def cols(self):
        '''
        the range of column
        '''
        return range(self.__col, self.__col + self.__colspan)

    def max_row(self):
        return max(self.rows())

    def max_col(self):
        return max(self.cols())

    def min_row(self):
        return min(self.rows())

    def min_col(self):
        return min(self.cols())

    def __contains__(self, xy):
        return (xy[0] in self.rows()) and (xy[1] in self.cols())

    def range(self):
        '''
        cell covered area
        '''
        return [(x, y) for x in self.rows() for y in self.cols()]

    def __and__(self, other_cell):
        '''
        get intersection of this cell and other cell
        '''
        return [x for x in self.range() if x in other_cell.range()]

    def row(self):
        return self.__row

    def col(self):
        return self.__col

    def setval(self, value):
        self.__value = value

    def getval(self, value):
        return self.__value

    def overlap(self, other_cell):
        '''
        test if this cell is overlap with other cell
        '''
        return (self & other_cell != [])


class htmltable:
    __data = []
    __caption = ""
    __rowsize = 0
    __colsize = 0
    __border = 1

    def __init__(self, data=[], caption=""):
        self.__data = data
        self.__caption = caption
        if len(self.__data) != 0:
            self.resize()

    def getcell(self, row, column):
        for cell in self.__data:
            if (row, column) in cell:
                return cell

    def setcell(self, row, column, value):
        update_value = False
        for cell in self.__data:
            if (row, column) in cell:
                index = self.__data.index(cell)
                self.__data[index].setval(value)
                update_value = True

        if update_value is False:
            self.__data.append(htmlcell(row, column, value))
            self.resize()

    def resize(self, rowsize=0, colsize=0):
        max_row = max([i.max_row() for i in self.__data])
        max_col = max([i.max_col() for i in self.__data])
        self.__rowsize = max(self.__rowsize, rowsize, max_row)
        self.__colsize = max(self.__colsize, colsize, max_col)

    def fromlist(self, listvals):
        for row in listvals:
            row_index = listvals.index(row) + 1
            for value in row:
                col_index = row.index(value) + 1
                self.__data.append(htmlcell(row_index, col_index, value))
        self.resize()

    def tohtml(self):
        attr_border = 'border="1"'
        if self.__border != 1:
            attr_border = 'border="' + str(self.__border) + '"'

        htmltext = '<table ' + attr_border + '>\n'
        for row in range(1, self.__rowsize+1):
            htmltext += '<tr>\n'
            for col in range(1, self.__colsize + 1):
                cell = self.getcell(row, col)
                if cell.row() == row and cell.col() == col:
                    htmltext += cell.tohtml()
            htmltext += '</tr>\n'
        htmltext += '</table>\n'
        return htmltext


def test():
    cell = htmlcell(1, 1, 789, 2, 2)
    xy1 = (3, 4)
    print "xy1 in cell:", xy1 in cell
    xy2 = (1, 2)
    print "xy2 in cell:", xy2 in cell
    print "cell.range():", cell.range()

    cell2 = htmlcell(3, 3, 44)
    cell3 = htmlcell(2, 2, 55, 3, 3)

    print "cell & cell2:", cell & cell2
    print "cell & cell3:", cell & cell3
    print "cell overlap cell2:", cell.overlap(cell2)
    print "cell overlap cell3:", cell.overlap(cell3)
    print "cell to html:", cell.tohtml()
    print "cell2 to html:", cell2.tohtml()
    print "cell3 to html:", cell3.tohtml()

    listvals = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    table = htmltable()
    table.fromlist(listvals)
    tablehtml = table.tohtml()
    print tablehtml


if __name__ == '__main__':
    test()
