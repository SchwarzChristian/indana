from indana._algorithm_config import AlgorithmConfig
import numpy as np

class PlotConfig(AlgorithmConfig):
    def __init__(self, data, fields=[], submit_name="plot"):
        color_maps = [
            "Accent", "Blues", "BrBG", "BuGn", "BuPu", 
            "CMRmap", "Dark2", "GnBu", "Greens", "Greys", 
            "OrRd", "Oranges", "PRGn", "Paired", "Pastel1", 
            "Pastel2", "PiYG", "PuBu", "PuBuGn", "PuOr", 
            "PuRd", "Purples", "RdBu", "RdGy", "RdPu", 
            "RdYlBu", "RdYlGn", "Reds", "Set1", "Set2", 
            "Set3", "Spectral", "Vega10", "Vega20", "Vega20b",
            "Vega20c", "Wistia", "YlGn", "YlGnBu", "YlOrBr", 
            "YlOrRd", "afmhot", "autumn", "binary", "bone", 
            "brg", "bwr", "cool", "coolwarm", "copper", 
            "cubehelix", "flag", "gist_earth", "gist_gray", "gist_heat", 
            "gist_ncar", "gist_rainbow", "gist_stern", "gist_yarg", "gnuplot", "gnuplot2", 
            "gray", "hot", "hsv", "inferno", 
            "jet", "magma", "nipy_spectral", "ocean", "pink", 
            "plasma", "prism", "rainbow", "seismic", "spectral", 
            "spring", "summer", "tab10", "tab20", "tab20b", 
            "tab20c", "terrain", "viridis", "winter",
        ]
        self._data = data
        values = [ x for x in data.columns.values if data[x].dtype in [ np.number, np.int0 ] ]
        self._fields = [
            {
                "name": "x",
                "description": "x axis",
                "type": str,
                "values": values,
            }, {
                "name": "y",
                "description": "y axis",
                "type": str,
                "values": values,
            }, {
                "name": "c",
                "description": "color",
                "type": str,
                "values": values,
            }, {
                "name": "kind",
                "type": str,
                "values": [ "scatter", "line", "bar" ]
            }, {
                "name": "colormap",
                "type": str,
                "values": color_maps,
                "default": "tab20b",
            }, {
                "name": "rev_cmap",
                "description": "reverse colormap",
                "type": bool,
                "default": False,
            }
        ]
        self._fields += fields
        AlgorithmConfig.__init__(self,  self.plot, self._fields, submit_name=submit_name)

    def plot(self, **args):
        if not args["kind"] == "scatter":
            del args["c"]
        self._data.plot( **args)
