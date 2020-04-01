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


def test_index_route_get_component_title(live_server, selenium):
    selenium.get(live_server.url())
    assert "Task Form" in selenium.page_source


def test_index_route_return_true_if_form_was_rendered(live_server, selenium):
    selenium.get(live_server.url())
    selenium.find_element_by_name("task")
    selenium.find_element_by_id("form-vue")
    selenium.find_element_by_tag_name("form")
