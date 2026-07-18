# TED — The Tiny EDitor

A lightweight, tabbed text editor built with **Python** and **PySide6** (Qt for Python). TED provides a clean and minimal IDE-like experience with essential editing features and a dark-themed style configuration inspired by VS Code.

## Features

- **Tabbed Editing** — Open and edit multiple files simultaneously in separate tabs.
- **File Operations** — Open, create, and save files through the menu bar.
- **Zoom In/Out** — Hold `Ctrl` and scroll the mouse wheel to increase or decrease the font size.
- **Indentation Support** — `Tab` to indent and `Shift+Tab` to unindent lines.
- **Configurable Styles** — Syntax highlighting colors defined in [`config/styles.json`](config/styles.json) using a dark theme color palette.
- **Keyboard Shortcuts** — `Ctrl+N` to create a new tab, standard shortcuts for open and save.

## Requirements

- Python 3.x
- PySide6

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the editor from the project root:

```bash
python -m ted
```

## Project Structure

```
ted/
├── __main__.py       # Entry point — launches the application
├── app.py            # QApplication setup and initialization
├── ide_window.py     # Main window with menu bar and tab widget
├── edit_area.py      # Text editor widget with zoom and indentation
config/
└── styles.json       # Syntax highlighting style definitions
```

## License

This project is licensed under the [MIT License](LICENSE).
