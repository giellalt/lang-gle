
IRISH  G R A M M A R   C H E C K E R

# DELIMITERS

* DELIMITERS = "<.>" "<!>" "<?>" "<...>" "<¶>" sent ; 

# TAGS AND SETS

## Tags

This section lists all the tags inherited from the fst, and used as tags
in the syntactic analysis. The next section, **Sets**, contains sets defined
on the basis of the tags listed here, those set names are not visible in the output.

### Beginning and end of sentence
BOS
EOS

### Parts of speech tags

Art
Noun
Prep

Subst Check what it is

N CHECK!!
A CHECK!!
Noun
Adjective
Adv
V
Pron
CS
CC
CC-CS
Po
Pr
Pcle
Num
Interj
ABBR
ACR
CLB
LEFT
RIGHT
WEB
PPUNCT
Det
PUNCT

COMMA
¶

### Tags for POS sub-categories

Simp
Sbj

Pers
Dem
Interr
Indef
Recipr
Refl
Rel
Coll
NomAg
Prop
Allegro
Arab
Romertall

### Tags for morphosyntactic properties

DefArt
Art
Def
Fem
Masc
Len
hPref, for h prefixation
Ecl
Poss, possessive

Nom
Acc
Gen
Dat
Loc
Com
Ess
Par
Voc
Sg
Pl
Cmp/SplitR
Cmp/SgNom Cmp/SgGen
Cmp/SgGen

Comp
Superl
Attr
Ord
Qst
IV
TV
VD
Verbal
Prt
Prs
Ind
Pot
Cond
Imprt
ImprtII
Sg1
Sg2
Sg3
Du1
Du2
Du3
Pl1
Pl2
Pl3
Inf
ConNeg
Neg
PrfPrc
VGen
PrsPrc
Ger
Sup
Actio
VAbess

* SET NUMBER = Sg OR Pl ;  

Err/Orth

### Semantic tags

Sem/Act
Sem/Ani
Sem/Atr
Sem/Body
Sem/Clth
Sem/Domain
Sem/Feat-phys
Sem/Fem
Sem/Group
Sem/Lang
Sem/Mal
Sem/Measr
Sem/Money
Sem/Obj
Sem/Obj-el
Sem/Org
Sem/Perc-emo
Sem/Plc
Sem/Sign
Sem/State-sick
Sem/Sur
Sem/Time
Sem/Txt

HUMAN

HAB-ACTOR
HAB-ACTOR-NOT-HUMAN

PROP-ATTR
PROP-SUR

TIME-N-SET

## Noun errors (Len vs. not Len) after prepositions

The following prepositions cause the following noun to be eclipsed and there are different rules for each preposition.
* LIST ECLIPSE-PREP = "<ar>" "<i>" "<chuig>" "<le>"; 			

These prepositions always cause the nouns after them to be lenited:
* LIST ART-LEN-PREP = "<de>" "<do>" "<faoi>" "<mar>" "<ó>" "<roimh>" "<trí>";					

Noun errors (Ecl vs. not Ecl) after prepositions

* LIST NUM-LEN = "aon" "<chéad>" "<dhá>" "trí" "<ceithre>" "cúig" "sé" "beirt" "uile"; 		
* LIST NUM-ECL = "seacht" "ocht" "naoi" "deich" ; 
* LIST NUM-PL-ADJ = "<dhá>" "trí" "ceithre" "cúig" "sé" "seacht" "ocht" "naoi" "deich" "beirt" ; 	
* LIST ECL-NON-ECL-N = (".*ó"r) (".*án"r) ; 

* LIST COMMONWORD = ("carr" Noun Masc) ("athair" Noun Masc) ; 	
* LIST RAREWORD = ("carr" Noun Fem) ("athair" Noun Fem) ; 	

###  Syntactic tags

`@+FAUXV     `
`@+FMAINV    `
`@-FAUXV     `
`@-FMAINV    `
`@-FSUBJ>    `
`@-F<OBJ     `
`@-FOBJ>     `
`@-FSPRED<OBJ`
`@-F<ADVL    `
`@-FADVL>    `
`@-F<SPRED   `
`@-F<OPRED   `
`@-FSPRED>   `
`@-FOPRED>   `
`@>ADVL`
`@ADVL<`
`@<ADVL`
`@ADVL>`
`@ADVL`
`@HAB>`
`@<HAB`
`@>N`
`@Interj  `
`@N<      `
`@>A      `
`@P<      `
`@>P      `
`@HNOUN   `
`@INTERJ  `
`@>Num    `
`@Pron<   `
`@>Pron   `
`@Num<    `
`@OBJ     `
`@<OBJ    `
`@OBJ>    `
`@OPRED   `
`@<OPRED  `
`@OPRED>  `
`@PCLE    `
`@COMP-CS<`
`@SPRED   `
`@<SPRED  `
`@SPRED>  `
`@SUBJ    `
`@<SUBJ   `
`@SUBJ>   `
SUBJ
SPRED
OPRED
@PPRED
`@APP      `
`@APP-N<   `
`@APP-Pron<`
`@APP>Pron `
`@APP-Num< `
`@APP-ADVL<`
`@VOC      `
`@CVP      `
`@CNP      `
OBJ
`<OBJ`
`OBJ>`
`<OBJ-OTHERS`
`OBJ>-OTHERS`

SYN-V
@X

## Sets containing sets of lists and tags

This part of the file lists a large number of sets based partly upon the tags defined above, and
partly upon lexemes drawn from the lexicon.
See the sourcefile itself to inspect the sets, what follows here is an overview of the set types.

### Sets for Single-word sets

* LIST INITIAL = "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m"  	
*         "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"           	
*         "á" ;  INITIAL

### Sets for word or not

WORD
any word
* SET REAL-WORD-NOT-ABBR = WORD - Num - Ord - (ABBR N) ; # This is former REALWORD-NOTABBR #!! REAL-WORD-NOT-ABBR 
* SET NOT-COMMA = WORD - COMMA ;  #!! NOT-COMMA 
= * SET NOT-COMMA = WORD - COMMA ;  #!! NOT-COMMA 

### Case sets

ADLVCASE

CASE-AGREEMENT
CASE

NOT-NOM
NOT-GEN
NOT-ACC

### Verb sets

#### Verbs and their complements

NOT-V

### Sets for finiteness and mood

REAL-NEG

MOOD-V

NOT-PRFPRC

### Sets for person

SG1-V
SG2-V
SG3-V
PL1-V
PL2-V
PL3-V

Set for your, my and his

* LIST PLPOSS = (Poss Pl)  ;  

Note that imperative verbs are not included in these sets!

Some subsets of the VFIN sets
* SET SG-V = SG1-V OR SG2-V OR SG3-V ;  
* SET PL-V = PL1-V OR PL2-V OR PL3-V ; 

### Pronoun sets

### Adjectival sets and their complements

### Adverbial sets and their complements

### Sets of elements with common syntactic behaviour

### NP sets defined according to their morphosyntactic features

### The PRE-NP-HEAD family of sets

These sets model noun phrases (NPs). The idea is to first define whatever can
occur in front of the head of the NP, and thereafter negate that with the
expression **WORD - premodifiers**.

### Border sets and their complements

### Morphoponological sets

### Grammarchecker sets

* LIST SUGGEST = SUGGEST ;   tag ensuring generation of a suggestion for an errouneous word
* LIST ADDED = ADDED ;   tag ensuring ... hmm
* LIST &lex-tá-is = &lex-tá-is ;       
* LIST &msyn-lenition-after-possessive-adjective = &msyn-lenition-after-possessive-adjective ;       
* LIST &msyn-adj-gender = &msyn-adj-gender ;       
* LIST &msyn-ar-a-haon-a-chlog = &msyn-ar-a-haon-a-chlog ;  
* LIST &msyn-ar-an-aonach = &msyn-ar-an-aonach ;  
* LIST &msyn-beag-is-fiú-de = &msyn-beag-is-fiú-de ;  
* LIST &msyn-cúpla-plnoun-sgnoun = &msyn-cúpla-plnoun-sgnoun ;      
* LIST &msyn-ecl-after-prep = &msyn-ecl-after-prep ;      
* LIST &msyn-fada-ó = &msyn-fada-ó ;     
* LIST &msyn-ie.i. = &msyn-&.i. ;     
* LIST &msyn-inis-de = &msyn-inis-de ;     
* LIST &msyn-inis-do = &msyn-inis-do ;     
* LIST &GEmsyn-len-after-prep = &msyn-len-after-prep ;     
* LIST &msyn-len-after-prep-sfem = &msyn-len-after-prep-sfem ;     
* LIST &msyn-noun-defart = &msyn-noun-defart ;     
* LIST &msyn-possadj-nom-gen = &msyn-possadj-nom-gen ;     
* LIST &msyn-prep-pron = &msyn-prep-pron ;     
* LIST &msyn-gen-case-nouns = &msyn-gen-case-nouns ;     
* LIST &msyn-teastaigh-ó = &msyn-teastaigh-ó ;     
* LIST &msyn-ar-an-tae = &msyn-ar-an-tae;     
* LIST &msyn-ar-an-gcaife = &msyn-ar-an-gcaife;     
* LIST &msyn-tóin-poill = &msyn-tóin-poill ;     
* LIST &msyn-fem-article = &msyn-fem-article ;     
* LIST &spell-conservatively = spell-conservatively ;     
* LIST &spell-it-all = spell-it-all ;     
* LIST &syn-a-before-verb-relativephrase = &syn-a-before-verb-relativephrase ;     
* LIST &use-ellipsis = &use-ellipsis ;     
* LIST &use-guillemets = &use-guillemets ;     
* LIST SUGGEST = SUGGEST ;     

* MAPPING-PREFIX = & ;     

Here ends the list and set section

# BEFORE-SECTIONS       

* LIST <fixedcase> = <fixedcase>;        
* ADD:fixedcase-np <fixedcase> TARGET Prop ;     	 ,  Never change case of proper nouns

# SECTION       

## spellchecking

* ADD:spell-it-all (&typo SUGGESTWF) (<spelled>) ;      		 = add rule marking typos

* LIST HUMAN-N = "dochtúir" "múinteoir" "bean" "fear" ;    	 (to be moved to other tags)

* **RULE: lex-tá-is ** To change *TÁ* to *IS*

## Gender errors in adjectives

**RULE: msyn-adj-gender** to change Masculine adjective to Feminine if it modifies a feminine noun !!IT WORKS!!

## Prepositions

**ADD:msyn-prep-pron** RULE TO CHANGE A PREPOSITION AND A PRONOUN INTO A PREPOSITIONAL PRONOUN (e.g., AG MÉ = AGAM, ROIMH SIBH = ROMHAIBH) !!IT WORKS!!

**ADD:msyn-h-after-fem-possessive-adjective**: rule to add h to noun following possessor

### RULE TO ADD LENITION TO NOUNS FOLLOWING PREPOSITIONS

**ADD:msyn-len-after-prep**: 

### RULE TO LENITE VERBS AFTER THE NEGATIVE PARTICLE NÍ

### RULE TO LENITE VERBS IN THE PAST TENSE AFTER THE NEGATIVE PARTICLE NÍOR

**ADD:msyn-len-after-prep**: rule to add lenition to nouns following prepositions

### rule to correct lenition (séimhiú) errors for nouns after certain prepositions

**ADD:msyn-ecl-after-prep**: A rule to correct eclipse errors without an intervening article. !!!IT WORKS!!!

**ADD:msyn-ecl-after-prep-sfem**: Eclipse after preposition ... (sfem?)

### Rules for lenition

**ADD:msyn-teastaigh-ó**: exchange prep "mé" with "ó" when following "teastaigh"

**ADD:msyn-inis-do** ...

**ADD:msyn-ar-an-aonach**: A rule to correct the error "ag an aonach" to the correct form "ar an aonach".	

**ADD:msyn-ar-a-haon-a-chlog** ...

**ADD:msyn-fada-ó** ...

**ADD:msyn-beag-is-fiú-de** "beag is fiú de" A + "de"	

**ADD:msyn-cúpla-plnoun-sgnoun** ..

### RULE TO CORRECT PLURAL NOUNS AFTER THE WORD CÚPLA AS THE NOUN AFTER CÚPLA SHOULD BE IN THE SINGULAR FORM. !!IT WORKS!!

### RULE TO ENSURE THAT NOUNS APPEAR IN THE GENITIVE CASE. !!IT WORKS!! 

**ADD:msyn-gen-case-nouns** ...

## Definiteness errors in nouns

### RULE TO CORRECT THE GENDER OF NOUNS IF THEY ARE DEFINITE FEMININE NOUNS. !!IT WORKS!!

### A RULE TO CHANGE THE NOUN AFTER A NOUN AND A POSSESIVE ADJECTIVE TO THE GENITIVE CASE. !!IT WORKS!!

### A simple grammar checker rule without suggestions: Ensure preceding nominal agrees with the verb

**ADD:use-guillemets**: Simple punctuation rules showing how to change the lemma in the suggestions:

**ADD:use-ellipsis** ...

**ADD:msyn-ar-an-tae**: This rule is for when people put milk in tea. In Irish, the correct way to say it is that milk is put on tea.

This rule is for when people put milk in coffee. In Irish, the correct way to say it is that milk is put on coffee. At is stands, the rule works for Ulaidh Irish. It needs to be changed to work for standard Irish.

**ADD:msyn-ar-an-gcaife** ...

**ADD:msyn-ie.i.** ...

###  A RULE TO INSERT THE PARTICLE A BEFORE A VERB RELATIVE PHRASE !!IT WORKS!!

* * *

<small>This (part of) documentation was generated from [tools/grammarcheckers/grammarchecker.cg3](https://github.com/giellalt/lang-gle/blob/main/tools/grammarcheckers/grammarchecker.cg3)</small>
