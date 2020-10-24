POETRY = $(shell which poetry)
POETRY_ENV_DIR = $(shell $(POETRY) env info -p)
POETRY_ENV = $(shell basename $(POETRY_ENV_DIR))

help: ## Show this help.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: deps
deps: ## Install project dependencies
	$(POETRY) install

.PHONY: nuke-deps
nuke-deps: ## Nuke the deps from orbit
	$(POETRY) env remove $(POETRY_ENV)

.PHONY: repl
repl: ## Launch the project repl
	$(POETRY) run python
