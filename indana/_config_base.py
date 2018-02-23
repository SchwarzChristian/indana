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

        for field in self._config["fields"]:
            if "values" in field and type(field["values"]) is list:
                if not "default" in field: field["default"] = field["values"][0]
                field["widget"] = widgets.Dropdown(
                    description=field["name"],
                    options=field["values"],
                )
            else:
                if field["type"] is int:
                    field["widget"] = widgets.BoundedIntText(
                        description=field["name"],
                        min=field.get("min", 0),
                        max=field.get("max", 100),
                        step=field.get("step", 1),
                    )
                if field["type"] is float:
                    field["widget"] = widgets.BoundedFloatText(
                        description=field["name"],
                        min=field.get("min", 0),
                        max=field.get("max", 1),
                        step=field.get("step", 0.01),
                    )
                if field["type"] is str:
                    field["widget"] = widgets.Text(description=field["name"])

    def render_form(self, clear=True):
        if clear: clear_output()

        for field in self._config["fields"]:
            field["widget"].value = field["type"](field.get("default", field["type"]()))
            display(field["widget"])

        btn_submit = widgets.Button(description="submit")
        btn_submit.on_click(self._cb_submit)
        display(btn_submit)

    def register_submit(self, cb):
        self._cb_submit_user.append(cb)

    @property
    def current_values(self):
        values = {}
        for field in self._config["fields"]:
            values[field["name"]] = field["type"](field["widget"].value)
        return values

    def _cb_submit(self, sender):
        for cb in self._cb_submit_user:
            cb(self.current_values)
