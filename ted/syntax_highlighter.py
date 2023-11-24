
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont
from PySide6.QtCore import Qt, QRegularExpression


class PythonSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent):
        super().__init__(parent)

        # Syntax formatting for keywords
        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor(Qt.blue))
        keyword_format.setFontWeight(QFont.Bold)
        keywords = [
            "and", "as", "assert", "break", "class", "continue",
            "def", "del", "elif", "else", "except", "finally",
            "for", "from", "global", "if", "import", "in",
            "is", "lambda", "nonlocal", "not", "or", "pass",
            "raise", "return", "try", "while", "with", "yield"
        ]
        self.highlighting_rules = [(QRegularExpression(r'\b' + word + r'\b'), keyword_format) for word in keywords]

        # Syntax formatting for comments
        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor(Qt.darkGreen))
        self.highlighting_rules.append((QRegularExpression(r'#.*'), comment_format))

        # Syntax formatting for strings
        string_format = QTextCharFormat()
        string_format.setForeground(QColor(Qt.darkRed))
        self.highlighting_rules.append((QRegularExpression(r'".*"|\'.*\''), string_format))

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            match_iterator = pattern.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
        self.setCurrentBlockState(0)