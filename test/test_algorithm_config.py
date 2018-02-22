from indana._algorithm_config import AlgorithmConfig

is_algorithm_run = False

def test_algorithm_config():
    global is_algorithm_run
    def algorithm(data, param):
        global is_algorithm_run
        is_algorithm_run = True

        assert data == "23"
        assert param == 42

    ac = AlgorithmConfig(algorithm, {
        "fields": [
            {
                "name": "data",
                "type": str,
                "default": "23",
            }, {
                "name": "param",
                "type": int,
                "default": 42,
            },
        ]
    })

    ac.render_form()
    ac.run()
    assert is_algorithm_run
    