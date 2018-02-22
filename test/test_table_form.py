from indana._table_form import TableForm

def test_main():
    tf = TableForm({
        "fields": [{
            "name": "field_1",
            "type": int,
            "default": 23,
        }],
        "filename": "test.csv",
    })
    tf.render_form()