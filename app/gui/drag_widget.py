from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QLabel, QFrame, QVBoxLayout


AUDIO_SUFFIX = {
    ".mp3",
    ".wav",
    ".m4a",
    ".flac",
    ".aac",
    ".ogg",
    ".wma",
    ".mp4",
    ".mkv",
    ".mov",
}


class DragWidget(QFrame):

    filesDropped = Signal(list)

    def __init__(self):

        super().__init__()

        self.setAcceptDrops(True)

        self.setObjectName("DropArea")

        self.setMinimumHeight(220)

        layout = QVBoxLayout(self)

        self.label = QLabel(
            "🎵\n\n拖拽音频或视频到这里\n\n支持 MP3 M4A WAV FLAC AAC MP4 MKV"
        )

        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

    def dragEnterEvent(self, event: QDragEnterEvent):

        if event.mimeData().hasUrls():

            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):

        files = []

        for url in event.mimeData().urls():

            path = Path(url.toLocalFile())

            if path.is_dir():

                for f in path.rglob("*"):

                    if f.suffix.lower() in AUDIO_SUFFIX:

                        files.append(str(f))

            else:

                if path.suffix.lower() in AUDIO_SUFFIX:

                    files.append(str(path))

        if files:

            self.filesDropped.emit(files)
