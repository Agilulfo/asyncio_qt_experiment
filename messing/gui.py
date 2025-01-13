from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QWidget,
)
import sys
from loopy import run_loopy

import PySide6.QtAsyncio as QtAsyncio

def run_gui():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    QtAsyncio.run(handle_sigint=True)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("async qt experiment")

        self.setCentralWidget(Central())


class Central(QWidget):
    def __init__(self):
        super().__init__()
        self.flip_flop_button = QPushButton("flip")
        async_run_button = QPushButton("Run async nonsense")

        layout = QHBoxLayout(self)
        layout.addWidget(self.flip_flop_button)
        layout.addWidget(async_run_button)

        self.flip_flop_button.clicked.connect(self.flip_flop_action)
        async_run_button.clicked.connect(self.async_nonsense)

    def flip_flop_action(self):
        if self.flip_flop_button.text() == "flip":
            self.flip_flop_button.setText("flop")
        else:
            self.flip_flop_button.setText("flip")

    def async_nonsense(self):
        run_loopy()
