#!/bin/sh
# This checks to see if you're using a gitignore and either creates one or
# adds necessary file ignores to existing one.
if [-f '.gitignore']
then
  echo 'gitignore exits in root adding QA ignores'
  echo '\n' >> .gitignore
  cat qa/.gitignore >> .gitignore
else
  echo 'gignore does not exist, creating it in root'
	cat qa/.gitignore > .gitignore
fi

if [-f 'Makefile']
then
  echo 'Makefile exists copying QA commands into it'
	echo '\n' >> Makefile
	cat qa/Makefile >> Makefile
else
  echo 'Makefile does not exist copying QA commands into it'
	cat qa/Makefile > Makefile
fi
