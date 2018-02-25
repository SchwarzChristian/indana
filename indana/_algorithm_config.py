from indana._config_base import ConfigBase
from IPython.display import display

class AlgorithmConfig(ConfigBase):
    """
    Can be used to configure and run some kind of algorithm

    Parameter
    =========

    algorithm: method to run
    config: parameter configuration
    """
    def __init__(self, algorithm, fields, submit_name="run"):
        ConfigBase.__init__(self, { "fields": fields }, submit_name=submit_name)
        self._algorithm = algorithm
        self.register_submit(self.run)

    def run(self, values = None):
        """
        runs the algorithm with the currently configured values
        """
        values = self.current_values
        for field in self._config["fields"]:
            field["default"] = values[field["name"]]
        self.render_form()
        result = self._algorithm(**self.current_values)
        display(result)
        return result
