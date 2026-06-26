from PySide6.QtCore import Signal
from PySide6.QtGui import QAction


class MainMenu:

    def __init__(self, window):

        self.window = window

        self.menuBar = window.menuBar()

        fileMenu = self.menuBar.addMenu("文件")

        self.openAction = QAction("打开文件", window)

        self.exitAction = QAction("退出", window)

        fileMenu.addAction(self.openAction)

        fileMenu.addSeparator()

        fileMenu.addAction(self.exitAction)

        toolMenu = self.menuBar.addMenu("工具")

        self.settingAction = QAction("设置", window)

        toolMenu.addAction(self.settingAction)

        helpMenu = self.menuBar.addMenu("帮助")

        self.aboutAction = QAction("关于", window)

        helpMenu.addAction(self.aboutAction)
