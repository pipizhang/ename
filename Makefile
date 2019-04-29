SHELL := /bin/bash

help: ## This help message
	@echo "Usage: make [target]"
	@echo "Commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY:vclean
vclean: ## Clean VirtualEnv
	@exec rm -rf ./venv

.PHONY:vinstall
vinstall: ## Setup VirtualEnv
	@exec virtualenv --no-site-packages venv

.PHONY:install
install: ## Install packages
	pip install --upgrade pip
	pip install -r requirements.txt
