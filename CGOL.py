import sys
from PyQt5.QtWidgets import QWidget, QApplication,QDesktopWidget
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt


class Board(QWidget): #implements game rules
     #create a list of life forms and give them a location on the 2d grid
    def __init__(self,size):
        super().__init__()
        LifeList = []
        for i in range(size):
            row = []
            for j in range(size):
                lifeform = LifeForm(i,j)
                row.append(lifeform)
            LifeList.append(row)
        self.setGeometry(0,0,QDesktopWidget().screenGeometry().width(),QDesktopWidget().screenGeometry().height())
        self.show()
class LifeForm(QWidget): #creates and controls anything related to lifeform also paints life form on screen
    def __init__(self,x,y):

        super().__init__()
        self.x = x
        self.y = y
#        self.addtoUI()

#    def addtoUI(self):

#        self.show()

    def paintEvent(self,event):
        qp = QPainter(Board())
        qp.begin()
        self.drawSelf(event,qp)
        qp.end()
    def drawSelf(self,event,qp):
        brush = qp.setBrush(Qt.red)
        #if location in grid is [x,y] then location of cell on pixels is
        #ScreensizeW // number of squares per row * x  and ScreenH//number of squares per col * y
        SCREENW = QDesktopWidget().screenGeometry().width()
        SCREENH = QDesktopWidget().screenGeometry().height()

        cell = qp.drawRect(SCREENW//N*self.x,SCREENH//N*self.y,SCREENW//N,SCREENH//N)




if __name__ == "__main__":
#GLOBALS FIRST
    N = 50

    #When i create a board it should create all the lifeforms for me and tell them to print themselves on the screen

    app = QApplication(sys.argv)
    print('no')
    b = Board(N)
    sys.exit(app.exec_())
