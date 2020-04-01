.PHONY: test
test:
	@pytest -vv

.PHONY: format
format:
	@black flask_vuejs sample_app tests

.PHONY: check
check:
	@black flask_vuejs sample_app tests --check


