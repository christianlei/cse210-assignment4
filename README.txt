Assignment 4
Christian Lei

To organize code:
A dist directory holds the antlr generated files, including WhileVisitor
The test directory holds the self tests
Entities hold the AST Objects
And the while.py goes in the main folder along with While.g4, Makefile and the test shell script.


To run code:
create python virtual env
install antlr with pip3 in virtual env
run ./test.sh in the assignment2 directory

If the code doesn't run, you might need to run
antlr -Dlanguage=Python3 While.g4 -o dist -visitor

Make sure to save a copy of the included visitor file, because that needs to be copied in to the generated visitor file.

libraries used:
antlr


Code citations:
https://stackoverflow.com/questions/11479816/what-is-the-python-equivalent-for-a-case-switch-statement
https://keyholesoftware.com/2020/01/21/an-antlr4-based-expression-parser/
https://github.com/raguiar2/calculator
https://stackoverflow.com/questions/15610183/if-else-statements-in-antlr-using-listeners