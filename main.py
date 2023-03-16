"""
@author Aman Rathore
"""
from aqt.editor import Editor
from .src import my_logger
from aqt import gui_hooks


def get_editor_fields_data(editor: Editor) -> dict:
    """get data of each field in the open add cards dialog, and returns it in form of dict"""
    return dict(editor.note.items())


def write_data_on_field(editor: Editor, data_dict):
    """overwrite the data on the editor fields
    it will only work if the field name specified in the dict is matching to the available field name"""
    fields = dict(editor.note.items())  # dictionary of values to add
    for field_name in fields:
        field_value = fields[field_name]
        if field_name in data_dict:
            fields[field_name] = f"{field_value} {data_dict[field_name]}"
    editor.note.fields = list(fields.values())
    editor.loadNote()


def save_editor_data():
    """Saves the data to a pickle file"""
    pass


def regain_field_data(editor: Editor):
    write_data_on_field(
        editor, {"Front": "value for front", "Back": "Back\'s value", "field3": "value3"})
    my_logger.add_log(get_editor_fields_data(editor))


gui_hooks.editor_did_load_note.append(regain_field_data)
