import wx
import wx.stc as stc
from ted.lexer import PythonLexer

class PythonEditor(stc.StyledTextCtrl):
    """Python source code editor"""
    def __init__(self, parent):
        super().__init__(parent)
        self.lexer = PythonLexer(self)
        self.set_dark_mode()
        self.SetCaretForeground("white")

    def set_dark_mode(self):
        # Set background and text colors for dark mode
        self.StyleSetBackground(wx.stc.STC_STYLE_DEFAULT, wx.Colour(30, 30, 30))  # Dark background
        self.StyleSetForeground(wx.stc.STC_STYLE_DEFAULT, wx.Colour(255, 255, 255))  # White text


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 600))
        self.panel = wx.Panel(self)
        self.editor = PythonEditor(self.panel)

        self.setup_ui()

    def setup_ui(self):
        # Create a vertical sizer
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Add a horizontal sizer for buttons
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Example buttons
        btn1 = wx.Button(self.panel, label="Button 1")
        btn2 = wx.Button(self.panel, label="Button 2")
        btn3 = wx.Button(self.panel, label="Button 3")

        # Add buttons to the horizontal sizer
        button_sizer.Add(btn1, 0, wx.ALL, 5)
        button_sizer.Add(btn2, 0, wx.ALL, 5)
        button_sizer.Add(btn3, 0, wx.ALL, 5)

        # Add the button sizer and editor to the vertical sizer
        vbox.Add(button_sizer, 0, wx.EXPAND)
        vbox.Add(self.editor, 1, wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, 5)

        # Set the sizer for the panel
        self.panel.SetSizer(vbox)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, "the Tiny EDitor")
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()
