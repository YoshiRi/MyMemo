
# -*- coding: utf-8 -*-
"""
Stackoverflowの文章より原型を拝借
QtのListwidgetで複数選択をしてPlotする。
"""

from PyQt5 import QtWidgets, QtCore
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Test(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Test, self).__init__(parent)
        self.layout = QtWidgets.QVBoxLayout()
        # リスト作成
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setSelectionMode( #複数選択可能にする
            QtWidgets.QAbstractItemView.MultiSelection
        )
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 211, 291))
        for i in range(10):
            item = QtWidgets.QListWidgetItem("%i" % i)
            self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(self.printItemText)

        # Figureを作成
        self.Figure = plt.figure()
        self.FigureCanvas = FigureCanvas(self.Figure)  # FigureをFigureCanvasに追加
        self.axis = self.Figure.add_subplot(1,1,1) # axを持っておく

        self.layout.addWidget(self.add_label("Ctrlを押しながらで複数選択"))
        self.layout.addWidget(self.listWidget)
        self.layout.addWidget(self.FigureCanvas)
        self.setLayout(self.layout)


    def add_label(self,text):
        # ラベルを作る
        label1=QtWidgets.QLabel(self)
        label1.setText(text)
        label1.adjustSize()
        return label1


    def printItemText(self):
        # 選択したアイテムを表示
        items = self.listWidget.selectedItems()
        x = []
        for i in range(len(items)):
            x.append(int(self.listWidget.selectedItems()[i].text()))

        print(x)
        self.update_Figure(x)

    # Figure
    def update_Figure(self,x):
        self.axis.cla() # リセットを掛ける必要がある。
        self.axis.plot(x,'-o')
        plt.grid(); plt.legend(["selected number"])
        self.FigureCanvas.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = Test()
    form.show()
    sys.exit(app.exec_())