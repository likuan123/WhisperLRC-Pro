from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout


class ToolBar(QWidget):

    startClicked = Signal()
    stopClicked = Signal()
    openClicked = Signal()
    clearClicked = Signal()

    def __init__(self):

        super().__init__()

        layout = QHBoxLayout(self)

        self.openBtn = QPushButton("选择文件")

        self.startBtn = QPushButton("开始")

        self.stopBtn = QPushButton("停止")

        self.clearBtn = QPushButton("清空")

        self.stopBtn.setEnabled(False)

        layout.addWidget(self.openBtn)

        layout.addStretch()

        layout.addWidget(self.startBtn)

        layout.addWidget(self.stopBtn)

        layout.addWidget(self.clearBtn)

        self.openBtn.clicked.connect(self.openClicked)

        self.startBtn.clicked.connect(self.startClicked)

        self.stopBtn.clicked.connect(self.stopClicked)

        self.clearBtn.clicked.connect(self.clearClicked)

    def set_running(self, running: bool):

        self.startBtn.setEnabled(not running)

        self.stopBtn.setEnabled(running)
