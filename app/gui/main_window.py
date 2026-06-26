from PySide6.QtWidgets import (
    QFileDialog,
    QMainWindow,
    QWidget,
    QVBoxLayout,
)

from app.gui.drag_widget import DragWidget
from app.gui.file_table import FileTable
from app.gui.progress_widget import ProgressWidget
from app.gui.toolbar import ToolBar
from app.gui.menu import MainMenu
from app.gui.statusbar import Status


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("WhisperLRC Pro")

        self.resize(1200, 800)

        self.menu = MainMenu(self)

        self.status = Status(self)

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        self.toolbar = ToolBar()

        self.drop = DragWidget()

        self.table = FileTable()

        self.progress = ProgressWidget()

        layout.addWidget(self.toolbar)

        layout.addWidget(self.drop)

        layout.addWidget(self.table)

        layout.addWidget(self.progress)

        self.drop.filesDropped.connect(self.add_files)

        self.toolbar.openClicked.connect(self.open_files)

        self.toolbar.clearClicked.connect(self.clear_files)

    def open_files(self):

        files, _ = QFileDialog.getOpenFileNames(

            self,

            "选择文件",

            "",

            "Audio (*.mp3 *.wav *.m4a *.flac *.aac *.ogg *.mp4 *.mkv)",

        )

        if files:

            self.add_files(files)

    def add_files(self, files):

        for file in files:

            self.table.add_file(file)

        self.status.show(f"已添加 {len(files)} 个文件")

    def clear_files(self):

        self.table.setRowCount(0)

        self.progress.set_progress(0)

        self.progress.set_text("等待开始...")

        self.status.show("已清空")
