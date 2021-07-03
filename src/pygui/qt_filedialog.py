#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
    QAction, QFileDialog, QApplication)
from PyQt5.QtGui import QIcon
from PyQt5 import QtWidgets,QtCore

# テキストフォーム中心の画面のためQMainWindowを継承する
class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):      

        topleft = QtWidgets.QFrame()
        topleft.setFrameShape(QtWidgets.QFrame.StyledPanel)
        bottom = QtWidgets.QFrame()
        bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        
        splitter1 = QtWidgets.QSplitter(QtCore.Qt.Vertical)

        # 中央のWidget
        self.textEdit = QTextEdit()
        self.textEdit2 = QTextEdit()
        #self.setCentralWidget(self.textEdit) #中央に追加
        splitter1.addWidget(topleft)
        splitter1.addWidget(self.textEdit)
        splitter1.setSizes([100,200])

        self.statusBar() # 下のバー
        # メニューバーのアイコン設定
        openFile = QAction(QIcon('imoyokan.jpg'), 'Open', self)
        # ショートカット設定
        openFile.setShortcut('Ctrl+O')
        # ステータスバー設定
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog) #Short cutかクリックされるとこれが呼ばれる

        # メニューバー作成
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)       

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('File dialog')
        self.show()


    def showDialog(self):

        # 第二引数はダイアログのタイトル、第三引数は表示するパス
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        # fname[0]は選択したファイルのパス（ファイル名を含む）
        if fname[0]:
            # ファイル読み込み
            f = open(fname[0], 'r')

            # テキストエディタにファイル内容書き込み
            with f:
                data = f.read()
                self.textEdit.setText(data)        

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())