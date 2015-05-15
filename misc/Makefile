.PHONY: externals
apertium-gle:
	svn checkout svn://svn.code.sf.net/p/apertium/svn/incubator/apertium-gle apertium-gle

wordnet-gaeilge:
	git clone https://github.com/kscanne/wordnet-gaeilge

externals: apertium-gle wordnet-gaeilge

.PHONY: environment
environment:
	virtualenv env
	. env/bin/activate
	pip install -r requirements.txt

wordnet.tsv: wordnet-gaeilge/en2wn.po
	. env/bin/activate && python export_po_wordnet.py $^ > $@.tmp
	cat $@.tmp | grep -v '^DUMMY' > $@.d.tmp
	cat $@.d.tmp | awk 'NR == 1; NR > 1 {print $0 | "sort -n"}' > $@
	rm $@.d.tmp $@.tmp

all: wordnet.tsv
