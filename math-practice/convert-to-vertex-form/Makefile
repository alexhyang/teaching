#!make
# convert-to-vertex-form.pdf: convert-to-vertex-form.tex
	# pdflatex convert-to-vertex-form.tex

solutions.txt: convert-to-vertex-form.tex
	cat convert-to-vertex-form.tex | rg -e '\$$.*\$$' | \
		sed -E 's/^.*\\item \$$(.*)\$$$$/\1/' > quadratic-expressions.txt
	cat quadratic-expressions.txt | sed -E 's/^y = (.*)$$/\1/' > raw-expressions.txt
	python3 Calculator.py -c raw-expressions.txt > raw-coefficients.txt
	python3 Calculator.py - raw-expressions.txt > raw-solutions.txt
	paste quadratic-expressions.txt raw-coefficients.txt raw-solutions.txt > solutions.txt
	rm raw-*.txt quadratic-expressions.txt
	cat solutions.txt

