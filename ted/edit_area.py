from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTextEdit
from PySide6.QtGui import QTextCursor, QFont, QKeyEvent, QWheelEvent

class EditArea(QTextEdit):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the font size
        self.font_size = 14
        self.setFontSize(self.font_size)
        self.setTabWidth(4)

        self.changing_tabs = False

    def setFontSize(self, size):
        font = QFont()
        font.setPointSize(size)
        self.setFont(font)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() == Qt.ControlModifier:
            # Zoom in or out
            delta = event.angleDelta().y()
            if delta > 0:
                self.font_size += 1
            elif delta < 0 and self.font_size > 1:
                self.font_size -= 1
            self.setFontSize(self.font_size)

            event.accept()
        else:
            super().wheelEvent(event)  # Handle other wheel events normally

    def setTabWidth(self, spaces):
        fm = self.fontMetrics()
        space_width = fm.horizontalAdvance(' ')
        self.setTabStopDistance(space_width * spaces)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Backtab:
            # Handle Shift+Tab here
            self.unindentLine()
        else:
            super().keyPressEvent(event)  # Handle other key events normally

    def unindentLine(self):
        print("Unindenting line")

        cursor = self.textCursor()
        cursor.select(QTextCursor.LineUnderCursor)
        line_text = cursor.selectedText()
        print("Line text:", line_text)

        # Count the number of leading tabs in line_text
        leading_tabs = 0
        for i in range(len(line_text)):
            if line_text[i] != '\t':
                break
            leading_tabs += 1

        if leading_tabs > 0:
            chars_to_remove = 1
        else:
            chars_to_remove = 0

        # Select text between the start of the line and the first non-space character
        # Remove the spaces
        cursor.movePosition(QTextCursor.StartOfLine)
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, chars_to_remove)
        cursor.removeSelectedText()
