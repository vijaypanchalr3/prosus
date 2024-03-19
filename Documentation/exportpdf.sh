#!/bin/bash -
cd container/
latexmk -pdflatex='lualatex -shell-escape -interaction nonstopmode' -pdf -f documentation.tex

# latexmk -c

mv documentation.pdf ../
cd ../
