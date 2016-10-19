test:
	coverage run -m unittest test_rpn

run:
	python rpn.py

.PHONY: test run

