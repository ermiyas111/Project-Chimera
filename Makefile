IMAGE_NAME ?= project-chimera
PYTHON ?= python

.PHONY: setup build test spec-check

setup:
	$(PYTHON) -m venv .venv
	. .venv/bin/activate; pip install --upgrade pip; pip install -r requirements.txt

build:
	docker build -t $(IMAGE_NAME) .

test:
	docker run --rm $(IMAGE_NAME) pytest tests/

spec-check:
	@missing=0; \
	for d in specs/*; do \
		if [ -d $$d ]; then \
			for f in spec.md functional.md technical.md; do \
				if [ ! -f "$$d/$$f" ]; then \
					echo "Missing $$f in $$d"; \
					missing=1; \
				fi; \
			done; \
		fi; \
	done; \
	if [ $$missing -ne 0 ]; then \
		echo "Spec check failed"; \
		exit 1; \
	else \
		echo "Spec check passed"; \
	fi
