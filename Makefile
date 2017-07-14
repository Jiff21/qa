
setup:
	ifneq ("$(wildcard $(../.gitignore))","")
		.gitignore > '\n\n'
		.gitignore > .gitignore
	else
		cp .gitignore ../
	endif

# if [ -a .gitignore ] ; \
# then \
# 	.gitignore > ../.gitignore
# else \
# 	cp .gitignore ../
# fi \


.PHONY: test_all
test_all: test

.PHONY: test_unit
test_unit:
	tox
