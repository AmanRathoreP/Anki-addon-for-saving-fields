from aqt.qt import QAction
from aqt.utils import showInfo, qconnect
from aqt import mw
from .src import my_logger, my_constants

my_logger.add_log("all stuff imported")


def testFunction() -> None:
    my_logger.add_log("user pressed test button")
    showInfo(
        f"Addon hierarchy is created successfully! and the useless variable value is {my_constants.useless_variable}")


action = QAction("test", mw)
qconnect(action.triggered, testFunction)
mw.form.menuTools.addAction(action)
