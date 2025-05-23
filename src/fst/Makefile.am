## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

# always build . last here, and tagsets have to be built after morphology
SUBDIRS = morphology filters phonetics syllabification orthography transcriptions tagsets . test

####### Automake targets: ########

# Define target variables first, before assigning to them:
GT_ANALYSERS=
GT_GENERATORS=
CUSTOM_FSTS=

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
#### analyser-%.hfst: analyser-%.tmp.hfst
#### generator-%.hfst: generator-%.tmp.hfst

##################################################################
#### BEGIN: Add local processing instructions BELOW this line ####
##################################################################

########################################################
#### Add language-specific transducer targets here: ####


#### HFST transducers
if CAN_HFST
GT_ANALYSERS+=fixes.hfst fixes-good.hfst
GT_GENERATORS+=

if WANT_CUSTOM_FSTS
CUSTOM_FSTS+=
endif # WANT_CUSTOM_FSTS

endif # CAN_HFST

#### FOMA transducers
if CAN_FOMA
GT_ANALYSERS+=fixes.foma fixes-good.foma
GT_GENERATORS+=

if WANT_CUSTOM_FSTS
CUSTOM_FSTS+=
endif # WANT_CUSTOM_FSTS

endif # CAN_FOMA
#################################################
#### Add language-specific build rules here: ####

.generated/analyser-verbs.%: morphology/gle.verb-all.% \
				  morphology/phonology.verb.compose.% \
				  morphology/phonology.init.compose.% \
				  morphology/phonology.tidy.compose.% $(GENDIR)
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
						@\"morphology/gle.verb-all.$*\"		 \
						.o. @\"morphology/phonology.init.compose.$*\" \
						.o. @\"morphology/phonology.verb.compose.$*\" \
						.o. @\"morphology/phonology.tidy.compose.$*\" \
						;\n\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)

.generated/analyser-nouns.%: morphology/gle.noun-all.% \
				  morphology/phonology.nounadj.compose.% \
				  morphology/phonology.init.compose.% \
				  morphology/phonology.tidy.compose.% $(GENDIR)
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
						@\"morphology/gle.noun-all.$*\"			\
						.o. @\"morphology/phonology.init.compose.$*\"	  \
						.o. @\"morphology/phonology.nounadj.compose.$*\" \
						.o. @\"morphology/phonology.tidy.compose.$*\"	  \
						;\n\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)

.generated/analyser-adj.%: morphology/gle.adj.% \
				morphology/phonology.nounadj.compose.% \
				morphology/phonology.init.compose.% \
				morphology/phonology.tidy.compose.% $(GENDIR)
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
						@\"morphology/gle.adj.$*\"					\
						.o. @\"morphology/phonology.init.compose.$*\"	  \
						.o. @\"morphology/phonology.nounadj.compose.$*\" \
						.o. @\"morphology/phonology.tidy.compose.$*\"	  \
						;\n\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)

.generated/analyser-others.hfst: morphology/gle.others.hfst $(GENDIR)
	$(AM_V_HMINIM)$(HFST_MINIMIZE) $< -o $@

.generated/analyser-others.%: morphology/gle.others.% $(GENDIR)
	$(AM_V_CP)cp $< $@

.generated/analyser-all.%: .generated/analyser-verbs.% \
				.generated/analyser-nouns.% \
				.generated/analyser-adj.% \
				.generated/analyser-others.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
						[ @\".generated/analyser-verbs.$*\"   \
						| @\".generated/analyser-nouns.$*\"   \
						| @\".generated/analyser-adj.$*\"	   \
						| @\".generated/analyser-others.$*\" ]\
						;\n\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)

### Final processing of the raw analyser/generator:
.generated/generator-raw-gt-desc.hfst: .generated/analyser-all.hfst \
								 fixes.hfst \
								 fixes-good.hfst
	$(AM_V_XFST_TOOL)$(PRINTF) "\
				set harmonize-flags ON\n\
				read regex \
				[	@\"fixes.hfst\"			 \
				.o. @\"$<\"					 \
				] | @\"fixes-good.hfst\"	 \
				;\n\
				 save stack $@\n\
				 quit\n" | $(HFST_XFST) -p $(MORE_VERBOSITY) $(HFST_FORMAT)


.generated/analyser-raw-gt-desc.hfst: .generated/generator-raw-gt-desc.hfst
	$(AM_V_CP)cp $< $@

# Wrap processing of Foma and Xfst in a define:
.generated/analyser-raw-gt-desc.%: analyser-all.% \
								 fixes.% \
								 fixes-good.%
		$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
						[	@\"fixes.$*\"		   \
						.o. @\"$<\"					\
						] | @\"fixes-good.$*\"	   \
						;\n\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)

##################################################################
#### END: Add local processing instructions ABOVE this line ######
##################################################################

include $(top_srcdir)/../giella-core/am-shared/src-fst-dir-include.am
include $(top_srcdir)/../giella-core/am-shared/devtest-include.am
