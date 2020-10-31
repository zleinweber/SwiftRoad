POETRY = $(shell which poetry)
POETRY_ENV_DIR = $(shell $(POETRY) env info -p)
POETRY_ENV = $(shell basename $(POETRY_ENV_DIR))
SWIFTROAD_DIR = swiftroad

help: ## Show this help.
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: deps
deps: ## Install project dependencies
	$(POETRY) install

.PHONY: nuke-deps
nuke-deps: ## Nuke the deps from orbit
	$(POETRY) env remove $(POETRY_ENV)

.PHONY: repl
repl: ## Launch the project repl
	$(POETRY) run python $(SWIFTROAD_DIR)/manage.py shell

.PHONY: runserver
runserver: ## Run the django dev server
	$(POETRY) run python $(SWIFTROAD_DIR)/manage.py runserver

.PHONY: check
check: ## Run django checks
	$(POETRY) run python $(SWIFTROAD_DIR)/manage.py check

.PHONY: migrations
migrations: ## Run Django manage.py makemigrations
	$(POETRY) run python $(SWIFTROAD_DIR)/manage.py makemigrations

.PHONY: migrate
migrate: ## Run Django manage.py migrate
	$(POETRY) run python $(SWIFTROAD_DIR)/manage.py migrate

.PHONY: createsuperuser
createsuperuser: ## Create Django Admin Site Superuser
	$(POETRY) run python $(SWIFTROAD_DIR)/manage.py createsuperuser

.PHONY: test
test: ## Run tests
	$(POETRY) run python $(SWIFTROAD_DIR)/manage.py test activities swiftroad

.PHONY: black
black: ## enblackenate the world
	$(POETRY) run black $(SWIFTROAD_DIR)/activities
	$(POETRY) run black $(SWIFTROAD_DIR)/swiftroad

.PHONY: pylint
pylint: ## Run pylint
	$(POETRY) run pylint $(SWIFTROAD_DIR)/activities
	$(POETRY) run pylint $(SWIFTROAD_DIR)/swiftroad