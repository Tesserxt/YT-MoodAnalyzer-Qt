import sys
import os

from ytApi import YtApi
from db import Database
from hfApi import HuggingFaceInferenceApi

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
        self.setFixedSize(500, 150)

        dialogLayout = QVBoxLayout()
        self.formLayout = QFormLayout()
        self.in1 = QLineEdit()
        self.in2 = QLineEdit()
        self.in3 = QLineEdit()
        self.formLayout.addRow("Youtube_API_KEY:", self.in1)
        self.formLayout.addRow("HF_Inference_API_key:", self.in2)
        self.formLayout.addRow("Video_ID:", self.in3)

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
        self.accept()

        ytApi = YtApi()
        db = Database()
        hfi = HuggingFaceInferenceApi()

        yt_key = self.in1.text()
        hfi_key = self.in2.text()
        vid = self.in3.text()


        #only responsible for saving credentials data for recall purposes
        db.save_cfg_data(
            {
                'yt_key': yt_key, 
                'hfi_key': hfi_key, 
                'vid': vid
            },
            "settings"
        )

        ytApi.set_api_key(yt_key)
        ytApi.set_video_id(vid)
        hfi.set_api_key(hfi_key)
       

        if not os.path.isfile("ytCommentsData.json"):
            data = ytApi.fetch_data()
            db.save_json_data(data)
        else:
            print("ytCommentsData already exists.")
        



        
        

 

app = QApplication([])
window = MainWindow()
window.show()
app.exec()