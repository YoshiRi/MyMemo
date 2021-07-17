# -*- coding: utf-8 -*-
"""
Stackoverflowの文章より原型を拝借
QtのListwidgetで複数選択をする設定
https://stackoverflow.com/questions/4008649/qlistwidget-and-multiple-selection
"""

from PyQt5 import QtWidgets, QtCore


class Test(QtWidgets.QDialog):
    def __init__(self, parent=None):
        #super(Test, self).__init__(parent)
        super().__init__()

        self.layout = QtWidgets.QVBoxLayout()
        self.listWidget = QtWidgets.QListWidget()
        self.listWidget.setSelectionMode( #複数選択可能にする https://doc.qt.io/qt-5/qabstractitemview.html
            QtWidgets.QAbstractItemView.MultiSelection # QtWidgets.QAbstractItemView.ExtendedSelection 
        )
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 211, 291))
        for i in range(10):
            item = QtWidgets.QListWidgetItem("Item %i" % i)
            self.listWidget.addItem(item)
        self.listWidget.itemClicked.connect(self.printItemText)
        self.layout.addWidget(self.add_label("Ctrlを押しながらで複数選択"))
        self.layout.addWidget(self.listWidget)
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
            x.append(str(self.listWidget.selectedItems()[i].text()))

        print (x)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) # 実行時に必要なおまじない
    form = Test()
    form.show()
    app.exec_() 