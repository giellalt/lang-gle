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
	
.DELETE_ON_ERROR: iat.gle-eng.tsv
iat.gle-eng.tsv: IAT_export/export_EN_GA_2015-05-15_All_Langs.tbx
	. env/bin/activate && python xml_to_tsv.py iat_tsv.yaml $^ > iat.gle-eng.tsv

.DELETE_ON_ERROR: iat.gle-eng.xml
iat.gle-eng.xml: iat.gle-eng.tsv
	. env/bin/activate && python render_tsv.py iat.gle-eng.j2 $^ > $@.tmp


# TODO: combine all the output .xml files into one lexicon for NDS, or Oahpa, etc.

# iat.gle-eng.xml
all: wordnet.gle-eng.xml

clean: 
	rm -rf wordnet.tsv wordnet.ga.tsv tmp/*.tsv
	rm -rf apertium-gle
	rm -rf wordnet-gaeilge
	rm -rf *.tmp
