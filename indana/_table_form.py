from os import path

from IPython.display import display, clear_output
from ipywidgets import widgets
import pandas as pd

from indana._config_base import ConfigBase

class TableForm(ConfigBase):
    def __init__(self, config):
        ConfigBase.__init__(self, config)

        if path.isfile(self._config["filename"]):
            self._data = pd.read_csv(self._config["filename"])
        else:
            self._data = pd.DataFrame()
        
        self.register_submit(self._cb_submit_tbl)

    @property
    def data(self):
        return self._data
            
    def render_form(self):
        clear_output()

        display(self._data)
        
        ConfigBase.render_form(self, clear=False)

        btn_clear = widgets.Button(description="clear")
        btn_clear.on_click(self._cb_clear)
        display(btn_clear)

        if len(self._data) > 1:
            for plot in self._config["plots"]:
                self._data.plot(**plot)
    
    def _save(self):
        self._data.to_csv(self._config["filename"], index=False)
        
    def _cb_submit_tbl(self, values):
        self._data = self._data.append(values, ignore_index=True)
        self._save()
        self.render_form()
        
    def _cb_clear(self, sender):
        self._data = pd.DataFrame()
        self._save()
        self.render_form()
