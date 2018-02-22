from ipywidgets import widgets
from IPython.display import display, clear_output

from indana._helper import deepcopy

class ConfigBase:
    """
    Base class for configuration classes
    """
    def __init__(self, config):
        self._config = deepcopy(config)
        self._cb_submit_user = []

        self._boxes = []
        for field in self._config["fields"]:
            field["txt_value"] = widgets.Text()
            self._boxes.append(widgets.Box([
                widgets.Label(field["name"]),
                field["txt_value"],
            ]))

    def render_form(self, clear=True):
        if clear: clear_output()

        for field in self._config["fields"]:
            field["txt_value"].value = str(field["default"]) if "default" in field else ""
        
        for box in self._boxes:
            display(box)

        btn_submit = widgets.Button(description="submit")
        btn_submit.on_click(self._cb_submit)
        display(btn_submit)

    def register_submit(self, cb):
        self._cb_submit_user.append(cb)

    def _cb_submit(self, sender):
        values = {}
        for field in self._config["fields"]:
            values[field["name"]] = field["type"](field["txt_value"].value)
        for cb in self._cb_submit_user:
            cb(values)
