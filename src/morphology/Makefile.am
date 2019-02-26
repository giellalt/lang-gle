## Process this file with automake to produce Makefile.in

## Copyright (C) 2011 Samediggi

## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Add language-specific flags for hfst-lexc compilation here:
HFST_LEXC_LOCAL_FLAGS=

# Set this to name of lexc file containing Multichar_Symbols and LEXICON Root
GT_LEXC_ROOT=$(srcdir)/root.lexc

# Set this to the names of all regular lexc source files:
GT_LEXC_SRCS_L1_L2=\
			 affixes/adjectives.lexc \
			 affixes/nouns.lexc \
			 affixes/symbols.lexc     \
			 affixes/verbs.lexc \
			 stems/abbreviations.lexc \
			 stems/tags.lexc \
			 stems/adjectives.lexc \
			 stems/adpositions.lexc \
			 stems/adverbs.lexc \
			 stems/articles.lexc \
			 stems/conjunctions.lexc \
			 stems/determiners.lexc \
			 stems/interjections.lexc \
			 stems/nouns.lexc \
			 stems/verbs.lexc \
			 stems/numerals.lexc \
			 stems/particles.lexc \
			 stems/pronouns.lexc \
			 stems/propernouns.lexc \
			 stems/tobar.lexc \
			 stems/verbalnouns.lexc \
			 stems/verbs.lexc
# If you are building an error-detecting L2 analyser, specify the lexc files
# that differ between the regular L1 and the L2 analysers below, in L1 and
# L2 respectively. L2 files must end in "*-L2.lexc". See SME for an example.
L1=

L2=

GT_LEXC_SRCS=\
			$(GT_LEXC_SRCS_L1_L2) \
			$(L1)

GT_LEXC_L2_SRCS=\
			$(GT_LEXC_SRCS_L1_L2) \
			$(L2)

# Set this to the names of all generated lexc files, if any
GENERATED_LEXC_SRCS=generated_files/punctuation.lexc \
                    generated_files/symbols.lexc

# Set this to the names of all source xml files, if any
GT_XML_SRCS=

# Define any additional lexc sources here (compiled on their own):
GT_LOCAL_SRCS=

# Define local xfscripts here:
GT_LOCAL_XFSCRIPT_SRCS=

# Define here any additional sources just included in the distro:
GT_DISTRO_SRCS=

### BEGIN: Local processing: ###

### List additional targets in the following variable, for build targets not
### covered by other means. This comes ***in addition to*** what you can do by
### just targeting lexicon.*: lexicon.tmp.*, and is useful if you want to build
### separate fst's that need further treatment in the src/ dir. See the language
### gle/ for an example of how this is used.

GIELLA_LOCAL_TARGETS=

### This target overrides some defaults to handle lexicons of parts-of-speech 
### separately

GLE_TARGETS=\
			gle.noun-all \
			gle.adj      \
			gle.verb-all \
			gle.others

if CAN_HFST
GIELLA_LOCAL_TARGETS+=$(addsuffix .hfst,$(GLE_TARGETS))
endif # CAN_HFST

if CAN_FOMA
GIELLA_LOCAL_TARGETS+=$(addsuffix .foma,$(GLE_TARGETS))
endif # CAN_HFST

if CAN_XFST
GIELLA_LOCAL_TARGETS+=$(addsuffix .xfst,$(GLE_TARGETS))
endif # CAN_HFST

generated_files/gle.noun-all.lexc: root-noun-all.lexc $(GT_LEXC_SRCS)
	$(AM_V_at)$(MKDIR_P) generated_files
	$(AM_V_GEN)cat $^ > $@

generated_files/gle.adj.lexc: root-adj.lexc $(GT_LEXC_SRCS)
	$(AM_V_at)$(MKDIR_P) generated_files
	$(AM_V_GEN)cat $^ > $@

generated_files/gle.verb-all.lexc: root-verb-all.lexc $(GT_LEXC_SRCS)
	$(AM_V_at)$(MKDIR_P) generated_files
	$(AM_V_GEN)cat $^ > $@

generated_files/gle.others.lexc: root-others.lexc $(GT_LEXC_SRCS)
	$(AM_V_at)$(MKDIR_P) generated_files
	$(AM_V_GEN)cat $^ > $@

####### HFST build rules: ########
%.hfst: generated_files/%.lexc
	$(AM_V_HLEXC)$(HFST_LEXC) \
		$(MORE_VERBOSITY) $(HFST_FORMAT) $(HFST_LEXC_FLAGS) \
		$(HFST_LEXC_LOCAL_FLAGS) -o $@ $^

####### Xerox build rules: #######
%.xfst: generated_files/%.lexc
	$(AM_V_XFST)$(XFST) $(VERBOSITY) \
			-e "read lexc $^" \
			-e "save stack $@ " \
			-stop

####### Foma build rules: #######
%.foma: generated_files/%.lexc
	$(AM_V_FOMA)$(FOMA) $(VERBOSITY) \
			-e "set lexc-align ON" \
			-e "read lexc $^" \
			-e "save stack $@ " \
			-s

### END: Local processing: ###

####### Other targets: ###########
# Clean: add local clean targets on separate lines, so that the first line can
# easily get updates from the template dir through svn merge.
clean-local:
	-rm -f *.all.* *fst *.foma *.script generated_files/*.lexc lexicon.*
	-rm -f url.lexc *.tmp.*

include $(top_srcdir)/am-shared/src-morphology-dir-include.am

# vim: set ft=automake:
