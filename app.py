import sys

from scrap import Scrap
from PyQt6.QtWidgets import (
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton
)

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.input_gui()
        
        
    def input_gui(self):

        self.setWindowTitle("YT-MoodAnalyzer-Qt")
        self.setFixedSize(400, 100)

        dialogLayout = QVBoxLayout()
        self.formLayout = QFormLayout()
        self.in1 = QLineEdit()
        self.in2 = QLineEdit()
        self.formLayout.addRow("API_KEY:", self.in1)
        self.formLayout.addRow("Video_ID:", self.in2)

        dialogLayout.addLayout(self.formLayout)
        buttons = QDialogButtonBox()
        buttons.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )
        dialogLayout.addWidget(buttons)
        self.setLayout(dialogLayout)
        buttons.accepted.connect(self.ok)
        buttons.rejected.connect(self.reject)

    def ok(self):
        scrap = Scrap()
        key = self.in1.text()
        vid = self.in2.text()
        scrap.set_api_key(key)
        scrap.set_video_id(vid)

        
        



app = QApplication([])
window = MainWindow()
window.show()
app.exec()