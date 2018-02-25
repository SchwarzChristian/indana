from indana._algorithm_config import AlgorithmConfig

class HistConfig(AlgorithmConfig):
    def __init__(self, data, fields=[], submit_name="plot"):
        self._data = data
        self._fields = [
            {
                "name": "field",
                "type": str,
                "values": list(data.columns.values),
            }
        ]
        self._fields += fields
        AlgorithmConfig.__init__(self,  self.plot, self._fields, submit_name=submit_name)

    def plot(self, **args):
        field = args["field"]
        args = { k: v for k, v in args.items() if not k == "field" }
        self._data[field].hist(**args)
