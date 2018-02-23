from indana._plot_config import PlotConfig
import pandas as pd

def test_main():
    data = pd.DataFrame({
        "a": [1, 2, 3],
        "b": [4, 5, 6],
        "c": [1, 3, 5],
    })

    pc = PlotConfig(data)
    pc.render_form()
    pc.run()
    