#####################################################
# Makefile containing shortcut commands for project #
#####################################################

# MACOS USERS:
#  Make should be installed with XCode dev tools.
#  If not, run `xcode-select --install` in Terminal to install.

# WINDOWS USERS:
#  1. Install Chocolately package manager: https:/chocolatey.org/
#  2. Open Command Prompt in administrator mode
#  3. Run `choco install make`
#  4. Restart all Git Bash/Terminal windows.

SHELL := /bin/bash

.PHONY: tf-fmt
tf-fmt:
	docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/format.sh

.PHONY: tf-show
tf-show:
	docker-compose -f ./CI/docker-compose.yml run --rm rony-ci -c "cd infrastructure; terraform show"

.PHONY: build-dev
build-dev:
	./CI/scripts/build_and_push.sh dev

.PHONY: build-staging
build-staging:
	./CI/scripts/build_and_push.sh staging

.PHONY: build-prod
build-prod:
	./CI/scripts/build_and_push.sh prod

.PHONY: plan-dev
plan-dev:
	source ./CI/scripts/get_credentials.sh; docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/plan.sh dev

.PHONY: plan-staging
plan-staging:
	source ./CI/scripts/get_credentials.sh; docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/plan.sh staging

.PHONY: plan-prod
plan-prod:
	source ./CI/scripts/get_credentials.sh; docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/plan.sh prod


.PHONY: apply-dev
apply-dev:
	source ./CI/scripts/get_credentials.sh; docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/apply.sh dev

.PHONY: apply-staging
apply-staging:
	source ./CI/scripts/get_credentials.sh; docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/apply.sh staging

.PHONY: apply-prod
apply-prod:
	source ./CI/scripts/get_credentials.sh; docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/apply.sh prod


.PHONY: destroy-dev
destroy-dev:
	source ./CI/scripts/get_credentials.sh; docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/destroy.sh dev

.PHONY: destroy-staging
destroy-staging:
	source ./CI/scripts/get_credentials.sh; docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/destroy.sh staging

.PHONY: destroy-prod
destroy-prod:
	source ./CI/scripts/get_credentials.sh; docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/destroy.sh prod
