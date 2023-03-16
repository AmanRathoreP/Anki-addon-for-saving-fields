"""
@author Aman Rathore
"""
from aqt.editor import Editor
from .src import my_logger, my_constants
from aqt import gui_hooks
my_logger.add_log("all stuff imported")


def onEditorClosed(editor: Editor):
    # Editor is closed
    my_logger.add_log("Editor closed! Save data now or never")


gui_hooks.editor_did_load_note.append(onEditorClosed)
