test:
	coverage run -m unittest test_rpn

run:
	python3 rpn.py

.PHONY: test run

