all: static image

## format: auto format the code
format:
	black monitoring_system $(CHECK_FORMAT) --line-length=120
	isort --profile black monitoring_system

## static: run static code analysis
static:	flake8 type-check

## flake8: run flake8 code analysis
flake8: format
	flake8 monitoring_system --max-line-length=120 --extend-ignore=E203

## type-check: run mypy type checks
type-check: format
	mypy --ignore-missing-imports --cache-dir=./build/.mypy_cache -p monitoring_system

## image: build the monitoring-system image
up:
	docker build --target monitoring-system -t monitoring-system .

## help: show makefile actions
help: Makefile
	@printf '\nMakeflie Actions:\n\n'
	@sed -n 's/^##//p' $<
