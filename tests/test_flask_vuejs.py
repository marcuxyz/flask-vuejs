

def test_import_vue():
    try:
        from flask_vue import Vue
    except ImportError:
        pass


def test_index_route_return_status_code_200(client):
    res = client.get("/")
    assert res.status_code == 200


def test_index_route_return_true_when_app_id_is_found(client):
    res = client.get("/")
    assert 'id="app"' in res.get_data(as_text=True)


def test_index_route_return_true_if_component_was_imported(client):
    res = client.get("/")
    assert "<script src='/static/components/form.js'></script>" in res.get_data(
        as_text=True
    )

def test_index_route_get_component_title(web_client):
    web_client.get('http://localhost:5000/')
    assert "Task Form" in web_client.page_source

def test_index_route_return_true_if_form_was_rendered(web_client):
    web_client.get('http://localhost:5000/')
    web_client.find_element_by_name("task")
    web_client.find_element_by_id("form-vue")
    web_client.find_element_by_tag_name("form")
