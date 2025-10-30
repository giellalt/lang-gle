## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

######## Test targets: ###########

if WANT_GRAMCHECK


# List here (space separated) all yaml files to be run as part of make check:
TESTS=from_grammarcheckers_cg3-FAIL.yaml \
    msyn-adj-gender.yaml \
    msyn-ar-a-haon-a-chlog-FAIL.yaml \
    msyn-ar-an-aonach-FAIL.yaml \
    msyn-ar-an-aonach-PASS.yaml \
    msyn-beag-is-fiu-de-FAIL.yaml \
    msyn-cupla-plnoun-sgnoun-PASS.yaml \
    msyn-ecl-after-prep-FAIL.yaml \
    msyn-fada-o-FAIL.yaml \
    msyn-fada-o-PASS.yaml \
    msyn-gen-case-nouns-FAIL.yaml \
    msyn-gen-noun-adj-PASS.yaml \
    msyn-gen-noun-defart-noun-FAIL.yaml \
    msyn-gen-noun-defart-noun-PASS.yaml \
    msyn-gen-noun-detpss-noun-PASS.yaml \
    msyn-gen-noun-detpss-noun-FAIL.yaml \
    msyn-gen-noun-noun-FAIL.yaml \
    msyn-gen-noun-noun-PASS.yaml \
    msyn-gen-vn-noun-PASS.yaml \
    msyn-gen-vn-noun-with-article-FAIL.yaml \
    msyn-inis-do-FAIL.yaml \
    msyn-noun-defart-FAIL.yaml \
    msyn-noun-defart-PASS.yaml \
    msyn-sentences.yaml \
    msyn-teastaigh-o-PASS.yaml


# List tests that are presently (expected) failures here, ie things that should
# be fixed *later*, but is not critical at the moment:
XFAIL_TESTS=from_grammarcheckers_cg3-FAIL.yaml \
    msyn-ar-a-haon-a-chlog-FAIL.yaml \
    msyn-ar-an-aonach-FAIL.yaml \
    msyn-gen-noun-detpss-noun-FAIL.yaml \
    msyn-beag-is-fiu-de-FAIL.yaml \
    msyn-ecl-after-prep-FAIL.yaml \
    msyn-fada-o-FAIL.yaml \
    msyn-gen-case-nouns-FAIL.yaml \
    msyn-gen-noun-adj-PASS.yaml \
    msyn-gen-noun-defart-noun-FAIL.yaml \
    msyn-gen-noun-noun-FAIL.yaml \
    msyn-gen-vn-noun-PASS.yaml \
    msyn-gen-vn-noun-with-article-FAIL.yaml \
    msyn-inis-do-FAIL.yaml \
    msyn-noun-defart-FAIL.yaml \
    msyn-sentences.yaml





endif # WANT_GRAMCHECK

#### Do NOT edit below here: ####
include $(top_srcdir)/../giella-core/am-shared/tools-grammarcheckers-tests-dir-include.am
include $(top_srcdir)/../giella-core/am-shared/devtest-include.am
