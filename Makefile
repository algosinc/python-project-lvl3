install:
	poetry install

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run coverage run pytest

test-coverage:
	poetry run pytest --cov=page_loader/ tests/ --cov-report xml

lint:
	poetry run flake8 --count --max-line-length=127 page-loader
	poetry run flake8 --count --max-line-length=127 tests
	poetry run mypy page_loader

selfcheck:
	poetry check

check:
	selfcheck test lint

build: check
	rm -Rvf dist/
	poetry build

.PHONY: install test lint selfcheck check build
