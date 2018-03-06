LINT_FILES = $(shell find cobinhood -name '*.py' -type f | sort)

lint:
	@pep8 $(LINT_FILES)
	@pylint --rcfile=$(CURDIR)/pylintrc --load-plugins pylint_quotes $(LINT_FILES)
