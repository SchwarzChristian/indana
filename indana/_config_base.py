from ipywidgets import widgets
from IPython.display import display, clear_output

from indana._helper import deepcopy

class ConfigBase:
    """
    Base class for configuration classes
    """
    def __init__(self, config, submit_name="submit"):
        self._config = deepcopy(config)
        self._cb_submit_user = []
        self._sumbit_name = submit_name

        for field in self._config["fields"]:
            if "description" in field:
                description = "%s, (%s)" % (field["description"], field["name"])
            else:
                description = field["name"]
            if "values" in field and type(field["values"]) is list:
                if not "default" in field: field["default"] = field["values"][0]
                field["widget"] = widgets.Dropdown(
                    description=description,
                    options=field["values"],
                )
            else:
                if field["type"] is int:
                    field["widget"] = widgets.BoundedIntText(
                        description=description,
                        min=field.get("min", 0),
                        max=field.get("max", 100),
                        step=field.get("step", 1),
                    )
                elif field["type"] is float:
                    field["widget"] = widgets.BoundedFloatText(
                        description=description,
                        min=field.get("min", 0),
                        max=field.get("max", 1),
                        step=field.get("step", 0.01),
                    )
                elif field["type"] is str:
                    field["widget"] = widgets.Text(description=description)
                elif field["type"] is bool:
                    field["widget"] = widgets.Checkbox(description=description)
                else: raise Exception("can not handle type: " + field["type"].__name__)

    def render_form(self, clear=True, **defaults):
        if clear: clear_output()

        for field in self._config["fields"]:
            field["widget"].value = field["type"](
                defaults.get(field["name"], 
                    field.get("default", 
                        field["type"]()
                    )
                )
            )
            display(field["widget"])

        btn_submit = widgets.Button(description=self._sumbit_name)
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
