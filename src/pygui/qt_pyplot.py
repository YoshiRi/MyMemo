#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os

import numpy as np
import matplotlib.pyplot as plt

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

import glob
from PIL import Image

class Application(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # UIの初期化
        self.initUI()

        # rootディレクトリ
        self.root = '../../../../../Pictures/'
        # 拡張子
        self.ext = 'png'

        # ファイルを配置
        self.set_FileList()

        # 画像
        self.FileName = self.FileList.item(0).text()

        # 画像を読み込む
        self.load_ImageFile()

        # Figureの初期化
        self.initFigure()

        # ファイルを変更した時のイベント
        self.FileList.itemSelectionChanged.connect(self.FileList_Changed)

    # UIの初期化
    def initUI(self):
        # Figure用のWidget
        self.FigureWidget = QtWidgets.QWidget(self)
        # FigureWidgetにLayoutを追加
        self.FigureLayout = QtWidgets.QVBoxLayout(self.FigureWidget)
        # Marginを消す
        self.FigureLayout.setContentsMargins(0,0,0,0)

        # ファイルのリスト
        self.FileList = QtWidgets.QListWidget(self)

        # 配置
        self.setGeometry(0,0,900,600)
        #self.FigureWidget.setGeometry(200,0,700,600)
        #self.FileList.setGeometry(0,0,200,600)
        hbox = QtWidgets.QHBoxLayout(self)
        vbox = QtWidgets.QVBoxLayout(self)
        vbox.addWidget(self.add_label("file name"))
        vbox.addWidget(self.FileList)
        frame_vbox = QtWidgets.QFrame(self)
        frame_vbox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_vbox.setLayout(vbox)

        splitter1 = QtWidgets.QSplitter(Qt.Horizontal)
        splitter1.addWidget(frame_vbox)
        splitter1.addWidget(self.FigureWidget)
        # Widgetを追加
        hbox.addWidget(splitter1)

        # レイアウト適用
        self.setLayout(hbox)
        QApplication.setStyle(QStyleFactory.create('Cleanlooks'))

    def add_label(self,text):
        # ラベルを作る
        label1=QtWidgets.QLabel(self)
        label1.setText(text)
        label1.adjustSize()
        return label1
        

    # Figureの初期化
    def initFigure(self):
        # Figureを作成
        self.Figure = plt.figure(1)
        # FigureをFigureCanvasに追加
        self.FigureCanvas = FigureCanvas(self.Figure)
        # LayoutにFigureCanvasを追加
        self.FigureLayout.addWidget(self.FigureCanvas)

        self.axis = self.Figure.add_subplot(1,1,1)
        self.axis_image = self.axis.imshow(self.image, cmap='gray')
        plt.axis('off')

    # ファイルを配置
    def set_FileList(self):
        # ファイルの読み込み
        Files = glob.glob(self.root+'*.'+self.ext)
        # ソート
        self.Files = sorted(Files)

        # ファイルリストに追加
        for file in self.Files: 
            self.FileList.addItem(os.path.basename(file))

    # ファイルを変更した時の関数
    def FileList_Changed(self):
        # 選択しているファイルの名前を取得
        self.FileName = self.FileList.selectedItems()[0].text()
        # 画像を読み込み
        self.load_ImageFile()
        # Figureを更新
        self.update_Figure()

    # 画像ファイルを読み込む
    def load_ImageFile(self):
        # 画像を開く
        image = Image.open(self.root + self.FileName)
        # numpy.ndarrayに
        self.image = np.asarray(image)

    # Figureを更新
    def update_Figure(self):
        #self.axis_image.set_data(self.image)
        self.axis.imshow(self.image)
        self.FigureCanvas.draw()

QApp = QtWidgets.QApplication(sys.argv)
app = Application()
app.show()
sys.exit(QApp.exec_())