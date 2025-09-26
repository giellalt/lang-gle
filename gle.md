# Irish language model documentation

All doc-comment documentation in one large file.

---

## src-cg3-functions.cg3.md 



* Sets for POS sub-categories

* Sets for Semantic tags

* Sets for Morphosyntactic properties

* Sets for verbs

- V is all readings with a V tag in them, REAL-V should
be the ones without an N tag following the V.  
The REAL-V set thus awaits a fix to the preprocess V ... N bug.

* The set COPULAS is for predicative constructions

* NP sets defined according to their morphosyntactic features

* The PRE-NP-HEAD family of sets

These sets model noun phrases (NPs). The idea is to first define whatever can
occur in front of the head of the NP, and thereafter negate that with the
expression **WORD - premodifiers**.

The set **NOT-NPMOD** is used to find barriers between NPs.
Typical usage: ... (*1 N BARRIER NPT-NPMOD) ...
meaning: Scan to the first noun, ignoring anything that can be
part of the noun phrase of that noun (i.e., "scan to the next NP head")

* Miscellaneous sets

* Border sets and their complements

* Syntactic sets

These were the set types.

### HABITIVE MAPPING

* **hab1** 

* **hab2** 

* **hab3** (<hab> @ADVL>) for hab-actor and hab-case; if leat to the right, and Nom to the right of leat. Lots of restrictions.

* **habNomLeft** 

* **hab4** 	

* **hab6** 

* **hab7** 

* **hab8** This is not HAB
* **hab5**  This is not HAB

* **habDain** (<hab> @ADVL>) for (Pron Dem Pl Loc) if leat followed by Nom to the right

* **habGen** (<hab> @<ADVL) hab for Gen; if Gen is located in the end of the sentence and Nom is sentence initial

* **spred<obj** (@SPRED<OBJ) for Acc; the object of an SPRPED. Not to be mistaken with OPRED. If SPRED is to the left, and copulas is to the left of it. Nom or Hab are found sentence initially.

* **Hab<spred** (@<SPRED) for Nom; if copulas, goallut or jápmit is FMAINV and habitive or human Loc is found to the left. OR: if Ill or @Pron< followed by HAB are found to the left.

* **Hab>Advlcase<spred** (<ext> @<SUBJ) for Nom; it allows adverbials with Ill/Loc/Com/Ess to be found inbetween HAB and <ext>.

* **Nom>Advlcase<spred** (<ext> @<SUBJ) for Nom; it allows adverbials with Ill/Loc/Com/Ess to be found inbetween Nom and <ext> @<SUBJ.

* **<spred** (<ext> @<SUBJ) for Nom; if copulas to the left, and some kind of adverb, N Loc, time related word or Po to the left of it. OR: if Ill or @Pron< to the left, followed by copulas and the before mentioned to the left of copulas. 

* **<spred** (<ext> @<SUBJ) for Nom, but not for Pers. To the left boahtit or heaŋgát as MAINV, and futher to the left is some kind of place related word, or time related word

* **<spredQst1** (<ext> @<SUBJ) for Nom in a typically question sentence; if A) Hab, some kind of place word, Po or Nom to the left, and Qst followed by copulas to the left. B) same as a, only the Qst-pcle is attached to copulas. C) Qst to the left, with copulas to its left, but not if two Nom:s are found somewhere to the right. D) copulas to the left, and BOS to the left. E) Loc or Ill to the left, and Loc or Hab to the left of this, Qst and copulas to the left. F) Num @>N to the left, Hab, some kind of place word, Po or Nom to the left, and Qst followed by copulas to the left. NOTE) for all these rules; human, Loc or Sem/Plc not allowed to the right.

* **<spredQst2** (@<SPRED) for Nom; in a typically question sentence; differs from <spredQst1 by not beeing as restricted to the right. Though you are not allowed to be Pers or human.

* **Nom<spredQst** (@<SPRED) for Nom; in a typically question sentence. Differs from <spredQst2 by letting Nom be found between SPRED and copulas

* **<spred** (@<SPRED) for A Nom or N Nom if; the subject Nom is on the same side of copulas as you: on the right side of copulas

* **<spredVeara** (@<SPRED) for veara + Nom; if genitive immediately to the right, and intransitive mainverb to the right of genitive

* **leftCop<spred** (@<SPRED) for Nom; if copulas is the main verb to the left, and there is no Ess found to the left of cop (note that Loc is allowed between target and cop). OR: if you are Coll or Sem/Group with copulas to your left. 

* **<spredLocEXPERIMENT** (@<SPRED) for material Loc; if you are to the right of copulas, and the Nom to the left of copulas is not a hab-actor

* **NumTime** (@<SPRED) for A Nom

* **<spredSg** (@<SPRED) for Sg Nom	

* **<spredPg** (@<SPRED) for Pl Nom	

* **<spred** (@<SPRED) for Nom; if copulas to the left, and Nom or sentence boundary to the left of copulas. First one to the right is EOS.

* **<spred** (@<SPRED) for N Ess

* **spredEss>** (@SPRED>) for N Ess; if copulas to the right of you, and if an NP with nom-case first one to your left.

* **HABSpredSg>** (@SPRED>) for Nom; if habitive first one to the left, followed by copulas.

* **GalleSpred>** (@SPRED>) for Num Nom; if sentence initial

* **spredSgMII>** (@SPRED>)

* **r492>** (@SPRED>) for Interr Gen; consisting only of negations. You are not allowed to be MII. You are not allowed to have an adjective or noun to yor right. You are not allowed to have a verb to your right; the exception beeing an aux.

* **AdjSpredSg>** (@SPRED>) for A Sg Nom; if copulas to the right, but not if A or @<SPRED are found to the right of copulas

* **SpredSg>Hab** (@SPRED>) for Nom; if you are sentence initial, copulas is located to the right, and there is a habitive to the right of copulas

* **Spred>SubjInf** (@SPRED>) for Nom; if copulas to the right, and the subject of copulas is an Inf to the right

* **spredCoord** (@<SPRED) coordination for Nom; only if there already is a SPRED to the left of CNP. Not if there is some kind of comparison involved.

* **subj>Sgnr1** (@SUBJ>) for Nom Sg, including Indef Nom if; VFIN + Sg3 or Pl3 to the right (VFIN not allowed to the left) 

* **subj>Du** (@SUBJ>) for dual nominatives, including Coll Nom. VFIN + Du3 to the right. 
* **subj>Pl** (@SUBJ>) for plural nominatives, including Coll and Sem/Group. VFIN + Pl3 to the right.

* **subj>Pl** (@SUBJ>) for plural nominatives

* **subj>Sgnr2** (@SUBJ>) for Nom Sg; if VFIN + Sg3 to the right.

* **<subjSg** (@<SUBJ) for Nom Sg; if VFIN Sg3 or Du2 to the left (no HAB allowed to the left).

* **f<advl** (@-F<ADVL) for infinite adverbials

* **f<advl** (@-F<ADVL) for infinite adverbials

* **s-boundary=advl>** (@ADVL>) for ADVL that resemble s-booundaries. Mainverb to the right.

* **-fobj>** (@-FOBJ>) for Acc 

* **-fobj>** (@-FOBJ>) for Acc

* **advl>mainV** (@ADVL>) if; finite mainverb not found to the left, but the finite mainverb is found to the right.

* **<advl** (@<ADVL) if; finite mainverb found to the left. Not if a comma is found immediately to the left and a finite mainverb is located somewhere to the right of this comma.

* **<advlPoPr** (@<ADVL) if mainverb to the left.
* **advlPoPr>** (@<ADVL) if mainverb to the right.

* **advlEss>** (@<ADVL) for weather and time Ess, if FMAINV to the left.

* **advl>inbetween** (@ADVL>) for Adv; if inbetween two sentenceboundaries where no mainverb is present.

* **comma<advlEOS** (@<ADVL) if; comma found to the left and the finite mainverb to the left of comma. To the right is the end of the sentence.

* **advlBOS>** (@ADVL>) if; you are N Ill and found sentnece initially. First one to your right is a clause.

* **<advlPoEOS** (@<ADVL) for Po; if you are found at the very end of a sentence. A mainverb is needed to the right though.

* **cleanupILL<advl** (@<ADVL) for N Ill if; there are no boundarysymbols to your left, if you arent already @N< OR @APP-N<, and no mainverb is to yor left.

* **<opredAAcc** (@<OPRED) for A Acc; if an other accusative to the left, and a transtive verb to the left of it. OR: if a transitive verb to the left, and an accusative to the left of it.

#### sma object

* **<advlEss** (@<ADVL) for ESS-ADVL if; FMAINV to the left
* **<spredEss** (@<SPRED) for N Ess if; FMAINV to the left is intransitive or bargat

### SUBJ MAPPING - leftovers

### OBJ MAPPING - leftovers

### HNOUN MAPPING

* * *

<small>This (part of) documentation was generated from [src/cg3/functions.cg3](https://github.com/giellalt/lang-gle/blob/main/src/cg3/functions.cg3)</small>

---

## src-fst-morphology-affixes-nouns.lexc.md 

Moirfeolaíocht na nAinmfhocail Gaeilge (Morphology of Irish Nouns)

FEMININE NOUN continuation classes
Weak Plurals : 
Broad singular is made slender; plural already broad

Weak Plurals : Broaden 

Singular already slender; plural is made broad

Weak Plurals : 

Weak Plurals : 

STRONG PLURALS

STRONG PLURALS

STRONG PLURALS

STRONG PLURALS

STRONG PLURALS

STRONG PLURALS

3rd Declension
Strong Plurals : +aí

an bheannacht -> na beannachtaí

gamhain - gamhna (gs), midheamhain - midheamhna (gs)

Strong Plurals :  +(e)anna

tóin -> tóineanna
scoth -> scothanna
EXCEPTION: an chuid -> na codanna see FIX file
EXCEPTION: an raith -> na rathanna see FIX file

Strong Plurals :  Broaden +anna

an chuid -> na codanna see FIX file
an raith -> na rathanna
an laith -> na lathanna
an luaith -> na luathanna

Strong Plurals : +í

an bhearna -> na bearnaí
an eala -> na healaí

Strong Plurals : Athrú e -> í

an aicme -> na haicmí (classes)
an táille -> na táillí (fees)

Strong Plurals : 

various ending in vowel	! plurals +nna

Strong Plurals : Leathnú  +acha

an bheoir -> na beoracha (beers)

Gen Sg : Coim + ach
Strong Plurals : Coimriú +eacha

an chathaoir -> na cathaoireacha (chairs) (Note long vowel aoi is not sync.
an cathair -> na cathracha

Gen Sg : Coim + a
Strong Plurals : Coimriú +(e)acha
samhail -> samhla
anacair -> anacra

Gen Sg : Coim + Slen + e
Strong Plurals : Coimriú +(e)acha
crithir - critre
fothair - foithre

tarraingt - tarraingthe - tarraingtí

MASCULINE NOUN continuation classes

WEAK PLURALS (i.e. where the nominative and genitive plurals are different) 
TYPE 1 Nom pl. ends in conson. eg cat : cait, fear : fir, marcach: marcaigh 

TYPE 2 Nom pl. formed by adding -a eg cos : cosa, úll : úlla 

(TYPE 3) Nom pl. formed by adding -ta eg 

2nd Declension
sliabh -> na sléibhte 

3rd Declension
Strong Plurals : +í 
as in Nm7 but singular are different

eg. bádóir -> na bádóirí

Strong Plurals : +anna

eg. an bláth -> na bláthanna

Strong Plurals : +aí

gen briocht -> breachta
Strong Plurals : +aí
briocht -> briochtaí

Strong Plurals : +anna
eg. an bláth -> na bláthanna

^Lea,broadening, is required, in gen sg: io -> ea (bior, crios) 
and this is done using ^Ath (change)
pl bior -> bioranna

Strong Plurals : Athrú +anna (io->ea)
eg. an cith -> na ceathanna

^Lea,broadening, is required, in gen sg: cith -> ceatha, greim -> greama
and this is done using ^Ath (change)
pl also broadened cith -> ceathanna

sliocht - sleachta gs & pl

Strong Plurals : +í

(A) nouns ending in -ín (a diminutive)
smidiríní (smithereens) no singular
eg. an cailín -> na cailíní (girls)
eg. an báidín -> na báidíní (small boats)

(B) nouns ending in -a
eg. an balla -> na ballaí (walls)

01/04/08

Strong Plurals : +idí
an fiche -> na fichidí (the twenties) eidí needs correcting
an caoga -> na caogaidí (the fifties)

GS +the

GS +te

GS +tha
PL +thaí
bascadh - basctha - bascthaí

GS +ta

moladh / gs = molta / pl = moltaí

INITIAL MUTATIONS
NOMINATIVE SINGULAR 

^IM = initial mutation e.g. with prepositions, and possession
Singular:
e.g. ar an bhosca, ar an mbosca
possessive markers on vowels: ár n-athair, a (f) hathair, 
Plural:
e.g. ar bhoscaí, i mboscaí
possessive e.g. ár n-aithreacha - our fathers (^C)

adds ^h to vowel-initial words ...  but adds the +hPref to all words ... see fix file

GENITIVE SINGULAR 

VOCATIVE SINGULAR 
Since this is trivial (always ^Sé) it is included with Final Mutations
in Voc-sg-0 and Voc-sg-1.

ALL PLURALS
Note: Vocative Plural does not require Def & Idf but it is easier to generate 
them and remove all Voc Pl Idfs at the end (the Def form is correct 
although the Def marker is unnecessary)

FINAL MUTATIONS
NOMINATIVE SINGULAR

GENITIVE SINGULAR 

VOCATIVE SINGULAR 

ALL PLURALS

when it is a place name
as well as the usual inflections for propernouns  (4 classes)
we want to generate an adjectival form e.g. Beilg - Beilgeach

new 5-6-2024
Place and Personal name files both use Nf1-Prop and Nm1-Prop etc.

masc nouns - slenderise

fem nouns - slenderise and add e

fem nouns - broaden and add a

fem nouns - no change

masc nouns - no change

fem nouns - Albain/na hAlban

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/nouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/nouns.lexc)</small>

---

## src-fst-morphology-affixes-prefixes.lexc.md 

Prefixes
Prefixes in the Irish language are bound to beginning of other words.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/prefixes.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/prefixes.lexc)</small>

---

## src-fst-morphology-affixes-propernouns.lexc.md 

Proper noun inflection
The Irish language proper nouns inflect in the same cases as regular
nouns, but with a colon (':') as separator.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/propernouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/propernouns.lexc)</small>

---

## src-fst-morphology-affixes-symbols.lexc.md 


## Symbol affixes

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/symbols.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/symbols.lexc)</small>

---

## src-fst-morphology-affixes-verbs.lexc.md 



inserted +Len +Uru to distinguish between a bhíonn & a mbíonn Dir/Indir
Rel clauses Dec 2004

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/verbs.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/verbs.lexc)</small>

---

## src-fst-morphology-phonology.nounadj.xfscript.md 



a d h      -> [%^FC ]   ||  [d|n|t|l|s] %^X _ %^Ath (%^Caol) t

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.nounadj.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.nounadj.xfscript)</small>

---

## src-fst-morphology-phonology.twolc.md 

=================================== !
The Irish morphophonological/twolc rules file !
=================================== !

* *primus%>s*
* *primus%>0*

*  examples:*

*  examples:*

*  examples:*

*  examples:*

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.twolc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.twolc)</small>

---

## src-fst-morphology-phonology.verb.xfscript.md 

Verbal Noun Gen

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.verb.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.verb.xfscript)</small>

---

## src-fst-morphology-root-adj.lexc.md 


INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

## Multichar_Symbols definitions

### Analysis symbols
The morphological analyses of wordforms of UNDEFINED language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).

- **+Acc		  ** = Accusative case
- **+Cp		  ** = ?
- **+Wh		  ** = wh word?

Subj is used for subjunctive

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root-adj.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root-adj.lexc)</small>

---

## src-fst-morphology-root-noun-all.lexc.md 


INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

## Multichar_Symbols definitions

### Analysis symbols
The morphological analyses of wordforms of UNDEFINED language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).

Subj is used for subjunctive

- **+Acc		  ** = Accusative case
- **+Cp		  ** = ?
- **+Wh		  ** = wh word?

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root-noun-all.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root-noun-all.lexc)</small>

---

## src-fst-morphology-root-others.lexc.md 


INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

## Multichar_Symbols definitions

### Analysis symbols
The morphological analyses of wordforms of UNDEFINED language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).

Subj is used for subjunctive

- **+Acc		  ** = Accusative case
- **+Cp		  ** = ?
- **+Wh		  ** = wh word?

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root-others.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root-others.lexc)</small>

---

## src-fst-morphology-root-verb-all.lexc.md 


INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

## Multichar_Symbols definitions

### Analysis symbols
The morphological analyses of wordforms of UNDEFINED language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).

- **+Acc		  ** = Accusative case
- **+Cp		  ** = ?
- **+Wh		  ** = wh word?

Subj is used for subjunctive

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root-verb-all.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root-verb-all.lexc)</small>

---

## src-fst-morphology-root.lexc.md 


## Irish morphological analyser                      !
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

## Definitions for Multichar_Symbols

### Tag symbols for analysis
The morphological analyses of wordforms for the Irish
language are presented in this system in terms of the following symbols.

- **+Corr  ** = correction in Learner corpus
- **+Error ** = error in Learner corpus
- **+Start ** = start of error/correction

Tag list:

- **+1P		** = first person inflection
- **+2P		** = second person inflection
- **+3P		** = third person inflection
- **+A		** = XXX check
- **+ABBR		** = Abbreviation
- **+ACR	      	** = Acronym
- **+Abr		** = "Abbreviation"
- **+Ad		** = Adverbial particle: go
- **+Adj		** = Adjective
- **+Adv		** = Adverb
- **+Anon		** = Anonymisation in transcribed speech
- **+Arab		** = Arabic numerals (1, 2, ...) 
- **+Art		** = Article determiner (an/na)
- **+Attr		** = Attribute, element preceeding head
- **+Auto		** = Autonomous verb form
- **+Bar		** = hyphen, underscore, dash etc.
- **+Bare		** = bare number form used after number particle "a"
- **+Base		** = Base form of adjective (changed from +Pos to +Base 10/09/03)
- **+Brack		** = round, square and curly brackets
- **+CC		** = Canúint Chonnachta, Connaught dialect
- **+CLB            ** = Clause boundary
- **+CLBfinal	** = Final clause boundary
- **+CM		** = Canúint na Mumhan, Munster dialect
- **+CU		** = Canúint Uladh, Ulster dialect 
- **+Card		** = Cardinal number(one two three ...)
- **+Cmc		** =  Communicator (yeah, y'know) in transcribed speech
- **+CmpNP/First	** = 
- **+CmpNP/None	** = 
- **+Cmpd		** = Compound prepostion
- **+CmpdNoGen	** = Compound prepostion which does not require genitive case on object NP
- **+Cmpl		** = Complementizer: go, gur, nach, nár
- **+Com		** = Common case (nominative/accusative/dative case)
- **+Comp		** = Comparative adjective (c)
- **+Conj		** = Conjunction
- **+Cond		** = Conditional mood
- **+Coord		** = Coordinating conjunction
- **+Cop		** = Copula
- **+Curr		** = Currency symbols
- **+Dat		** = Dative case (e.g. chois) fossilised forms
- **+DeNom		** = Adjectives drived from proper nouns, e.g. Albanach (Scottish adjective), not the same as Albanais (Scottish language noun)
- **+Def		** = Definite article
- **+DefArt		** = noun/number form that follows a definite article (an)
- **+Deg		** = degree particle with Adj/Abstract Noun (so loud, so sharp etc..
- **+Dem		** = Demonstrative determiner (also combined with copula, e.g. Seo
- **+Dep		** = Dependant forms of verbs
- **+Det		** = Determiner, e.g. possessive determiner: mo, do
- **+Dir		** = Directional adverb
- **+Direct 	** = Direct relative particle
- **+Ecl		** = Eclipsis (+Urú) initial mutation, e.g. ar an gcat
- **+Emph		** = Emphatic (Contrastive) form of personal pronoun e.g. ár dteachsa, do theachsa, a teachsa
- **+End		** = end bracket, quote etc
- **+English	** = English language words
- **+Err/Hyph	** = 
- **+Err/Lex	** = 
- **+Err/MissingSpace ** = 
- **+Err/Orth 	  ** = Orthografical error
- **+Err/SpaceCmp 	  ** = Compound space error
- **+Event		  ** = Simple Event (laugh, sneeze etc.) in transcribed speech
- **+Fam		  ** = Family Name - proper noun
- **+Fem		  ** = Feminine gender
- **+Filler		  ** = Filled Pause (eh, em, etc.) in transcribed speech 
- **+Fin		  ** = sentence final punctuation
- **+Foreign	  ** = words from other languages, mainly English, some Latin
- **+Fut		  ** = Future tense verbal particle
- **+FutInd		  ** = Future Indicative verb
- **+Gen		  ** = Genitive case
- **+Acc		  ** = Accusative case
- **+Cp		  ** = ?
- **+Wh		  ** = wh word?
- **+Gn		  ** = General adverb
- **+Guess		  ** = Morphological guesser
- **+hPref 		  ** = h prefixed to a vowel-initial word 
- **+Idf		** = Indefinite quantifier/pronoun e.g. aon (any), cibé (whoever), ceachtar/neachtar (either/neither) etc.
- **+Ill		** = n/a
- **+Imp		** = Imperative particle (negative)
- **+Imper		** = Imperative mood
- **+Indirect	** = Indirect relative particle
- **+Inf		** = Infinitival particle
- **+Int		** = Sentence internal punctuation
- **+Itj		** = Interjection
- **+Its		** = Intensifier of adjective e.g. sách, ró- etc.
- **+End		** = end bracket, quote etc
- **+Latin		** = Latin language words
- **+LEFT		** = Left side of parwise symbol (parenthesis or quotation mark)
- **+Len		** = Lenited forms
- **+Loc		** = Locative adverb
- **+MIDDLE		** = Middle punctuation
- **+MWE		** = Multi word expression
- **+Masc		** = Masculine gender
- **+N 		** = n/a (Noun is used) -- The +N tag is in use, TODO: change it
- **+NER		** = Named Entity Recognition
- **+NG			** = Don't generate non-standard form
- **+NStem		** = De-nominal verbal noun
- **+Neg		** = Negative particle (n)
- **+NegQ		** = Negative interrogative verbal particle(q)
- **+Nm			** = Number particle (m)
- **+Nom 		** =
- **+NotSlen	** = Adj qualifies pl noun with non-slender ending
- **+Noun		** = Noun (common, proper, verbal, substantive)
- **+Num		** = Numeral
- **+OLang/ENG	** = - English language words
- **+OLang/FIN	** = - 
- **+OLang/HUN	** = - 
- **+OLang/LAT	** = - Latin language words
- **+OLang/NNO	** = - 
- **+OLang/NOB	** = - 
- **+OLang/RUS	** = - 
- **+OLang/SMA	** = - 
- **+OLang/SME	** = - 
- **+OLang/SMJ	** = - 
- **+OLang/SWE	** = - 
- **+OLang/UND	** = - 
- **+Obj		** = Object e.g. á = "do a" when obj of VN
- **+Op			** = Number Operators, e.g. +,-,*,/ etc.
- **+Ord		** = Ordinal (first, second, third..) i.e.  mo dhá lámh, an chéad dhá theach 
- **+Part		** = Particle (not +Vb) (U)
- **+Past		** = Past tense verbal particle
- **+PastImp	** = Past Habitual - Gháthchaite (Imperfect Indicative)
- **+PastInd	** = Past Indicative tense
- **+PastSubj	** = Past Subjunctive tense
- **+Pat		** = Patronymic particle (p) (e.g. Ó, Ní, Uí, le, de ..)
- **+Pers		** = Personal pronoun
- **+PersName	** = Personal name - proper noun
- **+Pl			** = Plural number
- **+Place		** = Place name - proper noun
- **+Poss		** = Possessive pronoun (can be attached to a prep, e.g. im', dá, faoina)
- **+Pref		** = Prefix; seperated prefixes in historical texts
- **+Prep		** = Preposition
- **+Pres		** = Copula present & future tense
- **+PresImp	** =  Pres Habitual - Gháthláithreach(Verb bí only - and deireann (abair)
- **+PresInd	** = Present Indicative
- **+PresSubj	** = Present Subjunctive
- **+Pro		** = Pronoun with copula or relative particle
- **+Pron		** = Pronoun
- **+Prop		** = Proper noun
- **+Punct		** = Abbreviation
- **+PUNCT		** = Abbreviation (it seems several languages have two tags :-/
- **+Q			** = Interrogative particle(q)
- **+Qty		** = Quantifier
- **+Quo		** = all quotation marks double, single etc.
- **+Ref		** = Reflexive particle
- **+Rel		** = Relative particle
- **+RelInd		** = rel. indirect
- **+RIGHT		** = Right side of parwise symbol (parenthesis or quotation mark)
- **+Rom 	** =
- **+Sbj	** =  Subject pronouns: sí, sé and siad are used only when pron follows predicate verb in  subject position, otherwise í, é and iad are used.
- **+Sem/Amount		    	** =
- **+Sem/Build		    	** =
- **+Sem/Build-room	    	** =
- **+Sem/Cat		    	** =
- **+Sem/Curr		    	** =
- **+Sem/Date		    	** =
- **+Sem/Domain		    	** =
- **+Sem/Domain_Hum	    	** =
- **+Sem/Dummytag	    	** =
- **+Sem/Edu_Hum	    	** =
- **+Sem/Event		    	** =
- **+Sem/Food-med	    	** =
- **+Sem/Group_Hum	    	** =
- **+Sem/Hum		    	** =
- **+Sem/ID			    	** =
- **+Sem/Lang		    	** =
- **+Sem/Mal		    	** =
- **+Sem/Mat		    	** =
- **+Sem/Measr		    	** =
- **+Sem/Money		    	** =
- **+Sem/Obj		    	** =
- **+Sem/Obj-el		    	** =
- **+Sem/Obj-ling	    	** =
- **+Sem/Org		    	** =
- **+Sem/Org_Prod-audio 	** =
- **+Sem/Org_Prod-vis   	** =
- **+Sem/Part		    	** =
- **+Sem/Plc		    	** =
- **+Sem/Prod-vis	    	** =
- **+Sem/Route		    	** =
- **+Sem/Rule		    	** =
- **+Sem/Sign		    	** =
- **+Sem/State		    	** =
- **+Sem/State-sick	    	** =
- **+Sem/Substnc	    	** =
- **+Sem/Sur		    	** =
- **+Sem/Time		    	** =
- **+Sem/Time-clock	    	** =
- **+Sem/Title		    	** =
- **+Sem/Tool-it	    	** =
- **+Sem/Txt		    	** =
- **+Sem/Veh		    	** =
- **+Sem/Year		    	** =
- **+Sg						** = Singular
- **+Short					** = Short determiner, e.g. m', d'
- **+Simp					** = Simple preposition
- **+Slender				** = Adj qualifies a plural noun ending in a slender consonant
- **+Span 					** =
- **+St						** = start bracket, quote etc
- **+Strong					** = same plural form for all cases
- **+Subj			** = Subjunctive mood/particle
- **+Subord			** = Subordinating conjunction
- **+Subst			** = substantive noun, functions like a noun, but lacks full inflectional pardigm
- **+Suf 			** = -s vern suffix e.g. a bhíonns
- **+Sup			** = Superlative particle (s), e.g. is
* +Symbol = independent symbols in the text stream, like £, €, ©
- **+Temp			** = Temporal e.g. inniu, amárach etc.
- **+Typo 			** = Typos, e.g. ta/ata  instead of tá/atá
- **+Use/-GC		** = 
- **+Use/-PLX		** = 
- **+Use/-PMatch	** = 
- **+Use/-Spell		** = 
- **+Use/-TTS		** = 
- **+Use/Circ		** = 
- **+Use/GC			** = 
- **+Use/NG			** = 
- **+Use/PMatch		** = 
- **+Use/SpellNoSugg	** = 
- **+Use/TTS		** = 
- **+V				** = n/a (Verb is used)
- **+VD				** = ditransitive verb
- **+VF				** = - form used before a word starting with a vowel or f+vowel 
- **+VI				** = intransitive verb
- **+VT				** = transitive verb
- **+VTI			** = transitive & intransitive verb
- **+Var 			** = variant spelling e.g. rabh instead of raibh or dheachaidh
- **+Vb				** = Verbal particle (Q)
- **+Verb			** = Verb
- **+Verbal			** = Verbal noun
- **+Voc			** = Vocative case 
- **+Vc				** = Vocative particle
- **+Vow			** = Vowel-initial : used to allow past-tense Len e.g. d´ith
- **+Weak			** = Weak plural (noun)
- **+XMLTag			** =  XML tags in the text, e.g. <p>, <title> etc.
- **+Xxx			** =  Indecipherable speech (in transcribed speech)

- **+v1				** = n/a
- **+v2				** = n/a
- **^Adj	** = Adjective- used in initial mutations
- **^Ath	** = Athrú (Change) - in certain plurals the ending changes : "e" -> "í",  "each" -> "í" and "ach" changes to "aí" etc.eg gealach -> gealaí (of the moon)
- **^C		** = nominative, genitive & vocative : initial mutations of plural nouns 
- **^CB		** = compound boundary
- **^Caol	** = Caolú (slenderise)- Attenuation : ie slenderise the end of word 	! Usually by adding an "i" after  the last broad vowel 
- **^Coim	** = Coimriú - Syncopation - the last unstressed vowel is dropped	! eg saghas (type) ->saghs +anna, solas->soils+e (light) - with attenation also
- **^Def	** = dntls rule after definite article
- **^Do		** = d' before Past Imperfect (gnáthchaite) and conditional
- **^Emph	** = emphatic forms
- **^F		** = feminine: initial mutations of singular nouns depend on whether the noun is masculine or feminine
- **^Fr		** = Fréamh (root) use root - i.e.don't syncopate in these cases 
- **^G		** = genitive case
- **^GUESSNOUN	** = n/a - superseded by guesser FSTs
- **^IM		** = initial mutation marker e.g. mo chat, ar an mballa
- **^LC		** = Leathan/Caol: (broad/slender) Leathnaítear an tús mura dtosnaíonn an foirceann le "t"
- **^Lea	** = Leathnú - Broadening eg an "i" is removed 	! súil (eye); radharc na súl (eyesight)
- **^LeaS	** = Leathnaítear an tús mura dtosnaíonn an foirceann le "t"
- **^M 		** = masculine: initial mutations of singular nouns depend on whether the noun is masculine or feminine
- **^Sé		** = Lenition (Séimhiú - softening)- h added after certain initial consonants (bcdfgmpst)
- **^Urú	** = Eclipsis (Urú)- a letter placed before word initial letter  (bcdfgpt), e.g.  "g" before "c" - "an cat" in gen. pl. becomes "bia na gcat", (the cats' food) 
- **^V		** = Verb root
- **^VH		** = Maintains vowel harmony of broad and slender vowels  Motto : "leathan le leathan agus caol le caol" (slender with slender and   broad with broad)
- **^VN		** = verbal noun
- **^aigh 	** = remove -aigh ending
- **^hv		** = "h" before a vowel (eg éan : Nom. Pl. Masc. na héin - the birds) 
- **^igh 	** = remove -igh ending
- **^ts		** = "t" before "s"   eg sagart : Gen Sg.Masc. teach an tsagairt - the priest's house
- **^tv		** = "t-" before a vowel (eg éan : Nom. Sg. Masc. an t-éan - the bird) 

### Flag diacritics

- **@P.Pmatch.Loc 	** = XXX

We have manually optimised the structure of our lexicon using following
flag diacritics to restrict morhpological combinatorics - only allow compounds
with verbs if the verb is further derived into a noun again:
|  @P.NeedNoun.ON@ | (Dis)allow compounds with verbs unless nominalised
|  @D.NeedNoun.ON@ | (Dis)allow compounds with verbs unless nominalised
|  @C.NeedNoun@ | (Dis)allow compounds with verbs unless nominalised

For languages that allow compounding, the following flag diacritics are needed
to control position-based compounding restrictions for nominals. Their use is
handled automatically if combined with +CmpN/xxx tags. If not used, they will
do no harm.
|  @P.CmpFrst.FALSE@ | Require that words tagged as such only appear first
|  @D.CmpPref.TRUE@ | Block such words from entering ENDLEX
|  @P.CmpPref.FALSE@ | Block these words from making further compounds
|  @D.CmpLast.TRUE@ | Block such words from entering R
|  @D.CmpNone.TRUE@ | Combines with the next tag to prohibit compounding
|  @U.CmpNone.FALSE@ | Combines with the prev tag to prohibit compounding
|  @P.CmpOnly.TRUE@ | Sets a flag to indicate that the word has passed R
|  @D.CmpOnly.FALSE@ | Disallow words coming directly from root.

Use the following flag diacritics to control downcasing of derived proper
nouns (e.g. Finnish Pariisi -> pariisilainen). See e.g. North Sámi for how to use
these flags. There exists a ready-made regex that will do the actual down-casing
given the proper use of these flags.
|  @U.Cap.Obl@ | Allowing downcasing of derived names: deatnulasj.
|  @U.Cap.Opt@ | Allowing downcasing of derived names: deatnulasj.

## The Root lexicon etc.

- **LEXICON Root			** = 
- **	Abbrev;				** = 
- **	Prepositions;		** = Adpositions = Prepositions in 
- **	Adverb;				** = 
- **	Articles;			** = 
- **	Conjunctions;		** = 
- **	Determiners;		** = 
- **	Interjections;		** = 
- **	Fillers;			** = 
- **	Communicators;		** = 
- **	Events;				** = 
- **	Anonymous;			** = 
- **	Numerals;			** = 
- **	Particles;			** = 
- **	Personal_Pronouns;	** = 

- **	Englishlex;				** = English lexicon including all parts of speech
- **	Communicators-English;	** = English multi word communicators, e.g. d'ya know
- **	Bardiclex;				** = classical Irish lexicon from TCD Bardic corpus - 
- **	Latinlex;				** = Latin lexicom from RIA historical corpus
- **	!Tobar;					** = omitting this (non-standard older forms)

- **	Punctuation;		** = 
- **	Punctuation_ga;		** = 
- **	Symbols;			** = 
- **	XMLTags; 			** = XML tags e.g. <p>, <title> etc.

- **	AdjA;				** = ORIGINAL TEST LEXICON
- **	AdjIrregular;			** = ORIGINAL TEST LEXICON
- **	Adj-BaseOnly;	!AdjBASE;	** = ORIGINAL TEST LEXICON
- **	Adj-IrregComp;	!AI-COMP;	** = ORIGINAL TEST LEXICON
- **	AdjB;				** = punk adjs
- **	AdjC;				** = FP adjs - auto
- **	AdjDath; 			** = colours
- **	AdjE;				** = FP adjs - manual
- **	Adj-FGB1;			** = Foclóir Gaeilge Béarla Uí Dhónaill
- **	Adj-FGB2;			** = Foclóir Gaeilge Béarla Uí Dhónaill
- **	AdjVariants;			** = Adj Variants in FGB
- **	AdjEqualVariants;		** = Adj Variants with Equal Sign in FGB
- **	AdjF;				** = Nationalities
- **	AdjG;				** = additions from gaois.ie bitex

- **	Nouns; 			** = ORIGINAL TEST LEXICON
- **	Dative;			** = ORIGINAL TEST LEXICON
- **	Other;			** = ORIGINAL TEST LEXICON
- **	NounsB;			** = nouns
- **	NounsC;			** = FP nouns (automatic)
- **	NounsD;			** = FP nouns (manual Decl 1-3)
- **	NounsE;			** = FP nouns (manual Decs 4-5)
- **	NounsF;			** = FP nouns (manual Irregular)
- **	NounsH;			** = Various from corpora
- **	NounsIrregular;	** = 
- **	Substantive;  	** = 
- **	NounsFGB1;		** = FGB (O Donaill) automatic (in NCI corpus) 
- **	NounsFGB2;		** = FGB (O Donaill) automatic (additional)
- **	NounsVariants;		** = Variants extracted from FGB
- **	NounsEqualVariants;	** = Variants extracted from FGB (2011 EUD)

- **	NounsG;			** = Proper Nouns - MOVED from Nouns TO Proper Nouns
- **	NP-LEX-FAM;			** = Family Names (Irish)
- **	NP-LEX-FAM-EN;		** = Family Names (English)
- **	NP-LEX-PERS;		** = Personal Names (Irish)
- **	NP-LEX-PERS-EN;		** = Family Names (English)
- **	NP-LEX-EIRE;		** = Ireland - Counties, Cities and Towns (Irish)
- **	NP-LEX-EIRE-EN; 	** = Ireland - Counties, Cities and Towns (English)
- **	NP-LEX-TIR;			** = Countries (Irish)
- **	NP-LEX-TIR-EN;		** = Countries (English)
- **	NP-Irregular;		** = Various Irregular Proper Nouns
- **	NP-LEX-ORG;			** = Organisations
- **	NP-LEX-LOGAINM;		** = Placenames - sample from logainm.ie
- **	NP-LEX-RIACORPAS1;	** = Various Proper nouns from RIA Historical Corpus of Irish

- **	VerbalNounsV;		** = Verbal nouns derived from verb roots
- **	VerbalNounsN;		** = Verbal nouns derived from nouns
- **	VerbalAdjs;			** = Verbal adjectives derived from verb roots
- **	VerbalNounsGenV;	** = Verbal nouns (genitive ase) derived from verb roots
- **	VerbalNounsGenN;	** = Verbal nouns (genitive ase) derived from nouns
- **	VN-Variants;		** = FGB VN variants (VN, VNG & VA included)
- **	VNEqualVariants; 	** = FGB VN = variants (VN, VNG & VA included)

- **	Verbs;				** = Irregular verbs (11)
- **	VerbsC1A;			** = ORIGINAL TEST LEXICON
- **	VerbsC2A;			** = ORIGINAL TEST LEXICON
- **	VerbsB;				** = verbs
- **	VerbsC;				** = FP verbs
- **	VerbsD;				** = FP verbs
- **	Verbs-FGB1;			** = FGB verbs
- **	Verbs-FGB2;			** = FGB verbs
- **	Verb-Variants;		** = FGB verb variants
- **	VerbsEqualVariants;	** = FGB verb = variants

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root.lexc)</small>

---

## src-fst-morphology-stems-abbreviations.lexc.md 

Abbreviations 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/abbreviations.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/abbreviations.lexc)</small>

---

## src-fst-morphology-stems-adjectives.lexc.md 



SEE PREP/NUM etc dá	Adj3-1;	 ! do or de +

I R R E G U L A R   A D J E C T I V E S 

the following always come at the end of the noun/pron/adj and cannot 
be intermingled with other adjectives 
Have moved to Demonstrative Determiners 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adjectives.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/adjectives.lexc)</small>

---

## src-fst-morphology-stems-adpositions.lexc.md 

Prepositions: 

SIMPLE PREPOSITIONS
theses are not preps only copula or conj
this "is" looks like "agus" to me ... removing the prep reading ...
should be subst except in Prep Cmpd - see below : maidir+Prep+Simp:maidir			#;
should be subst:  maille+Prep+Simp:maille			#; ! maille le = along with

COMPOUNDS: PREP + ARTICLE (an/na)

le does not combine with art: but becomes leis before "an"

trí does not combine with art: but becomes tríd before "an"

Hisrorical forms (bardic)

COMPOUNDS: PREP + POSS PRON (a/ár)

COMPOUNDS: PREP + REL. PART. (a/ar)

COMPOUND PREPOSITIONS: PREP + NOUN

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adpositions.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/adpositions.lexc)</small>

---

## src-fst-morphology-stems-adverbs.lexc.md 

Adverbs

word for word, i.e. literally (2019)

MOVED TO ADJ annamh+Adv+Gn:annamh	#;
what about chomh mór/hálainn etc. etc. 

see PART-LEX.TXT (etc.) for following

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adverbs.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/adverbs.lexc)</small>

---

## src-fst-morphology-stems-articles.lexc.md 

Common Functional Words - Articles

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/articles.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/articles.lexc)</small>

---

## src-fst-morphology-stems-bardic.lexc.md 



* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/bardic.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/bardic.lexc)</small>

---

## src-fst-morphology-stems-conjunctions.lexc.md 

CONJUNCTIONS
E. Uí Dhonnchadha
New Irish Grammar by The Christian Brothers, etc.
removed items (subbord conjs) which are pre-verbal (which often have past tense inflection)
e.g. go/gur a/ar nach/nár 
and which often follow (or attach to) a conjunction
e.g. cé go, nuair nach, 
remaining subordinating conjunctions can be followed by verb or copula 
go mb'fhusa an obair ..., go dtógfadh sé
e.g. má bhíonn, más
some still have tense marking as they are combined forms
e.g. sula, sular, murar etc.

#### LEXICON Conjunctions

gur NOT moved to Verb Part as a)always precede a verb b) have tense c) preceded by conjs like nuair, cé - SHOULD BE REMOVED I THINK ???? NO NEED FOT CONJ AS WELL AS SUBORD COP AND SUBORD VERB PART ...

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/conjunctions.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/conjunctions.lexc)</small>

---

## src-fst-morphology-stems-determiners.lexc.md 

DETERMINERS
E. Uí Dhonnchadha

Determiners: Possessives

Determiners: INTERROGATIVES

(definite & indefinite amounts)

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/determiners.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/determiners.lexc)</small>

---

## src-fst-morphology-stems-english.lexc.md 



@dm discourse marker added to distinguish this from Irish so=seo=here

as in Air France, Air India etc.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/english.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/english.lexc)</small>

---

## src-fst-morphology-stems-interjections.lexc.md 

INTERJECTIONS

Interjections

FILLED PAUSES
Fillers in speech

Communicators in speech

Events in speech transcripts, e.g. cough, sneeze etc.

Anonymisation in transcripts/exam scripts

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/interjections.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/interjections.lexc)</small>

---

## src-fst-morphology-stems-numerals.lexc.md 

NUMBERS
E. Uí Dhonnchadha
For Personal Numerals (duine, beirt, triúr) SEE NOUNS

CARDINAL Numbers

ORDINAL Numbers

Number  Operators

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/numerals.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/numerals.lexc)</small>

---

## src-fst-morphology-stems-particles.lexc.md 

PARTICLES
E. Uí Dhonnchadha
Preverbal
Unique Membership classes

tense distiction is unnecessary

relative if can be translated as "who/which/whose/to,on,of etc. whom etc." or "that"

not relative if can't be translated as "who/which/whose/to,on,of etc. whom etc." ???
i.e. complementiser "that" ...

Reflexive (or emphatic) 'féin' moved from pronouns file

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/particles.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/particles.lexc)</small>

---

## src-fst-morphology-stems-pronouns.lexc.md 

Na Forainmneacha Pearsanta 		- The Personal Pronouns (mé,tú, sé, sí..)
Na Forainmneacha Éiginnte 		- Indefinite Pronouns (ceachtar, cibé ...)
Pronominals - words which act like pronouns

Personal Pronouns

Emphatic/Contrastive Pronouns

this is not an independent pronoun - it accompanies an pronoun or noun

Indefinite Pronouns
Interrogative Pronouns (added Feb 05) 
removed Pro from cén as noun complement is needed unlike cé
also include Det Art Sg in det-lex for "a shonrú cén dáta" = which

Copular DEMONSTRATIVE  See also Determiners

PREPOSITIONAL PRONOUNS (CONJUGATED PREPOSITIONS)

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/pronouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/pronouns.lexc)</small>

---

## src-fst-morphology-stems-propernouns.lexc.md 

Moirfeolaíocht na nAinmfhocail Gaeilge (Morphology of Irish Nouns)

South Africa

Mar 2012
Mar 2012

Added. Most popular names.
Male

Female

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/propernouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/propernouns.lexc)</small>

---

## src-fst-morphology-stems-punctuations.lexc.md 

Punctuation

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/punctuations.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/punctuations.lexc)</small>

---

## src-fst-morphology-stems-tags.lexc.md 


Multichar_Symbols

+XMLTag		! 

LEXICON Root
	XMLTags;

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/tags.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/tags.lexc)</small>

---

## src-fst-morphology-stems-tobar.lexc.md 

Tobar - ac Grianna

PLACENAMES

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/tobar.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/tobar.lexc)</small>

---

## src-fst-morphology-stems-verbalnouns.lexc.md 



NOTE: 'druideadh' is commented out since it was not found as a verbal noun
in the corpus, yet chances are that it would get mixed up with 'druideadh'
as independed form of 'druid', i.e. 'ó druideadh an scoil'

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/verbalnouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/verbalnouns.lexc)</small>

---

## src-fst-morphology-stems-verbs.lexc.md 

First Conjugation Verb Stems

Second Conjugation Verb Stems

DEFECTIVE VERBS

SOME COMMON COMPOUNDS
leave out _fios from lemma as it prevents some bí CG rules applying
IRREGULAR VERBS

Irregular Verbs

auto does not lenite

varient
varient
varient
varient
varient
varient
varient
varient	

auto does not lenite

Bardic - historical nonstandard spellings

FORMS NOT LENITED IN POSITIVE PAST TENSE incl IMPERFECT

Mixed Verb Stems

NEEDS FURTHER TESTING OF -X WORDS
and TEST

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/verbs.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/verbs.lexc)</small>

---

## src-fst-orthography-urucaps.xfscript.md 



NOW COMPOSED IN LOOKUP.SCRIPT

* * *

<small>This (part of) documentation was generated from [src/fst/orthography/urucaps.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/orthography/urucaps.xfscript)</small>

---

## src-fst-phonetics-txt2ipa.xfscript.md 



retroflex plosive, voiceless			t`  ʈ	    0288, 648 (` = ASCII 096)
retroflex plosive, voiced			d`	ɖ		0256, 598
labiodental nasal					F 	ɱ		0271, 625
retroflex nasal						n` 	ɳ		0273, 627
palatal nasal						J 	ɲ		0272, 626
velar nasal							N 	ŋ		014B, 331
uvular nasal							N\	ɴ		0274, 628
	
bilabial trill						B\ 	ʙ		0299, 665
uvular trill							R\ 	ʀ		0280, 640
alveolar tap							4	ɾ		027E, 638
retroflex flap						r` 	ɽ		027D, 637
bilabial fricative, voiceless		p\ 	ɸ		0278, 632
bilabial fricative, voiced			B 	β		03B2, 946
dental fricative, voiceless			T 	θ		03B8, 952
dental fricative, voiced				D 	ð		00F0, 240
postalveolar fricative, voiceless	S	ʃ		0283, 643
postalveolar fricative, voiced		Z 	ʒ		0292, 658
retroflex fricative, voiceless		s` 	ʂ		0282, 642
retroflex fricative, voiced			z` 	ʐ		0290, 656
palatal fricative, voiceless			C 	ç		00E7, 231
palatal fricative, voiced			j\ 	ʝ		029D, 669
velar fricative, voiced	        	G 	ɣ		0263, 611
uvular fricative, voiceless			X	χ		03C7, 967
uvular fricative, voiced				R 	ʁ		0281, 641
pharyngeal fricative, voiceless		X\ 	ħ		0127, 295
pharyngeal fricative, voiced			?\ 	ʕ		0295, 661
glottal fricative, voiced			h\	ɦ		0266, 614

alveolar lateral fricative, vl.		K 
alveolar lateral fricative, vd.		K\

labiodental approximant				P (or v\) 
alveolar approximant					r\ 
retroflex approximant				r\` 
velar approximant					M\

retroflex lateral approximant		l` 
palatal lateral approximant			L 
velar lateral approximant			L\
Clicks

bilabial								O\	(O = capital letter) 
dental								|\
(post)alveolar						!\ 
palatoalveolar						=\ 
alveolar lateral						|\|\
Ejectives, implosives

ejective								_>	e.g. ejective p		p_>
implosive							_<	e.g. implosive b	b_<
Vowels

close back unrounded					M
close central unrounded 				1 
close central rounded				} 
lax i								I 
lax y								Y 
lax u								U

close-mid front rounded				2 
close-mid central unrounded			@\ 
close-mid central rounded			8 
close-mid back unrounded				7

schwa	ə							@

open-mid front unrounded				E 
open-mid front rounded				9
open-mid central unrounded			3 
open-mid central rounded				3\ 
open-mid back unrounded				V 
open-mid back rounded				O

ash (ae digraph)						{ 
open schwa (turned a)				6

open front rounded					& 
open back unrounded	        		A 
open back rounded					Q
Other symbols

voiceless labial-velar fricative		W 
voiced labial-palatal approx.		H 
voiceless epiglottal fricative		H\ 
voiced epiglottal fricative			<\ 
epiglottal plosive					>\

alveolo-palatal fricative, vl. 		s\ 
alveolo-palatal fricative, voiced	z\ 
alveolar lateral flap				l\ 
simultaneous S and x					x\ 
tie bar								_
Suprasegmentals

primary stress						" 
secondary stress						% 
long									: 
half-long							:\ 
extra-short							_X 
linking mark							-\
Tones and word accents

level extra high						_T 
level high							_H
level mid							_M 
level low							_L 
level extra low						_B
downstep								! 
upstep								^	(caret, circumflex)

contour, rising						 
contour, falling						_F 
contour, high rising					_H_T 
contour, low rising					_B_L 

contour, rising-falling				_R_F 
(NB Instead of being written as diacritics with _, all prosodic 
marks can alternatively be placed in a separate tier, set off 
by < >, as recommended for the next two symbols.)
global rise						<R> 
global fall						<F>
Diacritics						
									
voiceless						_0	(0 = figure), e.g. n_0
voiced							_v 
aspirated						_h 
more rounded						_O	(O = letter) 
less rounded						_c 
advanced							_+
retracted						_-
centralized						_" 
syllabic							=	(or _=) e.g. n= (or n_=) 
non-syllabic						_^ 
rhoticity						`
									
breathy voiced					_t 
creaky voiced					_k
linguolabial						_N 
labialized						_w 
palatalized						'	(or _j) e.g. t' (or t_j) 
velarized						_G 
pharyngealized					_?\
									
dental							_d 
apical							_a 
laminal							_m
nasalized						~	(or _~) e.g. A~ (or A_~) 
nasal release					_n
lateral release					_l 
no audible release				_}

velarized or pharyngealized		_e 
velarized l, alternatively		5 
raised							_r 
lowered							_o 
advanced tongue root				_A 
retracted tongue root			_q

* * *

<small>This (part of) documentation was generated from [src/fst/phonetics/txt2ipa.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/phonetics/txt2ipa.xfscript)</small>

---

## src-fst-transcriptions-transcriptor-abbrevs2text.lexc.md 



We describe here how abbreviations are in Irish are read out, e.g.
for text-to-speech systems.

For example:

* s.:syntynyt # ;  
* os.:omaa% sukua # ;  
* v.:vuosi # ;  
* v.:vuonna # ;  
* esim.:esimerkki # ; 
* esim.:esimerkiksi # ; 

* * *

<small>This (part of) documentation was generated from [src/fst/transcriptions/transcriptor-abbrevs2text.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/transcriptions/transcriptor-abbrevs2text.lexc)</small>

---

## src-fst-transcriptions-transcriptor-numbers-digit2text.lexc.md 



% komma% :,      Root ;
% tjuohkkis% :%. Root ;
% kolon% :%:     Root ;
% sárggis% :%-   Root ; 
% násti% :%*     Root ; 

* * *

<small>This (part of) documentation was generated from [src/fst/transcriptions/transcriptor-numbers-digit2text.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/transcriptions/transcriptor-numbers-digit2text.lexc)</small>

---

## tools-grammarcheckers-grammarchecker.cg3.md 


IRISH  G R A M M A R   C H E C K E R

## DELIMITERS

* DELIMITERS = "<.>" "<!>" "<?>" "<...>" "<¶>" sent ; 

## TAGS AND SETS

### Tags

This section lists all the tags inherited from the fst, and used as tags
in the syntactic analysis. The next section, **Sets**, contains sets defined
on the basis of the tags listed here, those set names are not visible in the output.

#### Beginning and end of sentence
BOS
EOS

#### Parts of speech tags

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

#### Tags for POS sub-categories

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

#### Tags for morphosyntactic properties

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
VTI
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

#### Semantic tags

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

### Noun errors (Len vs. not Len) after prepositions

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

####  Syntactic tags

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

### Sets containing sets of lists and tags

This part of the file lists a large number of sets based partly upon the tags defined above, and
partly upon lexemes drawn from the lexicon.
See the sourcefile itself to inspect the sets, what follows here is an overview of the set types.

#### Sets for Single-word sets

* LIST INITIAL = "a" "b" "c" "d" "e" "f" "g" "h" "i" "j" "k" "l" "m"  	
*         "n" "o" "p" "q" "r" "s" "t" "u" "v" "w" "x" "y" "z"           	
*         "á" ;  INITIAL

#### Sets for word or not

WORD
any word
* SET REAL-WORD-NOT-ABBR = WORD - Num - Ord - (ABBR N) ; # This is former REALWORD-NOTABBR #!! REAL-WORD-NOT-ABBR 
* SET NOT-COMMA = WORD - COMMA ;  #!! NOT-COMMA 
= * SET NOT-COMMA = WORD - COMMA ;  #!! NOT-COMMA 

#### Case sets

ADLVCASE

CASE-AGREEMENT
CASE

NOT-NOM
NOT-GEN
NOT-ACC

#### Verb sets

##### Verbs and their complements

NOT-V

#### Sets for finiteness and mood

REAL-NEG

MOOD-V

NOT-PRFPRC

#### Sets for person

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

#### Pronoun sets

#### Adjectival sets and their complements

#### Adverbial sets and their complements

#### Sets of elements with common syntactic behaviour

#### NP sets defined according to their morphosyntactic features

#### The PRE-NP-HEAD family of sets

These sets model noun phrases (NPs). The idea is to first define whatever can
occur in front of the head of the NP, and thereafter negate that with the
expression **WORD - premodifiers**.

#### Border sets and their complements

#### Morphoponological sets

#### Grammarchecker sets

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
* LIST &msyn-i-rith-nom-gen = &msyn-i-rith-nom-gen ;     
* LIST &msyn-ie.i. = &msyn-&.i. ;     
* LIST &msyn-inis-de = &msyn-inis-de ;     
* LIST &msyn-inis-do = &msyn-inis-do ;     
* LIST &GEmsyn-len-after-prep = &msyn-len-after-prep ;     
* LIST &msyn-len-after-prep-sfem = &msyn-len-after-prep-sfem ;     
* LIST &msyn-noun-defart = &msyn-noun-defart ;     
* LIST &msyn-possadj-nom-gen = &msyn-possadj-nom-gen ;     
* LIST &msyn-prep-pron = &msyn-prep-pron ;     
* LIST &msyn-gen-case-nouns = &msyn-gen-case-nouns ;     
* LIST &msyn-gen-case-article-masc-sing = &msyn-gen-case-article-masc-sing ;     
* LIST &msyn-gen-case-article-fem-plural = &msyn-gen-case-article-fem-plural ;     
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

## BEFORE-SECTIONS       

* LIST <fixedcase> = <fixedcase>;        
* ADD:fixedcase-np <fixedcase> TARGET Prop ;     	 ,  Never change case of proper nouns

## SECTION       

### spellchecking

* ADD:spell-it-all (&typo SUGGESTWF) (<spelled>) ;      		 = add rule marking typos

* LIST HUMAN-N = "dochtúir" "múinteoir" "bean" "fear" ;    	 (to be moved to other tags)

* **RULE: lex-tá-is ** To change *TÁ* to *IS*

### Gender errors in adjectives

**RULE: msyn-adj-gender** to change Masculine adjective to Feminine if it modifies a feminine noun !!IT WORKS!!

### Prepositions

**ADD:msyn-prep-pron** RULE TO CHANGE A PREPOSITION AND A PRONOUN INTO A PREPOSITIONAL PRONOUN (e.g., AG MÉ = AGAM, ROIMH SIBH = ROMHAIBH) !!IT WORKS!!

**ADD:msyn-h-after-fem-possessive-adjective**: rule to add h to noun following possessor

#### RULE TO ADD LENITION TO NOUNS FOLLOWING PREPOSITIONS

**ADD:msyn-len-after-prep**: 

#### RULE TO LENITE VERBS AFTER THE NEGATIVE PARTICLE NÍ

#### RULE TO LENITE VERBS IN THE PAST TENSE AFTER THE NEGATIVE PARTICLE NÍOR

**ADD:msyn-len-after-prep**: rule to add lenition to nouns following prepositions

#### rule to correct lenition (séimhiú) errors for nouns after certain prepositions

**ADD:msyn-ecl-after-prep**: A rule to correct eclipse errors without an intervening article. !!!IT WORKS!!!

**ADD:msyn-ecl-after-prep-sfem**: Eclipse after preposition ... (sfem?)

#### Rules for lenition

**ADD:msyn-teastaigh-ó**: exchange prep "mé" with "ó" when following "teastaigh"

**ADD:msyn-inis-do** ...

**ADD:msyn-ar-an-aonach**: A rule to correct the error "ag an aonach" to the correct form "ar an aonach".	

**ADD:msyn-ar-a-haon-a-chlog** ...

**ADD:msyn-fada-ó** ...

**ADD:msyn-beag-is-fiú-de** "beag is fiú de" A + "de"	

**ADD:msyn-cúpla-plnoun-sgnoun** ..

#### RULE TO CORRECT PLURAL NOUNS AFTER THE WORD CÚPLA AS THE NOUN AFTER CÚPLA SHOULD BE IN THE SINGULAR FORM. !!IT WORKS!!

#### RULE TO ENSURE THAT NOUNS APPEAR IN THE GENITIVE CASE. !!IT WORKS!! 

**ADD:msyn-gen-case-nouns** ...

### Definiteness errors in nouns

#### RULE TO CORRECT THE GENDER OF NOUNS IF THEY ARE DEFINITE FEMININE NOUNS. !!IT WORKS!!

#### A RULE TO CHANGE THE NOUN AFTER A NOUN AND A POSSESIVE ADJECTIVE TO THE GENITIVE CASE. !!IT WORKS!!

#### A simple grammar checker rule without suggestions: Ensure preceding nominal agrees with the verb

**ADD:use-guillemets**: Simple punctuation rules showing how to change the lemma in the suggestions:

**ADD:use-ellipsis** ...

**ADD:msyn-ar-an-tae**: This rule is for when people put milk in tea. In Irish, the correct way to say it is that milk is put on tea.

This rule is for when people put milk in coffee. In Irish, the correct way to say it is that milk is put on coffee. At is stands, the rule works for Ulaidh Irish. It needs to be changed to work for standard Irish.

**ADD:msyn-ar-an-gcaife** ...

**ADD:msyn-ie.i.** ...

####  A RULE TO INSERT THE PARTICLE A BEFORE A VERB RELATIVE PHRASE !!IT WORKS!!

* * *

<small>This (part of) documentation was generated from [tools/grammarcheckers/grammarchecker.cg3](https://github.com/giellalt/lang-gle/blob/main/tools/grammarcheckers/grammarchecker.cg3)</small>

---

## tools-tokenisers-tokeniser-disamb-gt-desc.pmscript.md 

## Tokeniser for gle

Usage:
```
$ make
$ echo "ja, ja" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa boasttu olmmoš, man mielde lahtuid." | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "márffibiillagáffe" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://github.com/hfst/hfst/wiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1. unknown word-like forms, and
2. unmatched strings
We want to give 1) a match, but let 2) be treated specially by
`hfst-tokenise -a`
Unknowns are made of:
* lower-case ASCII
* upper-case ASCII
* select extended latin symbols
ASCII digits
* select symbols
* Combining diacritics as individual symbols,
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

### Unknown handling
Unknowns are tagged ?? and treated specially with `hfst-tokenise`
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Finally we mark as a token any sequence making up a:
* known word in context
* unknown (OOV) token in context
* sequence of word and punctuation
* URL in context

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-disamb-gt-desc.pmscript](https://github.com/giellalt/lang-gle/blob/main/tools/tokenisers/tokeniser-disamb-gt-desc.pmscript)</small>

---

## tools-tokenisers-tokeniser-gramcheck-gt-desc.pmscript.md 

## Grammar checker tokenisation for gle

Requires a recent version of HFST (3.10.0 / git revision>=3aecdbc)
Then just:
```
$ make
$ echo "ja, ja" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

More usage examples:
```
$ echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa boasttu olmmoš, man mielde lahtuid." | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "márffibiillagáffe" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://github.com/hfst/hfst/wiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1) unknown word-like forms, and
2) unmatched strings
We want to give 1) a match, but let 2) be treated specially by hfst-tokenise -a
* select extended latin symbols
* select symbols
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

TODO: Could use something like this, but built-in's don't include šžđčŋ:

Simply give an empty reading when something is unknown:
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Finally we mark as a token any sequence making up a:
* known word in context
* unknown (OOV) token in context
* sequence of word and punctuation
* URL in context

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-gramcheck-gt-desc.pmscript](https://github.com/giellalt/lang-gle/blob/main/tools/tokenisers/tokeniser-gramcheck-gt-desc.pmscript)</small>

---

## tools-tokenisers-tokeniser-tts-cggt-desc.pmscript.md 

## TTS tokenisation for smj

Requires a recent version of HFST (3.10.0 / git revision>=3aecdbc)
Then just:
```sh
make
echo "ja, ja" \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

More usage examples:
```sh
echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa \
boasttu olmmoš, man mielde lahtuid." \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
echo "márffibiillagáffe" \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://kitwiki.csc.fi/twiki/bin/view/KitWiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1) unknown word-like forms, and
2) unmatched strings
We want to give 1) a match, but let 2) be treated specially by hfst-tokenise -a
* select extended latin symbols
* select symbols
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

TODO: Could use something like this, but built-in's don't include šžđčŋ:

Simply give an empty reading when something is unknown:
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Needs hfst-tokenise to output things differently depending on the tag they get

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-tts-cggt-desc.pmscript](https://github.com/giellalt/lang-gle/blob/main/tools/tokenisers/tokeniser-tts-cggt-desc.pmscript)</small>
