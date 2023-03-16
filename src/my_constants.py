"""
@author Aman Rathore
"""
import os
import json

root_dir = os.path.dirname(os.path.dirname(__file__))

logs_dir = os.path.join(root_dir, "logs")


try:
    with open(os.path.join(root_dir, "meta.json"), 'r') as f:
        meta = json.load(f)
    useless_variable = meta["config"]["useless_variable"]
except:
    with open(os.path.join(root_dir, "config.json"), 'r') as f:
        config = json.load(f)
    useless_variable = config["useless_variable"]
