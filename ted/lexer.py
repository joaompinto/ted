import keyword
import json
import wx
from pathlib import Path
import wx.stc as stc

class PythonLexer:
    def __init__(self, editor):
        self.editor = editor
        self.styles = self.load_styles()
        self.setup_lexer()


    def load_styles(self):
        app_dir = Path(__file__).resolve().parent
        config_dir = Path(wx.StandardPaths.Get().GetUserConfigDir())

        # Paths to search for the styles.json file
        paths = [
            app_dir / '..' / 'config' / 'styles.json',
            config_dir / 'styles.json'
        ]

        for path in paths:
            if path.exists():
                print(f"Loading styles from {path}")
                try:
                    with open(path, 'r') as file:
                        return json.load(file)
                except Exception as e:
                    print(f"Error loading JSON from {path}: {e}")

        # Default styles if JSON is not available
        return {
            "default": {"style": "fore:#000000"},
            "keyword": {"style": "fore:#0000FF,bold"},
            "triple_double_quotes": {"style": "fore:#800080,italic"}
            # ... other default styles
        }

    def setup_lexer(self):
        self.editor.SetLexer(stc.STC_LEX_PYTHON)
        self.editor.SetKeyWords(0, " ".join(keyword.kwlist))

        for style_name, style_conf in self.styles.items():
            style_id = getattr(stc, f"STC_P_{style_name.upper()}", None)
            if style_id is not None:
                self.editor.StyleSetSpec(style_id, style_conf['style'])