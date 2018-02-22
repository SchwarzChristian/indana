from indana._config_base import ConfigBase

def test_main():
    cb = ConfigBase({
        "fields": [{
            "name": "field_1",
            "type": int,
            "default": 23,
        }],
    })
    cb.render_form()