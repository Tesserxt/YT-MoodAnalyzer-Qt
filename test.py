import sys

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
        formLayout = QFormLayout()
        formLayout.addRow("API_KEY:", QLineEdit())
        formLayout.addRow("Video_ID:", QLineEdit())

        dialogLayout.addLayout(formLayout)
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
        print("aradha")
        self.accept()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()