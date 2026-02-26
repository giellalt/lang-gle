
#Irish morphological analyser                      !
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

# Multichar_Symbols definitions

## Analysis symbols
The morphological analyses of wordforms of UNDEFINED language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).

- **+Acc		  ** = Accusative case
- **+Cp		  ** = ?
- **+Wh		  ** = wh word?

Subj is used for subjunctive

- **LEXICON Root           **  Where all adjectives start
- **AdjectiveAndPrefix ;   **  and splits according to affix

- **LEXICON AdjectiveAndPrefix  **
- **an- AllAdjectives ;         ** they may get an an- prefix
- **ró- AllAdjectives ;         ** ... a ró- prefix
- **    AllAdjectives ;         ** ... or no prefix
- This is for testing only. We might want tags
for these prefixes or perhaps a flag that makes
it possible to block an- or ró- forms of certain
adjectives in the lexicon.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root-adj.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root-adj.lexc)</small>
