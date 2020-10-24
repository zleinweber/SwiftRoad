POETRY = $(shell which poetry)
POETRY_ENV_DIR = $(shell $(POETRY) env info -p)
POETRY_ENV = $(shell basename $(POETRY_ENV_DIR))
SWIFTROAD_DIR = swiftroad

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

.PHONY: runserver
runserver: ## Run the django dev server
	$(POETRY) run python $(SWIFTROAD_DIR)/manage.py runserver

.PHONY: migrate
migrate: ## Run Django manage.py migrate
	$(POETRY) run python $(SWIFTROAD_DIR)/manage.py migrate

.PHONY: black
black: ## enblackenate the world
	$(POETRY) run black $(SWIFTROAD_DIR)/journal
	$(POETRY) run black $(SWIFTROAD_DIR)/swiftroad

.PHONY: pylint
pylint: ## Run pylint
	$(POETRY) run pylint $(SWIFTROAD_DIR)/journal
	$(POETRY) run pylint $(SWIFTROAD_DIR)/swiftroad