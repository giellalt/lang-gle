
#      I R I S H  G R A M M A R   C H E C K E R

## DELIMITERS

* DELIMITERS = "<.>" "<!>" "<?>" "<...>" "<¶>" sent ; 

## TAGS AND SETS

## Tags

This section lists all the tags inherited from the fst, and used as tags
in the syntactic analysis. The next section, **Sets**, contains sets defined
on the basis of the tags listed here, those set names are not visible in the output.

### Beginning and end of sentence
BOS
EOS

### Parts of speech tags

* Art
* Noun
* Prep

* Subst Check what it is

* N CHECK!!
* A CHECK!!
* Noun
* Adjective
* Adv
* V
* Pron
* CS
* CC
* CC-CS
* Po
* Pr
* Pcle
Num
* Interj
* ABBR
* ACR
* CLB
* LEFT
* RIGHT
* WEB
* PPUNCT
* Det
* PUNCT

* COMMA
* ¶

### Tags for POS sub-categories

* Simp
* Sbj

* Pers
* Dem
* Interr
* Indef
* Recipr
* Refl
* Rel
* Coll
* NomAg
* Prop
* Allegro
* Arab
* Romertall

### Tags for morphosyntactic properties

* DefArt
* Art
* Def
* Fem
* Masc
* Len
* hPref, for h prefixation
* Ecl
* Poss, possessive

* Nom
* Acc
* Gen
* Dat
* Loc
* Com
* Ess
* Par
* Voc
* Sg
* Pl
* Cmp/SplitR
* Cmp/SgNom Cmp/SgGen
* Cmp/SgGen

* Comp
* Superl
* Attr
* Ord
* Qst
* IV
* TV
* VD
* Verbal
* Prt
* Prs
* Ind
* Pot
* Cond
* Imprt
* ImprtII
* Sg1
* Sg2
* Sg3
* Du1
* Du2
* Du3
* Pl1
* Pl2
* Pl3
* Inf
* ConNeg
* Neg
* PrfPrc
* VGen
* PrsPrc
* Ger
* Sup
* Actio
* VAbess
* Abbreviation

* SET NUMBER = Sg OR Pl ;  

* Err/Orth

* ### Semantic tags

* Sem/Act
* Sem/Ani
* Sem/Atr
* Sem/Body
* Sem/Clth
* Sem/Domain
* Sem/Feat-phys
* Sem/Fem
* Sem/Group
* Sem/Lang
* Sem/Mal
* Sem/Measr
* Sem/Money
* Sem/Obj
* Sem/Obj-el
* Sem/Org
* Sem/Perc-emo
* Sem/Plc
* Sem/Sign
* Sem/State-sick
* Sem/Sur
* Sem/Time
* Sem/Txt

* HUMAN

* HAB-ACTOR
* HAB-ACTOR-NOT-HUMAN

* PROP-ATTR
* PROP-SUR

* TIME-N-SET

## Noun errors (Len vs. not Len) after prepositions

The following prepositions cause the following noun to be eclipsed and there are different rules for each preposition.
* LIST ECLIPSE-PREP = "<ar>" ("ar" Prep Simp SUGGEST) "<Ar>" "<i>" "<I>" ("i" Prep Simp SUGGEST) "<chuig>" ("chuig" Prep Simp SUGGEST) "<le>" "<Le>" ("le" Prep Simp SUGGEST); 

These prepositions always cause the nouns after them to be lenited:
* LIST ART-LEN-PREP = "<de>" "<do>" "<faoi>" "<mar>" "<ó>" "<roimh>" "<thar>" "<trí>";					

Noun errors (Ecl vs. not Ecl) after prepositions

* LIST NUM-LEN = "aon" "<chéad>" "<dhá>" "trí" "<ceithre>" "cúig" "sé" "beirt" "uile"; 		
* LIST NUM-ECL = "seacht" "ocht" "naoi" "deich" ; 
* LIST NUM-PL-ADJ = "<dhá>" "trí" "ceithre" "cúig" "sé" "seacht" "ocht" "naoi" "deich" "beirt" ; 	
* LIST ECL-NON-ECL-N = (".*ó"r) (".*án"r) ; 

* LIST COMMONWORD = ("carr" Noun Masc) ("athair" Noun Masc) ; 	
* LIST RAREWORD = ("carr" Noun Fem) ("athair" Noun Fem) ; 	

###  Syntactic tags

* `@+FAUXV     `
* `@+FMAINV    `
* `@-FAUXV     `
* `@-FMAINV    `
* `@-FSUBJ>    `
* `@-F<OBJ     `
* `@-FOBJ>     `
* `@-FSPRED<OBJ`
* `@-F<ADVL    `
* `@-FADVL>    `
* `@-F<SPRED   `
* `@-F<OPRED   `
* `@-FSPRED>   `
* `@-FOPRED>   `
* `@>ADVL`
* `@ADVL<`
* `@<ADVL`
* `@ADVL>`
* `@ADVL`
* `@HAB>`
* `@<HAB`
* `@>N`
* `@Interj  `
* `@N<      `
* `@>A      `
* `@P<      `
* `@>P      `
* `@HNOUN   `
* `@INTERJ  `
* `@>Num    `
* `@Pron<   `
* `@>Pron   `
* `@Num<    `
* `@OBJ     `
* `@<OBJ    `
* `@OBJ>    `
* `@OPRED   `
* `@<OPRED  `
* `@OPRED>  `
* `@PCLE    `
* `@COMP-CS<`
* `@SPRED   `
* `@<SPRED  `
* `@SPRED>  `
* `@SUBJ    `
* `@<SUBJ   `
* `@SUBJ>   `
* SUBJ
* SPRED
* OPRED
* @PPRED
* `@APP      `
* `@APP-N<   `
* `@APP-Pron<`
* `@APP>Pron `
* `@APP-Num< `
* `@APP-ADVL<`
* `@VOC      `
* `@CVP      `
* `@CNP      `
* OBJ
* `<OBJ`
* `OBJ>`
* `<OBJ-OTHERS`
* `OBJ>-OTHERS`

* SYN-V
* @X

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

* ADLVCASE

* CASE-AGREEMENT
* CASE

* NOT-NOM
* NOT-GEN
* NOT-ACC

### Verb sets

#### Verbs and their complements

* NOT-V

### Sets for finiteness and mood

* REAL-NEG
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

#### Genitive rules

1. N N => N N.Gen (When two nouns come together, the second noun has to be in the genitive case.)

2. N DefArt N => N DefArt N.Gen (When two nouns come together and there is the definite article between the nouns.)

3. N DetPoss N => N DetPoss N.Gen (When two nouns come together and there is a possessive adjective between the nouns, the possessive adjective does not cancel the rule of the second noun being in the genitive case.)

4. N A => N A.Gen When adjectives come after nouns in the genitive, the adjective must be rendered into the genitive case as well.)

5. VN N.Gen => VN N.Gen (When a definite noun follows a verbal noun, the definite noun has to be in the genitive case.)

Other gen tags:
* LIST &msyn-gen-case-nouns = &msyn-gen-case-nouns ;    is the old genrule tag we want to get rid of

###  Other tags

* LIST &use-guillemets = &use-guillemets ;     
* LIST &lex-ar-a-haon-a-chlog = &lex-ar-a-haon-a-chlog ;  
* LIST &lex-ar-an-aonach = &lex-ar-an-aonach ;  
* LIST &lex-ar-an-gcaife = &lex-ar-an-gcaife;     
* LIST &lex-ar-an-tae = &lex-ar-an-tae;     
* LIST &lex-tá-is = &lex-tá-is ;       
* LIST &msyn-adj-gender = &msyn-adj-gender ;       
* LIST &msyn-beag-is-fiu-de = &msyn-beag-is-fiu-de ;  
* LIST &msyn-cúpla-plnoun-sgnoun = &msyn-cúpla-plnoun-sgnoun ;      
* LIST &msyn-ecl-after-prep = &msyn-ecl-after-prep ;      
* LIST &msyn-ecl-after-prep2 = &msyn-ecl-after-prep2 ;      
* LIST &msyn-fada-o = &msyn-fada-o ;     
* LIST &msyn-gen-vn-noun-with-article = &msyn-gen-vn-noun-with-article;	 
* LIST &msyn-hPref-after-prep = &msyn-hPref-after-prep ; 
* LIST &msyn-inis-do = &msyn-inis-do ;     
* LIST &msyn-len-after-prep = &msyn-len-after-prep ;     
* LIST &msyn-ecl-after-mura = &msyn-ecl-after-mura ;	  
* LIST &msyn-ecl-after-da = &msyn-ecl-after-da ;	  
* LIST &msyn-ecl-after-go = &msyn-ecl-after-go ;	  
* LIST &msyn-ecl-after-nach = &msyn-ecl-after-nach ;  
* LIST &msyn-lenition-after-possessive-adjective = &msyn-lenition-after-possessive-adjective ;       
* LIST &msyn-noun-defart = &msyn-noun-defart ;     
* LIST &msyn-prepart-prep = &msyn-prepart-prep ;     
* LIST &msyn-prep-detposs = &msyn-prep-detposs ;     
* LIST &msyn-possadj-nom-gen = &msyn-possadj-nom-gen ;     
* LIST &msyn-prep-pron = &msyn-prep-pron ;     
* LIST &msyn-teastaigh-ó = &msyn-teastaigh-ó ;     
* LIST &syn-a-before-verb-relativephrase = &syn-a-before-verb-relativephrase ;     
* LIST ADDED = ADDED ;   tag ensuring ... hmm
* LIST ADDED-BEFORE-BLANK = ADDED-BEFORE-BLANK ;   tag ensuring ... hmm
* LIST SUGGEST = SUGGEST ;   tag ensuring generation of a suggestion for an errouneous word

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

## Prepositions and pronouns fused

**ADD:msyn-prep-pron** RULE TO CHANGE A PREPOSITION AND A PRONOUN INTO A PREPOSITIONAL PRONOUN (e.g., AG MÉ = AGAM, ROIMH SIBH = ROMHAIBH) !!IT WORKS!!

## Prepositions and possessive adjectives fused

**ADD:msyn-h-after-fem-possessive-adjective**: rule to add h to noun following possessor

### RULE TO ADD LENITION TO NOUNS FOLLOWING PREPOSITIONS

### RULE TO LENITE VERBS AFTER THE NEGATIVE PARTICLE NÍ

### RULE TO LENITE VERBS IN THE PAST TENSE AFTER THE NEGATIVE PARTICLE NÍOR

**ADD:msyn-len-after-prep**: rule to add lenition to nouns following prepositions

Template rule to delete A and modify B in A B strings:

### rule to correct lenition (séimhiú) errors for nouns after certain prepositions

### rule to take away lenition for nouns after certain prepositions

### Rules for lenition

**ADD:msyn-teastaigh-ó**: exchange prep "mé" with "ó" when following "teastaigh" IT WORKS

**ADD:msyn-inis-do** ...

**ADD:msyn-fada-o** ...

**ADD:msyn-beag-is-fiu-de** "beag is fiú de" A + "de"

**ADD:msyn-cúpla-plnoun-sgnoun** ..

### RULE TO CORRECT PLURAL NOUNS AFTER THE WORD CÚPLA AS THE NOUN AFTER CÚPLA SHOULD BE IN THE SINGULAR FORM. !!IT WORKS!!

#### Genitive rule 1. Noun + Noun => Noun + Noun.Gen

#### Genitive rule 2. Noun DefArt Noun => Noun DefArt Noun.Gen

#### Genitive rule 3. Noun DetPoss Noun

A RULE TO CHANGE THE NOUN AFTER A NOUN AND A POSSESIVE ADJECTIVE TO THE GENITIVE CASE.
Note: Rule says target is Noun.Com + Det.Poss + Noun.Com, and changes the final noun.

#### Genitive rule 4 N A

#### Genitive rule 5. Verbal noun + noun e.g., ag scríobh an litir > ag scríobh na litreach VN NOUN ART NOUN.Com > VN Noun Art.Gen Noun.Gen

#### Art + Noun.Gen => Art.Gen + Noun.Gen # here we correct 

**ADD:msyn-gen-case-nouns** ...

## Definiteness errors in nouns, e.g., an asal > an t-asal, an bean > an bhean, an sráid > an tsráid.

### A simple grammar checker rule without suggestions: Ensure preceding nominal agrees with the verb

**ADD:use-guillemets**: Simple punctuation rules showing how to change the lemma in the suggestions:

**ADD:use-ellipsis** ...

**ADD:use-ie.i.** ...

###  A RULE TO INSERT THE PARTICLE A BEFORE A VERB RELATIVE PHRASE !!IT WORKS!!

**ADD:lex-ar-an-aonach**: A rule to correct the error "ag an aonach" to the correct form "ar an aonach".	

**ADD:lex-ar-a-haon-a-chlog** ...

**ADD:lex-ar-an-tae**: This rule is for when people put milk in tea. In Irish, the correct way to say it is that milk is put on tea.

This rule is for when people put milk in coffee. In Irish, the correct way to say it is that milk is put on coffee. At is stands, the rule works for Ulaidh Irish. It needs to be changed to work for standard Irish.

**ADD:lex-ar-an-gcaife** ...

**ADD:faoi an - faoin **: A rule to correct the error "faoi an" to the correct form "faoin".

**ADD:msyn-hPref-after-prep**: A rule to insert an h after certain prepositions 

**ADD:msyn-ecl-after-prep**: A rule to correct eclipse errors without an intervening article. !!!IT WORKS!!! THESE RULES NEED TO BE AFTER THE ADDING AN ARTICLE AFTER PREPOSITION RULES

**ADD:msyn-ecl-after-prep-sfem**: Eclipse after preposition ... (sfem?)

* * *

<small>This (part of) documentation was generated from [tools/grammarcheckers/grammarchecker.cg3](https://github.com/giellalt/lang-gle/blob/main/tools/grammarcheckers/grammarchecker.cg3)</small>
