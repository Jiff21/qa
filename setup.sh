#!/bin/sh

echo 'Copying or adding qa .gitignores into the root project'
cat qa/.gitignore >> .gitignore
echo 'Copying or adding qa Makefile into the root project'
cat qa/Makefile >> Makefile
echo 'Only run this command once its not smart and will double these.'
