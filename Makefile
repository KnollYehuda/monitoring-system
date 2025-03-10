all: static start

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
	chown -R 1000:1000 ./monitoring_system/*

start:
	make up
	make down

## image: build the monitoring-system image
up:
	mkdir -p /tmp/monitoring_system/celery
	docker compose up -d
	@echo "\n\033[1;34m== Monitoring System Services ==\033[0m\n"
	@echo "\033[1;32mGrafana:\033[0m             http://localhost:3000  \033[1;37m(default credentials: admin/admin)\033[0m"
	@echo "\033[1;33mPrometheus:\033[0m          http://localhost:9090"
	@echo "\033[1;35mCelery Flower:\033[0m       http://localhost:5555"
	@echo "\033[1;36mRabbitMQ Management:\033[0m http://localhost:15672 \033[1;37m(default credentials: guest/guest)\033[0m"
	@echo "\n\033[1;34m================================\033[0m\n"
	@if [ "$(TIME_OUT)" -gt 0 ]; then \
        echo "\033[1;33mSleeping for $(TIME_OUT) seconds...\033[0m"; \
		sleep $(TIME_OUT); \
    else \
        read -p "Press any key to exit" userInput; \
    fi


down:
	docker compose down
	rm -r /tmp/monitoring_system/celery

## help: show makefile actions
help: Makefile
	@printf '\nMakeflie Actions:\n\n'
	@sed -n 's/^##//p' $<
