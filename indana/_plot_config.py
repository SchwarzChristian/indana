from indana._algorithm_config import AlgorithmConfig

class PlotConfig(AlgorithmConfig):
    def __init__(self, data, fields=[]):
        config = {
            "fields": [
                {
                    "name": "x",
                    "type": str,
                    "default": "x",
                }, {
                    "name": "y",
                    "type": str,
                    "default": "y",
                }, {
                    "name": "kind",
                    "type": str,
                    "default": "scatter",
                }
            ]
        }
        config["fields"] += fields
        AlgorithmConfig.__init__(self,  data.plot, config)
