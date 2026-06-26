import os

from PySide6.QtWidgets import (
    QTableWidget,
    QHeaderView,
    QTableWidgetItem,
)


class FileTable(QTableWidget):

    def __init__(self):

        super().__init__(0, 4)

        self.setHorizontalHeaderLabels(
            [
                "文件",
                "大小",
                "状态",
                "输出",
            ]
        )

        self.horizontalHeader().setSectionResizeMode(
            0,
            QHeaderView.Stretch,
        )

        self.horizontalHeader().setSectionResizeMode(
            1,
            QHeaderView.ResizeToContents,
        )

        self.horizontalHeader().setSectionResizeMode(
            2,
            QHeaderView.ResizeToContents,
        )

        self.horizontalHeader().setSectionResizeMode(
            3,
            QHeaderView.Stretch,
        )

    def add_file(self, filename):

        row = self.rowCount()

        self.insertRow(row)

        size = os.path.getsize(filename) / 1024 / 1024

        self.setItem(
            row,
            0,
            QTableWidgetItem(filename),
        )

        self.setItem(
            row,
            1,
            QTableWidgetItem(f"{size:.2f} MB"),
        )

        self.setItem(
            row,
            2,
            QTableWidgetItem("等待"),
        )

        self.setItem(
            row,
            3,
            QTableWidgetItem(""),
        )

    def update_status(self, row, status):

        self.item(row, 2).setText(status)

    def update_output(self, row, text):

        self.item(row, 3).setText(text)
