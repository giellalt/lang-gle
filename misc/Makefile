#


# TODO: installation of https://github.com/harelba/q


.PHONY: apertium-gle
apertium-gle:
	svn checkout svn://svn.code.sf.net/p/apertium/svn/incubator/apertium-gle apertium-gle

.PHONY: wordnet-gaeilge
wordnet-gaeilge:
	git clone https://github.com/kscanne/wordnet-gaeilge

.PHONY: externals
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

tmp/wordnet.ga.%.tsv: wordnet-gaeilge/ga-data.%.po
	. env/bin/activate && python export_po_wordnet_mono.py $^ > $@.tmp
	cat $@.tmp | awk 'NR == 1; NR > 1 {print $0 | "sort -n"}' > $@
	rm $@.tmp

Q := "SELECT gle_words from ./wordnet.tsv LIMIT 5"

Q := "SELECT * FROM ./wordnet.tsv definitions JOIN ./wordnet.ga.pos.tsv semantics ON (definitions.gle_words = semantics.gle_words)"

# -t - tsv
# -H - use header in input
# -O - output header
wordnet.merged.tsv: wordnet.tsv \
				    wordnet.ga.tsv
	q -tHO -q merge.sql > wordnet.merged.tsv

# awk one-liner to merge tsvs and remove the header from all subsequent
# files
wordnet.ga.tsv: tmp/wordnet.ga.noun.tsv \
				tmp/wordnet.ga.verb.tsv \
				tmp/wordnet.ga.adv.tsv \
				tmp/wordnet.ga.adj.tsv
	awk 'FNR==1 && NR!=1{next;}{print}' $^ > $@

.DELETE_ON_ERROR: wordnet.gle-eng.xml wordnet.gle-eng.xml.tmp
wordnet.gle-eng.xml: wordnet.merged.tsv
	. env/bin/activate && python render_tsv.py entry.j2 $^ > $@.tmp
	cat $@.tmp | xmllint --format - > $@

all: wordnet.tsv \
	 wordnet.ga.tsv \
	 wordnet.merged.tsv \
	 wordnet.gle-eng.xml
