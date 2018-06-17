#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import myWindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    MainWindow = myWindow.MyWindow()
    MainWindow.show() 
    sys.exit(app.exec_())
