#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
Qt checkbox のチュートリアル
https://www.finddevguides.com/Pyqt-qsplitter-widget

Example：Qwidgetから継承
SplitterはaddWidgetで部品を追加可能。Splitter自身も追加可能
基本的に一つの領域に一つの部品を配置できる。
"""

class Example(QWidget):

   def __init__(self):
      super(Example, self).__init__()

      self.initUI()

   def initUI(self):

      hbox = QHBoxLayout(self)
      
      # フレームを作る
      topleft = QFrame()
      topleft.setFrameShape(QFrame.StyledPanel)
      bottom = QFrame()
      bottom.setFrameShape(QFrame.StyledPanel)

      # ラベルを作る
      label1=QtWidgets.QLabel(self)
      label1.setText("label1")
      label1.addWidget()


      # 水平に分割
      splitter1 = QSplitter(Qt.Horizontal)
      textedit = QTextEdit()
      textedit2 = QTextEdit()
      textedit3 = QTextEdit()
      splitter1.addWidget(textedit2)
      splitter1.addWidget(textedit)
      splitter1.setSizes([100,200])

      splitter2 = QSplitter(Qt.Vertical)
      splitter2.addWidget(splitter1)
      splitter2.addWidget(textedit3)

      # Widgetを追加
      hbox.addWidget(splitter2)

      # レイアウト適用
      self.setLayout(hbox)
      QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

      # Windowサイズを規定
      self.setGeometry(300, 300, 300, 200)
      self.setWindowTitle('QSplitter demo')
      self.show()

def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()