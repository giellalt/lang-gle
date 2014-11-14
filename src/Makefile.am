## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

# always build . last here, and tagsets have to be built after morphology
SUBDIRS = phonology morphology filters phonetics hyphenation orthography syntax transcriptions tagsets .

####### Automake targets: ########

# Define target variables first, before assigning to them:
GT_ANALYSERS_HFST=
GT_GENERATORS_HFST=
GT_ANALYSERS_XFST=
GT_GENERATORS_XFST=

#### Local modifications in *fst processing: ####
####
#### Copy the fallback targets, and rename them to the desired targets. Then:
#### Replace the 'cp' command (Xerox) / Prepend the hfst-invert command (Hfst -
#### remember to move the $<) with whatever you need to complete
#### the processing to get the final target transducer.
#### Remember to add the dependencies as well.
#### Also make sure that HFST and Xerox processing are the same.
####
#### If you add new transducers to be built, you need to add them to the
#### relevant variable, e.g.:
####
#### if CAN_HFST
#### GT_GENERATORS_HFST+=generator-oahpa-gt-norm.hfst
#### endif
####
#### NB!!!! The HFST targets should get a hyphen after 'analyser'/'generator'
#### respectively, to make the local targets minimally different from and
#### slightly more specific than the fallback targets. This is to avoid warnings
#### about duplicate targets. That is, the local targets should looke like:
####


##################################################################
#### BEGIN: Add local processing instructions BELOW this line ####
##################################################################
analyser-%.hfst: analyser-%.tmp.hfst \
				 $(srcdir)/fixes.regex \
				 $(srcdir)/fixes-good.regex
	$(AM_V_RGX2FST)$(HFST_REGEXP2FST) -S $(srcdir)/fixes.regex -o fixes.hfst
	$(AM_V_RGX2FST)$(HFST_REGEXP2FST) -S $(srcdir)/fixes-good.regex \
								 -o fixes-good.hfst
	$(AM_V_GEN)$(HFST_COMPOSE) -F fixes.hfst $< |\
		$(HFST_DISJUNCT) fixes-good.hfst |\
		$(HFST_INVERT) |\
		$(HFST_MINIMIZE) |\
		$(HFST_FST2FST) -f olw -o $@

########################################################
#### Add language-specific transducer targets here: ####

#### Xerox transducers:
if CAN_XFST
GT_ANALYSERS_XFST+=
GT_GENERATORS_XFST+=
endif # CAN_XFST

#### HFST transducers
if CAN_HFST
GT_ANALYSERS_HFST+=analyser-verbs.hfst analyser-nouns.hfst analyser-adj.hfst \
				   analyser-others.hfst \
				   analyser-all.hfst
GT_GENERATORS_HFST+=
endif # CAN_HFST

#################################################
#### Add language-specific build rules here: ####

analyser-verbs.hfst: morphology/gle.verb-all.hfst phonology/gle-phon.verbs.hfst
	hfst-compose-intersect -1 morphology/gle.verb-all.hfst -2 phonology/gle-phon.initialmutation.hfst |\
	hfst-compose-intersect -2 phonology/gle-phon.verbs.hfst |\
	hfst-compose-intersect -2 phonology/gle-tidy.hfst |\
		hfst-minimize -o $@

analyser-nouns.hfst: morphology/gle.noun-all.hfst phonology/gle-phon.nouns.hfst
	hfst-compose-intersect -1 morphology/gle.noun-all.hfst -2 phonology/gle-phon.initialmutation.hfst |\
	hfst-compose-intersect -2 phonology/gle-phon.nouns.hfst |\
	hfst-compose-intersect -2 phonology/gle-tidy.hfst |\
		hfst-minimize -o $@

analyser-adj.hfst: morphology/gle.adj.hfst phonology/gle-phon.nouns.hfst
	hfst-compose-intersect -1 morphology/gle.adj.hfst -2 phonology/gle-phon.nouns.hfst |\
	hfst-compose-intersect -2 phonology/gle-phon.nouns.hfst |\
	hfst-compose-intersect -2 phonology/gle-tidy.hfst |\
		hfst-minimize -o $@

analyser-others.hfst: morphology/gle.others.hfst
	hfst-minimize $< -o $@

analyser-all.hfst: analyser-verbs.hfst analyser-nouns.hfst analyser-adj.hfst \
	analyser-others.hfst
	hfst-disjunct analyser-verbs.hfst analyser-nouns.hfst |\
		hfst-disjunct - analyser-adj.hfst |\
		hfst-disjunct - analyser-others.hfst |\
		hfst-invert |\
		hfst-minimize -o $@

##################################################################
#### END: Add local processing instructions ABOVE this line ######
##################################################################

#### HFST transducer fallback target:
#### - inversion is needed FOR THE ANALYSER because the hfst model is upside
#### down compared to Xerox AT APPLICATION TIME. The other command makes the
#### final transducer ready for use.
analyser%.hfst: analyser%.tmp.hfst
	$(AM_V_INVERT)$(HFST_INVERT) -i $< -o $@

generator%.hfst: generator%.tmp.hfst
	$(AM_V_CP)cp -f $< $@

#### Xerox transducer fallback target:
%.xfst: %.tmp.xfst
	$(AM_V_CP)cp -f $< $@

include $(top_srcdir)/am-shared/src-dir-include.am
