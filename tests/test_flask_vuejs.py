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


def test_index_route_return_true_if_hello_marcus_exists(live_server, selenium):
    selenium.get(live_server.url())
    print(selenium.page_source)
    assert "Hello Marcus" in selenium.page_source


def test_index_route_get_presentation_title_component(live_server, selenium):
    selenium.get(live_server.url())
    assert "Apresentation" in selenium.page_source


def test_index_route_return_true_if_component_has_been_mounted(live_server, selenium):
    selenium.get(live_server.url())
    selenium.find_element_by_id("presentation")
    selenium.find_element_by_tag_name("div")
