from PySide6.QtWidgets import QStatusBar


class Status:

    def __init__(self, window):

        self.bar = QStatusBar()

        window.setStatusBar(self.bar)

        self.show("Ready")

    def show(self, text):

        self.bar.showMessage(text)
