from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QFileDialog, QTabWidget
from PySide6.QtGui import QAction  # Corrected import
from ted.edit_area import EditArea



class IDEWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 IDE with File Loading")

        # Main widget and layout
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout(self.main_widget)

        # Tab Widget for multiple files
        self.tab_widget = QTabWidget()
        self.main_layout.addWidget(self.tab_widget)


        self.setCentralWidget(self.main_widget)
        self.setGeometry(100, 100, 800, 600)

        # Automatically open a new tab when the application starts
        self.createNewTab()

        # Create Menu Bar
        self.createMenuBar()

    def createMenuBar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("&File")

        # New Tab action
        new_tab_action = QAction("&New Tab", self)
        new_tab_action.triggered.connect(self.createNewTab)
        new_tab_action.setShortcut("Ctrl+N")  # Set the shortcut
        file_menu.addAction(new_tab_action)


        # Open File action
        open_action = QAction("&Open", self)
        open_action.triggered.connect(self.loadFile)
        file_menu.addAction(open_action)

        # Save File action
        save_action = QAction("&Save", self)
        save_action.triggered.connect(self.saveFile)
        file_menu.addAction(save_action)

    def createNewTab(self):
        # Create a new instance of the editor widget
        new_editor = EditArea()
        self.tab_widget.addTab(new_editor, "Untitled")
        self.tab_widget.setCurrentWidget(new_editor)  # Set the current tab
        new_editor.setFocus()  # Set focus to the new editor

    def loadFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            editor = EditArea()
            with open(file_name, 'r') as file:
                editor.setText(file.read())
            self.tab_widget.addTab(editor, file_name)

    def saveFile(self):
        current_widget = self.tab_widget.currentWidget()
        if current_widget:
            file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
            if file_name:
                with open(file_name, 'w') as file:
                    file.write(current_widget.text())