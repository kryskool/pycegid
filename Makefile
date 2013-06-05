CWD         = $(shell pwd)

XUNIT_PATH  = ./jenkins.xml

test:
	PYTHONPATH=$(CWD) py.test -v tests/

jenkins:
	PYTHONPATH=$(CWD) py.test -v --junitxml=$(XUNIT_PATH) tests/
