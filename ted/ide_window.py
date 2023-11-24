from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog

from ted.edit_area import EditArea
from ted.syntax_highlighter import PythonSyntaxHighlighter



class IDEWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 IDE with File Loading")

        # Main widget and layout
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)

        # Editor
        self.editor = EditArea()
        self.main_layout.addWidget(self.editor)
        # Set up the syntax highlighter
        self.syntax_highlighter = PythonSyntaxHighlighter(self.editor.document())


        # Load file button
        self.load_button = QPushButton("Load File")
        self.load_button.clicked.connect(self.loadFile)
        self.main_layout.addWidget(self.load_button)

        self.setCentralWidget(self.main_widget)
        self.setGeometry(100, 100, 800, 600)



    def loadFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Python Files (*.py);;All Files (*)")
        if file_name:
            with open(file_name, 'r') as file:
                self.editor.setText(file.read())