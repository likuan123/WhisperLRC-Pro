from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QProgressBar,
    QVBoxLayout,
)


class ProgressWidget(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        self.info = QLabel("等待开始...")

        self.progress = QProgressBar()

        self.progress.setValue(0)

        layout.addWidget(self.info)

        layout.addWidget(self.progress)

    def set_progress(self, value):

        self.progress.setValue(value)

    def set_text(self, text):

        self.info.setText(text)
