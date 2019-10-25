VENV:=/tmp/venv/gcode
BIN=${VENV}/bin
PYTHON=${BIN}/python3
PIP=${BIN}/pip

${PYTHON}:
	python3 -mvenv ${VENV}
	${PIP} install --upgrade wheel setuptools pip
	${PIP} install -r requirements.txt
	${PIP} install -r requirements_test.txt

.PHONY: clean
clean:
	rm -rf ${VENV}

.PHONY: watch
watch:
	watcher -cmd "pre-commit run --all-files" -startcmd -keepalive -interval "2s" gcode/*.py tests/*.py
