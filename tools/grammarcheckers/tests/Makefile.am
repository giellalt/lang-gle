## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

######## Test targets: ###########

if WANT_GRAMCHECK

# List here (space separated) all yaml files to be run as part of make check:
TESTS=from_grammarcheckers_cg3-FAIL.yaml \
    from_grammarcheckers_cg3-PASS.yaml \
    msyn-ar-a-haon-a-chlog-FAIL.yaml \
    msyn-ar-an-aonach-FAIL.yaml \
    msyn-beag-is-fiu-de-FAIL.yaml \
    msyn-cupla-plnoun-sgnoun-PASS.yaml \
    msyn-ecl-after-prep-FAIL.yaml \
    msyn-fada-o-FAIL.yaml \
    msyn-fada-o-PASS.yaml \
    msyn-inis-do-FAIL.yaml \
    msyn-noun-defart-FAIL.yaml \
    msyn-noun-defart-PASS.yaml \
    msyn-possadj-nom-gen-PASS.yaml \
    msyn-teastaigh-o-PASS.yaml


# List tests that are presently (expected) failures here, ie things that should
# be fixed *later*, but is not critical at the moment:
XFAIL_TESTS=from_grammarcheckers_cg3-FAIL.yaml \
    msyn-ar-a-haon-a-chlog-FAIL.yaml \
    msyn-ar-an-aonach-FAIL.yaml \
    msyn-beag-is-fiu-de-FAIL.yaml \
    msyn-ecl-after-prep-FAIL.yaml \
    msyn-fada-o-FAIL.yaml \
    msyn-inis-do-FAIL.yaml \
    msyn-noun-defart-FAIL.yaml


endif # WANT_GRAMCHECK

#### Do NOT edit below here: ####
include $(top_srcdir)/../giella-core/am-shared/tools-grammarcheckers-tests-dir-include.am
include $(top_srcdir)/../giella-core/am-shared/devtest-include.am
