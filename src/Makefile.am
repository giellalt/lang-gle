## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

# always build . last here, and tagsets have to be built after morphology
SUBDIRS = fst filters phonetics hyphenation orthography cg3 transcriptions tagsets .

####### Automake targets: ########

# Define target variables first, before assigning to them:
GT_ANALYSERS=
GT_GENERATORS=

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
#### GT_GENERATORS+=generator-oahpa-gt-norm.hfst
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

########################################################
#### Add language-specific transducer targets here: ####

#### Xerox transducers:
if CAN_XFST
GT_ANALYSERS+=fixes.xfst fixes-good.xfst
GT_GENERATORS+=
endif # CAN_XFST

#### HFST transducers
if CAN_HFST
GT_ANALYSERS+=fixes.hfst fixes-good.hfst
GT_GENERATORS+=
endif # CAN_HFST

#### FOMA transducers
if CAN_FOMA
GT_ANALYSERS+=fixes.foma fixes-good.foma
GT_GENERATORS+=
endif # CAN_FOMA

#################################################
#### Add language-specific build rules here: ####

analyser-verbs.%: fst/gle.verb-all.% \
					 fst/phonology.verb.compose.% \
					 fst/phonology.init.compose.% \
					 fst/phonology.tidy.compose.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
				@\"fst/gle.verb-all.$*\"         \
			.o. @\"fst/phonology.init.compose.$*\" \
			.o. @\"fst/phonology.verb.compose.$*\" \
			.o. @\"fst/phonology.tidy.compose.$*\" \
			;\n\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

analyser-nouns.%: fst/gle.noun-all.% \
					 fst/phonology.nounadj.compose.% \
					 fst/phonology.init.compose.% \
					 fst/phonology.tidy.compose.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
				@\"fst/gle.noun-all.$*\"            \
			.o. @\"fst/phonology.init.compose.$*\"    \
			.o. @\"fst/phonology.nounadj.compose.$*\" \
			.o. @\"fst/phonology.tidy.compose.$*\"    \
			;\n\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

analyser-adj.%: fst/gle.adj.% \
			    fst/phonology.nounadj.compose.% \
			    fst/phonology.init.compose.% \
			    fst/phonology.tidy.compose.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
				@\"fst/gle.adj.$*\"                 \
			.o. @\"fst/phonology.init.compose.$*\"    \
			.o. @\"fst/phonology.nounadj.compose.$*\" \
			.o. @\"fst/phonology.tidy.compose.$*\"    \
			;\n\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

analyser-others.hfst: fst/gle.others.hfst
	$(AM_V_HMINIM)$(HFST_MINIMIZE) $< -o $@

analyser-others.%: fst/gle.others.%
	$(AM_V_CP)cp $< $@

analyser-all.%: analyser-verbs.% \
				analyser-nouns.% \
				analyser-adj.% \
				analyser-others.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
			[ @\"analyser-verbs.$*\"   \
			| @\"analyser-nouns.$*\"   \
			| @\"analyser-adj.$*\"     \
			| @\"analyser-others.$*\" ]\
			;\n\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

### Final processing of the raw analyser/generator:
generator-raw-gt-desc.hfst: analyser-all.hfst \
				 fixes.hfst \
				 fixes-good.hfst
	$(AM_V_XFST_TOOL)$(PRINTF) "\
			set harmonize-flags ON\n\
			read regex \
			[   @\"fixes.hfst\"          \
			.o. @\"$<\"                  \
			] | @\"fixes-good.hfst\"     \
			;\n\
		 save stack $@\n\
		 quit\n" | $(HFST_XFST) -p $(MORE_VERBOSITY) $(HFST_FORMAT)

analyser-raw-gt-desc.hfst: generator-raw-gt-desc.hfst
	$(AM_V_CP)cp $< $@

# Wrap processing of Foma and Xfst in a define:
analyser-raw-gt-desc.%: analyser-all.% \
				 fixes.% \
				 fixes-good.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
			[   @\"fixes.$*\"          \
			.o. @\"$<\"                 \
			] | @\"fixes-good.$*\"     \
			;\n\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

##################################################################
#### END: Add local processing instructions ABOVE this line ######
##################################################################

include $(top_srcdir)/am-shared/src-dir-include.am
