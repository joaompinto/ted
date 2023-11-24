import sys
from PySide6.QtWidgets import QApplication, QStyleFactory
from ted.ide_window import IDEWindow

def main(name: str):

    if name == "__main__":

        # Create the Qt Application
        app = QApplication(sys.argv)

        # Set the application style to Windows native
        app.setStyle(QStyleFactory.create("Fusion"))

        # Create an instance of the IDEWindow
        mainWin = IDEWindow()
        mainWin.show()

        sys.exit(app.exec())