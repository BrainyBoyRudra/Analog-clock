from PyQt5.QtWidgets import *
from PyQt5 import QtCore,QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
class clock (QMainWindow):
    def __init__(self):
        super().__init__()
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setWindowTitle('TitanClockŢ◉◠◠◣')
        self.setGeometry(200,300,200,300)
        self.setStyleSheet('background:cyan;')
        self.hpointer = QtGui.QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-50)])
        self.mpointer =QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-70)])
        self.spointer =QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-90)])
        self.bcolour = Qt.white
        self.mcolour = Qt.white
        self.scolour = Qt.white
    def paintEvent(self,event):
        rec = min(self.width(),self.height())
        tiktik =  QTime.currentTime()
        painter = QPainter(self)
        def drawpointer(colour,rotation,pointer):
            painter.setBrush(QBrush(colour))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width()/2,self.height()/2)
        painter.scale(rec/300,rec/300)
        #painter.setPen(QtCore.Qt.NoPen)
        painter.setPen(QtCore.Qt.darkCyan)
        drawpointer(self.bcolour,(30*(tiktik.hour()+tiktik.minute()/60)),self.hpointer)
        drawpointer(self.mcolour,(6*(tiktik.minute()+tiktik.second()/60)),self.mpointer)
        drawpointer(self.scolour,(6*tiktik.second()),self.spointer)
        painter.setPen(QPen(Qt.darkMagenta))
        for i in range(0,60):
            if i%5 == 0:
                painter.drawLine(87,0,97,0)
            painter.rotate(6)
        painter.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = clock()
win.show()
exit(app.exec_())