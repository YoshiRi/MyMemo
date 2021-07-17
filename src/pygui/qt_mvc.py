import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Model(QAbstractItemModel):
    headers = 'トッピング', 'うどん/そば', '温/冷'
    def __init__(self, parent=None):
        super(Model, self).__init__(parent)
        self.items = [
            ['たぬき','そば','温'],
            ['きつね','うどん','温'],
            ['月見','うどん','冷'],
            ['天ぷら','そば','温'],
            ]

    def index(self, row, column, parent=QModelIndex()):
        return self.createIndex(row, column, None)

    def parent(self, child):
        return QModelIndex()

    def rowCount(self, parent=QModelIndex()):
        return len(self.items)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            try:
                return self.items[index.row()][index.column()]
            except:
                return
        return

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role != Qt.DisplayRole:
            return
        if orientation == Qt.Horizontal:
            return self.headers[section]

    def addRow(self, topping, menkind, hotcold):
        self.beginInsertRows(QModelIndex(), len(self.items), 1)
        self.items.append([topping, menkind, hotcold])
        self.endInsertRows()

    def removeRows(self, rowIndexes):
        for row in sorted(rowIndexes, reverse=True):
            self.beginRemoveRows(QModelIndex(), row, row + 1)
            del self.items[row]
            self.endRemoveRows()

    def flags(self, index):
        return super(Model, self).flags(index) | Qt.ItemIsEditable

    def setData(self, index, value, role=Qt.EditRole):
        if role == Qt.EditRole:
            self.items[index.row()][index.column()] = value
            return True
        return False


class View(QTreeView):
    def __init__(self, parent=None):
        super(View, self).__init__(parent)
        self.setItemsExpandable(False)
        self.setIndentation(0)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def drawBranches(self, painter, rect, index):
        return


class InputWidget(QWidget):
    toppings = 'きつね', 'たぬき', '天ぷら', '月見', '肉', 'カレー'
    noodles = 'うどん', 'そば'
    hotcold = '温', '冷'
    columns = toppings, noodles, hotcold

    def __init__(self, parent=None):
        super(InputWidget, self).__init__(parent)
        layout = QVBoxLayout()

        self.toppingInput = InputWidget.comboBox(InputWidget.toppings)
        layout.addWidget(self.toppingInput)

        grpbox, self.noodles = InputWidget.radioButtons(InputWidget.noodles)
        layout.addWidget(grpbox)

        grpbox, self.hotcold = InputWidget.radioButtons(InputWidget.hotcold)
        layout.addWidget(grpbox)

        self.addButton = QPushButton('確定')
        layout.addWidget(self.addButton)

        layout.addStretch()

        self.setLayout(layout)

    @staticmethod
    def comboBox(values):
        comboBox = QComboBox()
        for value in values:
            comboBox.addItem(value)
        return comboBox

    @staticmethod
    def radioButtons(values):
        grpbox = QGroupBox()
        layout = QHBoxLayout()
        buttons = []
        for value in values:
            rb = QRadioButton(value)
            layout.addWidget(rb)
            buttons.append(rb)
        buttons[0].setChecked(True)
        grpbox.setLayout(layout)
        return grpbox, buttons

    def values(self):
        topping = self.toppingInput.currentText()

        udonsoba = '?'
        for btn in self.noodles:
            if btn.isChecked():
                udonsoba = btn.text()
                break

        hotcold = '?'
        for btn in self.hotcold:
            if btn.isChecked():
                hotcold = btn.text()
                break

        return topping, udonsoba, hotcold


class Delegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(Delegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        editor = InputWidget.comboBox(InputWidget.columns[index.column()])
        editor.setParent(parent)
        return editor

    def setEditorData(self, editor, index):
        value = index.model().data(index, Qt.DisplayRole)
        editor.setCurrentIndex(editor.findText(value))

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText())


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.view = View(self)
        self.model = Model(self)
        self.view.setModel(self.model)
        self.view.setItemDelegate(Delegate())
        self.setCentralWidget(self.view)

        self.inputWidget = InputWidget()
        self.inputWidget.addButton.clicked.connect(self.addItem)
        self.addDock = QDockWidget('追加入力', self)
        self.addDock.setWidget(self.inputWidget)
        self.addDock.setAllowedAreas(Qt.AllDockWidgetAreas)
        self.addDockWidget(Qt.RightDockWidgetArea, self.addDock)
        self.addDock.hide()

        toolBar = QToolBar()
        self.addToolBar(toolBar)

        delButton = QPushButton('削除')
        delButton.clicked.connect(self.removeItems)
        toolBar.addWidget(delButton)

        self.addButton = QPushButton('追加')
        self.addButton.clicked.connect(self.addDock.show)
        toolBar.addWidget(self.addButton)

    def addItem(self):
        self.model.addRow(*self.inputWidget.values())

    def selectedRows(self):
        rows = []
        for index in self.view.selectedIndexes():
            if index.column() == 0:
                rows.append(index.row())
        return rows

    def removeItems(self):
        self.model.removeRows(self.selectedRows())


def main():
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    w.raise_()
    app.exec_()

if __name__ == '__main__':
    main()