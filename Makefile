Assignment4.pdf : main.tex Ph20_Set2_Plot.png
	pdflatex main.tex

Ph20_Set2_Plot.png : Ph20_Set2.py
	python Ph20_Set2.py e^x 0 1 100 1
