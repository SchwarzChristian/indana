import pandas as pd
from IPython.display import display, clear_output
from ipywidgets import widgets
from os import path

class TableForm:
    def __init__(self, config):
        self._config = config

        if path.isfile(self._config["filename"]):
            self._data = pd.read_csv(self._config["filename"])
        else:
            self._data = pd.DataFrame()
        
        self._boxes = []
        for field in self._config["fields"]:
            field["txt_value"] = widgets.Text()
            self._boxes.append(widgets.Box([
                widgets.Label(field["name"]),
                field["txt_value"],
            ]))

    @property
    def data(self):
        return self._data
            
    def render_form(self):
        clear_output()

        display(self._data)
        for field in self._config["fields"]:
            field["txt_value"].value = field["default"] if "default" in field else ""
        
        for box in self._boxes:
            display(box)

        btn_submit = widgets.Button(description="submit")
        btn_clear = widgets.Button(description="clear")

        btn_submit.on_click(self._cb_submit)
        btn_clear.on_click(self._cb_clear)

        display(widgets.Box([
            btn_submit,
            btn_clear,
        ]))
        if len(self._data) > 1:
            for plot in self._config["plots"]:
                self._data.plot(**plot)
    
    def _save(self):
        self._data.to_csv(self._config["filename"], index=False)
        
    def _cb_submit(self, sender):
        new_row = {}
        for field in self._config["fields"]:
            new_row[field["name"]] = field["type"](field["txt_value"].value)

        self._data = self._data.append(new_row, ignore_index=True)
        self._save()
        self.render_form()

    def _cb_clear(self, sender):
        self._data = pd.DataFrame()
        self._save()
        self.render_form()
    
