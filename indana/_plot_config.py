from indana._algorithm_config import AlgorithmConfig

class PlotConfig(AlgorithmConfig):
    def __init__(self, data, fields=[]):
        config = {
            "fields": [
                {
                    "name": "x",
                    "type": str,
                    "values": list(data.columns.values),
                }, {
                    "name": "y",
                    "type": str,
                    "values": list(data.columns.values),
                }, {
                    "name": "kind",
                    "type": str,
                    "values": [
                        "scatter",
                        "line",
                        "bar",
                    ]
                }
            ]
        }
        config["fields"] += fields
        AlgorithmConfig.__init__(self,  data.plot, config)
