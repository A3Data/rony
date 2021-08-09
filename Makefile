#####################################################
# Makefile containing shortcut commands for project #
#####################################################

# MACOS USERS:
#  Make should be installed with XCode dev tools.
#  If not, run `xcode-select --install` in Terminal to install.

# WINDOWS USERS:
#  1. Install Chocolately package manager: https://chocolatey.org/
#  2. Open Command Prompt in administrator mode
#  3. Run `choco install make`
#  4. Restart all Git Bash/Terminal windows.

.PHONY: tf-validate
tf-validate:
	docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/validate_terraform.sh $(module)

.PHONY: test-lint
 test-lint:
	docker-compose -f ./CI/docker-compose.yml run --rm rony-ci ./CI/scripts/test_and_lint.sh $(module)