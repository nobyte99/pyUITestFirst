# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 19:42:23 2018

@author: xhj
"""
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from  mainwindow import Ui_MainWindow

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Init()
    
    def Init(self):
        self.ui.pushButton.clicked.connect(self.close)
        
    

        
        