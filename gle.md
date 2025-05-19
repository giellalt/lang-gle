# Irish language model documentation

All doc-comment documentation in one large file.

---

# src-cg3-functions.cg3.md 



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

## HABITIVE MAPPING

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

### sma object

* **<advlEss** (@<ADVL) for ESS-ADVL if; FMAINV to the left
* **<spredEss** (@<SPRED) for N Ess if; FMAINV to the left is intransitive or bargat

## SUBJ MAPPING - leftovers

## OBJ MAPPING - leftovers

## HNOUN MAPPING

* * *

<small>This (part of) documentation was generated from [src/cg3/functions.cg3](https://github.com/giellalt/lang-gle/blob/main/src/cg3/functions.cg3)</small>

---

# src-fst-morphology-affixes-adjectives.lexc.md 

JUN 2012 EUD: Added +Len everywhere lenition is applied i.e. ^Sé 
: May have implications for CG3
Na hAidiactaí Tuairisciúla - Descriptive Adjectives
C O N T I N U A T I O N     C L A S S E S
E. Uí Dhonnchadha
(c)2001

adj following a fem. noun is always lenited (^Sé) regardless of whether 
the preceding noun is lenited or eclipsed (neither ??)
as is the vocative after vocative particle "a"

SAME FORM IS USED FOR COMPARATIVE AND FEM GEN SG

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/adjectives.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/adjectives.lexc)</small>

---

# src-fst-morphology-affixes-nouns.lexc.md 

+Idf is no longer used with base form .. just +DefArt after article ...
## Moirfeolaíocht na nAinmfhocail Gaeilge (Morphology of Irish Nouns)

FEMININE NOUN continuation classes
Weak Plurals : 
Broad singular is made slender; plural already broad

Weak Plurals : Broaden 

Singular already slender; plural is made broad

gamhain - gamhna (gs), midheamhain - midheamhna (gs)

Strong Plurals :  +(e)anna

tóin -> tóineanna
scoth -> scothanna
EXCEPTION: an chuid -> na codanna see FIX file
EXCEPTION: an raith -> na rathanna see FIX file

Strong Plurals : +í

an bhearna -> na bearnaí
an eala -> na healaí

Strong Plurals : Athrú e -> í

an aicme -> na haicmí (classes)
an táille -> na táillí (fees)

Strong Plurals : 

various ending in vowel  ! plurals +nna

Strong Plurals : Leathnú  +acha

an bheoir -> na beoracha (beers)

Gen Sg : Coim + ach

an chathaoir -> na cathaoireacha (chairs) (Note long vowel aoi is not sync.
an cathair -> na cathracha

Gen Sg : Coim + a
samhail -> samhla
anacair -> anacra

Gen Sg : Coim + Slen + e
crithir - critre
fothair - foithre

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

Strong Plurals : +í

(A) nouns ending in -ín (a diminutive)
smidiríní (smithereens) no singular
eg. an cailín -> na cailíní (girls)
eg. an báidín -> na báidíní (small boats)

(B) nouns ending in -a
eg. an balla -> na ballaí (walls)

Strong Plurals : +idí
an fiche -> na fichidí (the twenties) eidí needs correcting
an caoga -> na caogaidí (the fifties)

INITIAL MUTATIONS
NOMINATIVE SINGULAR 
definite article eg. an cat (m) (p38 NIG)
an t-éan(m) - the bird (p39 NIG) 
an bhróg(f) - the shoe
initial mutation for other reasons
e.g. comp. preps. ar an gcnoc, poss. mo chat

^IM = initial mutation e.g. with prepositions, and possession
Singular:
e.g. ar an bhosca, ar an mbosca
possessive markers on vowels: ár n-athair, a (f) hathair, 
Plural:
e.g. ar bhoscaí, i mboscaí
possessive e.g. ár n-aithreacha - our fathers (^C)

indefinite => no initial mutation
appending the +Len & +Ecl rather than creating seperate forms ...
adds ^h to vowel-initial words ...  but adds the +hPref to all words ... see fix file
just vowel-initial e.g. doras, fiú etc.
although no initial mutation takes place 

GENITIVE SINGULAR 

eg. tábhacht a n-oidhreachta
eg. bia cait, bia sagairt, bia stóir, 
bia rúin, pobail  
siopa grósaera - a grocer's shop
eg. bia an chait,an íl, bia an stóir 
bia an éin (the bird's food)
eg. bia an tsagairt (overgenerates 
tshagairt, h will be removed,
eg. bia an rúin, an phobail
eg. siopa an ghrósaera - the grocer's shop
VOCATIVE SINGULAR 
Since this is trivial (always ^Sé) it is included with Final Mutations
in Voc-sg-0 and Voc-sg-1.

FINAL MUTATIONS
NOMINATIVE SINGULAR

GENITIVE SINGULAR 

VOCATIVE SINGULAR 

ALL PLURALS

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/nouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/nouns.lexc)</small>

---

# src-fst-morphology-affixes-prefixes.lexc.md 

Prefixes
Prefixes in the Irish language are bound to beginning of other words.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/prefixes.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/prefixes.lexc)</small>

---

# src-fst-morphology-affixes-propernouns.lexc.md 

Proper noun inflection
The Irish language proper nouns inflect in the same cases as regular
nouns, but with a colon (':') as separator.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/propernouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/propernouns.lexc)</small>

---

# src-fst-morphology-affixes-symbols.lexc.md 


# Symbol affixes

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/symbols.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/symbols.lexc)</small>

---

# src-fst-morphology-affixes-verbs.lexc.md 



inserted +Len +Uru to distinguish between a bhíonn & a mbíonn Dir/Indir
Rel clauses Dec 2004
inserted ^Verb (x5) in NegQ (EUD 14-10-2017)

FORMS NOT LENITED IN POSITIVE PAST TENSE incl IMPERFECT

áil -> Gen ála

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/verbs.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/verbs.lexc)</small>

---

# src-fst-morphology-phonology.nounadj.xfscript.md 



a d h      -> [%^FC ]   ||  [d|n|t|l|s] %^X _ %^Ath (%^Caol) t

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.nounadj.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.nounadj.xfscript)</small>

---

# src-fst-morphology-phonology.twolc.md 

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

# src-fst-morphology-phonology.verb.xfscript.md 

Verbal Noun Gen

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.verb.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.verb.xfscript)</small>

---

# src-fst-morphology-root-adj.lexc.md 


INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

# Multichar_Symbols definitions

## Analysis symbols
The morphological analyses of wordforms of UNDEFINED language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).

Subj is used for subjunctive

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root-adj.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root-adj.lexc)</small>

---

# src-fst-morphology-root-noun-all.lexc.md 


INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

# Multichar_Symbols definitions

## Analysis symbols
The morphological analyses of wordforms of UNDEFINED language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).

Subj is used for subjunctive

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root-noun-all.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root-noun-all.lexc)</small>

---

# src-fst-morphology-root-others.lexc.md 


INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

# Multichar_Symbols definitions

## Analysis symbols
The morphological analyses of wordforms of UNDEFINED language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).

Subj is used for subjunctive

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root-others.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root-others.lexc)</small>

---

# src-fst-morphology-root-verb-all.lexc.md 


INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

# Multichar_Symbols definitions

## Analysis symbols
The morphological analyses of wordforms of UNDEFINED language are presented
in this system in terms of following symbols.
(It is highly suggested to follow existing standards when adding new tags).

Subj is used for subjunctive

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root-verb-all.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root-verb-all.lexc)</small>

---

# src-fst-morphology-root.lexc.md 


# Irish morphological analyser                      !
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.

# Definitions for Multichar_Symbols

## Analysis symbols
The morphological analyses of wordforms for the Irish
language are presented in this system in terms of the following symbols.
(It is highly suggested to follow existing standards when adding new tags).

- **+Adv		** = Adverb

- **+Gn		** = General
- **+Its		** = intensifiers e.g. sách, ró- etc.
- **+Q		** = Interrogative
- **+Dir		** = Directional
- **+Loc		** = Locative
- **+Temp		** = Temporal e.g. inniu, amárach etc.

- **+Art	** = article
- **+Def	** = definite 
- **+Masc	** = masculine gender
- **+Fem	** = feminine gender

- **+Com	** = nominative, accusative,dative case
- **+Gen	** = genitive case 

- **+Sg	** = singular
- **+Pl	** = plural

- **+Conj		** = conjunction
- **+Coord		** = co-ordinate
- **+Subord		** = subordinate

- **+Det		** = Determiner, e.g. mo, do
- **+Short		** = Short determiner, e.g. m', d'

- **+Dem		** = Demonstrative
- **+Poss		** = Possessive
- **+Q			** = Interrogative
- **+Idf		** = Indefinite
- **+Def		** = Definite
- **+Qty		** = Quantifier
- **+Art		** = with article
- **+1P +2P +3P	** = first, sceond or third person

- **+Fem		** =  feminine gender
- **+Masc		** =  masculine gender

- **+Sg +Pl		** = singular or plural in number

- **+CM +CC +CU	** = dialects

- **+Itj		** =  Interjection
- **+Filler		** =  Filled Pause (eh, em,
- **+Cmc		** =  Communicator (yeah, y'know)
- **+Event		** =  Simple Event (laugh, sneeze etc.)
- **+Xxx		** =  Indecipherable speech	

- **+Num		** = Numeral
- **+Card		** = Cardinal (one two three ...)
- **+Ord		** = Ordinal (first, second, third..) i.e.  mo dhá lámh, an chéad dhá theach 
- **+Def		** = after definite article etc. (an, na, aon, céad)

- **+Part		** = Particle (not +Vb) (U)

- **+Voc		** = Vocative (v)
- **+Nm		** = Numeral (m)
- **+Inf		** = Infinitive (i)
- **+Pat		** = Patronym (p) (e.g. Ó, Ní, Uí, le, de ..)
- **+Comp		** = Comparative degree (c)
- **+Sup		** = Superlative degree (s)
- **+Cp		** = cop rel part
- **+Deg		** = degree particle with Adj/Abstract Noun (so loud, so sharp etc..
- **+Ad			** = Adverbial particle "go"

- **+Vb			** = Verbal (Q)

- **+Neg		** = Negative (n)
- **+Q			** = Interrogative verbal particle(q)
- **+NegQ		** = Negative interrogative verbal particle(q)

- **+Rel		** = Relative (r)
- **+Pro		** = rel part + pron

- **+Subj		** = subjunctive
- **+Imp		** = imperative
- **+Cmpl		** = complementizer

- **+Past		** = past tense verbal particle
- **+CU		** = canúint Uladh
- **+CM		** = canúint na Mumhan
- **+CC		** = canúint Chonnachta

- **+Prep		** = Preposition

- **+Simp		** = Simple
- **+Cmpd		** = Compound

- **+Rel		** = with Relative particle
- **+Poss		** = with Possessive 
- **+Art		** = with Article
- **+Deg		** = with Degree Particle
- **+Obj		** = á = "do a" when obj of VN

- **+Pl		** = plural
- **+CU		** = Canuint Uladh

- **+Pron		** = Pronoun
- **+Pro		** = Pronoun with Copula

- **+Prep		** = Prepositional pronoun
- **+Pers		** = Personal
- **+Emph		** = Emphatic (Contrastive) form of personal pronoun 
- **+Ref		** = Reflexive
- **+Idf		** = Indefinite
- **+Dem		** = Demonstrative
- **+1P +2P +3P	** = first, second or third person
- **+Fem		** = feminine gender
- **+Masc		** = masculine gender

- **+Sg +Pl		** = singular or plural in number

Subj is used for subjunctive
- **+Sbj	** =  sí, sé and siad are used only when pron follows predicate verb in 

- **+Punct		** = Abbreviation
- **+Int		** = sentence internal
- **+Fin		** = sentence final
- **+Brack		** = round, square and curly brackets
- **+St		** = start bracket, quote etc
- **+End		** = end bracket, quote etc
- **+Q		** = question mark ?
- **+Bar		** = hyphen, underscore, dash etc.
- **+Quo		** = all quotation marks double, single etc.
- **+Conj +Coord	** = &
* +Symbol = independent symbols in the text stream, like £, €, ©

- **+XMLTag		** = 

- **+1P +2P +3P 	** = First, second and third person
- **+Auto		** = Autonomous 

- **+PresInd	** = Present Indicative
- **+PastInd	** = Past Indicative
- **+FutInd		** = Future Indicative

- **+PastImp	** = Gháthchaite Past Habitual (Imperfect Indicative)
- **+PresImp	** = Gháthláithreach Pres Habitual (Verb bí only)

- **+Cond		** = 

- **+PresSubj	** = Present Subjunctive
- **+PastSubj	** = Past Subjunctive

- **+Imper		** = 

- **+Rel		** = relative forms - direct
- **+RelInd		** = rel. indirect

- **+Dep		** = dependant forms

- **+Cop		** = Copula
- **+Pres		** = copula present & future
- **+Past		** = copula past & conditional

- **+VF		** = - form used before a word starting with a vowel or f+vowel 
- **+Pro		** = - copula - sea
- **+Emph		** = - emphatic forms
- **+CM		** = Canúint na Mumhan
- **+CC		** = Canúint Chonnachta
- **+CU		** = Canúint Uladh

- **^VN		** = verbal noun

- **+Adj	** = adjective
- **+Base	** = positive / base form (changed from +Pos to +Base 10/09/03)
- **+Comp	** = comparative
- **+Masc	** = masculine gender
- **+Fem	** = feminine gender
- **+Com	** = nominative case
- **+Gen	** = genitive case 
- **+Voc	** = vocative case 
- **+Sg	** = singular
- **+Pl	** = plural

- **+Weak	** = when an adj is qualifying a strong plural noun(i.e. noun plural is the 
- **+Strong	** = same for all cases) the adj will also have the same form in all cases

- **+NotSlen ** = qualifies a plural noun ending in a broad consonantor a vowel
- **+hPref	** = prefix e.g. (h)iontach
- **+Ecl	** = eclipsis - urú; e.g. i ngach
- **+Len	** = e.g. ab fhearr, ba mhó

- **^Adj	** = Adjective- used in initial mutations
- **^Sé	** = Séimhiú (softening) Lenition - h added after certain initial 
- **^Urú	** = eclipsis e.g. i ngach 
- **^Ath	** = Athrú (change) word ending
- **^Caol	** = Caolú (slenderise)- Attenuation : ie slenderise the end of word 
- **^Lea	** = Broaden
- **^Coim	** = Syncopate
- **^IM	** = initial mutation
- **^hv	** = h before vowel

- **+Noun	** = noun
- **+Prop	** = proper
- **+Masc	** = masculine gender
- **+Fem	** = feminine gender
- **+Com	** = nominative case 
- **+Gen	** = genitive case 
- **+Voc	** = vocative case 
- **+Dat	** = dative (e.g. teach)
- **+Sg	** = singular
- **+Pl	** = plural
- **+DefArt	** = noun preceeded by definite article (an)
- **+Def	** = noun preceeded by definite article (an)
- **+Idf	** = noun without article (there is no indefinite article)
- **+Strong	** = strong plural 
- **+Weak	** = weak plural
- **+Emph	** = emphasised - ár dteachsa, do theachsa, a teachsa
- **+Subst	** = substantive - functions like a noun, but lack noun inflections
- **+Len	** = (+Sé) lenite after simple prep. eg ar chat
- **+Ecl	** = (+Urú) e.g.  after compound prep eg ar an gcat
- **+Poss	** = possessive e.g. haois, n-aoiseanna 
- **+hPref 	** = h before vowel 
- **+CM	** = canúint na Mumhan, Munster dialect
- **+CC	** = canúint Chonnachta
- **+CU	** = canúint Uladh

- **+Part	** = see irregular nouns
- **+Num	** = see irregular nouns

- **^M 	** = masculine & feminine : initial mutations of singular nouns depend on 
- **^F	** = whether the noun is masculine or feminine

- **^C 	** = nominative, genitive & vocative : initial mutations of plural nouns 
- **^G 	** = depend on the case

- **^Sé	** = Séimhiú (softening) Lenition - h added after certain initial 

- **^tv	** = "t-" before a vowel (eg éan : Nom. Sg. Masc. an t-éan - the bird) 

- **^hv	** = "h" before a vowel (eg éan : Nom. Pl. Masc. na héin - the birds) 

- **^ts	** = "t" before "s" 
- **^Def	** = dntls rule after definite article

- **^Caol	** = Caolú (slenderise)- Attenuation : ie slenderise the end of word 
- **^Lea	** = Leathnú - Broadening eg an "i" is removed 
- **^Coim	** = Coimriú - Syncopation - the last unstressed vowel is dropped
- **^Ath	** = Athrú (Change) - in certain plurals the ending changes : "e" -> "í",
- **^VH	** = Maintains vowel harmony of broad and slender vowels
- **^Emph	** = emphatic forms
- **^IM	** = general initial mutation e.g. mo chat, ar an mballa

- **^CB	** = compound boundary

- **+CmpdNoGen ** = 

- **+Noun	** = noun
- **+Prop	** = proper
- **+Masc	** = masculine gender
- **+Fem	** = feminine gender
- **+Com	** = nominative case 
- **+Gen	** = genitive case 
- **+Voc	** = vocative case 
- **+Sg	** = singular
- **+Pl	** = plural
- **+hPref	** = 
- **+DefArt	** = noun preceeded by definite article (an)
- **+Def	** = noun preceeded by definite article (an)
- **+Idf	** = noun without article (there is no indefinite article)
- **+Strong	** = strong plural 
- **+Weak	** = weak plural
- **+Emph	** = emphasised - ár dteachsa, do theachsa, a teachsa
- **+Len	** = lenite after simple prep. eg ar chat
- **+Prep	** = prefix h before vowel
- **+Ecl	** = after compound prep eg ar an gcat
- **+CM	** = canúint na Mumhan, Munster dialect
- **+CC	** = canúint Chonnachta
- **+CU	** = canúint Uladh

- **+Place	** = Place name
- **+Fam	** = Family Name
- **+Pers	** = Personal Name
- **+Adj	** = +Adj+Base+DeNom are used for adjectives drived from proper nouns
- **+Base	** = e.g. Spáinneach

- **^M 	** = masculine & feminine : initial mutations of singular nouns depend on 
- **^F	** = whether the noun is masculine or feminine

- **^C 	** = nominative, genitive & vocative : initial mutations of plural nouns 
- **^G 	** = depend on the case

- **^Sé	** = Séimhiú (softening) Lenition - h added after certain initial 

- **^Urú	** = Eclipsis - a letter placed before word initial letter  (bcdfgpt)

- **^tv	** = "t-" before a vowel (eg éan : Nom. Sg. Masc. an t-éan - the bird) 

- **^ts	** = "t" before "s" 
- **^Def	** = dntls rule after definite article

- **^Caol	** = Caolú (slenderise)- Attenuation : ie slenderise the end of word 
- **^Lea	** = Leathnú - Broadening eg an "i" is removed 
- **^Coim	** = Coimriú - Syncopation - the last unstressed vowel is dropped
- **^Ath	** = Athrú (Change) - in certain plurals the ending changes : "e" -> "í",
- **^VH	** = Maintains vowel harmony of broad and slender vowels
- **^Emph	** = emphatic forms
- **^IM	** = general initial mutation e.g. mo chat, ar an mballa

- **+VT +VI +VTI +VD ** = transitive, intrans., both trans & intrans
- **+Vow 		** = vowel initial stem
- **+Suf 		** = -s suffix e.g. a bhíonns
- **+Typo 		** = ta/ata  instead of tá/atá
- **+Var 		** = variant spelling e.g. rabh instead of raibh or dheachaidh
- **+1P +2P +3P 	** = First, second and third person
- **+Auto		** = Autonomous 

- **+Sg +Pl		** = Singular and Plural

- **+PresInd	** = Present Indicative
- **+PastInd	** = Past Indicative
- **+FutInd		** = Future Indicative

- **+PastImp	** = Gháthchaite Past Habitual (Imperfect Indicative)
- **+PresImp	** = Gháthláithreach Pres Habitual (Verb bí only - and deireann (abair)

- **+PresSubj	** = Present Subjunctive
- **+PastSubj	** = Past Subjunctive

- **+Rel		** = relative forms - direct
- **+RelInd		** = rel. indirect

- **+Dep		** = dependant forms

- **+Cop		** = Copula
- **+Pres		** = copula present & future
- **+Past		** = copula past & conditional

- **+VF		** = - form used before a word starting with a vowel or f+vowel 
- **+Pron		** = - copula+pron - sea
- **+Art		** = - copula+pron+art - sén
- **+Def		** = - copula+pron+art - sén
- **+Subst		** = - copula+pron+art+noun - séard (is é an rud)
- **+Noun		** = - copula+pron+art+noun - séard (is é an rud)
- **+Emph		** = - emphatic forms
- **+CM		** = Canúint na Mumhan
- **+CC		** = Canúint Chonnachta
- **+CU		** = Canúint Uladh

- **^VN		** = verbal noun

- **+VT		** = transitive
- **+VD		** = ditransitive
- **+VI		** = intransitive
- **+VTI		** = transitive & intransitive
- **+Vow		** = vowel-initial : used to allow past-tense Len e.g. d´ith

- **+1P +2P +3P 	** = First, second and third person
- **+Auto		** = Autonomous 

- **+Sg +Pl		** = Singular and Plural

- **+PresInd	** = Present Indicative
- **+PastInd	** = Past Indicative
- **+FutInd		** = Future Indicative
- **+PastImp	** = Past Imperfect Indicative

- **+Cond		** = 

- **+PresSubj	** = Present Subjunctive
- **+PastSubj	** = Past Subjunctive

- **+Imper		** = 
- **+Neg		** = Negative
- **+Q		** = Interrogative
- **+NegQ		** = 
- **^Sé		** = Séimhiú (Lenite, soften)
- **^Caol		** = Caolaítear an deireadh (Slenderise the ending)
- **^Lea		** = Leathnaítear an tús (Broaden the root)
- **^LeaS		** = Leathnaítear an tús mura dtosnaíonn an foirceann le "t"
- **^LC		** = leathan/Caol: Leathnaítear an tús mura dtosnaíonn an foirceann le "t"

- **^igh 		** = remove -igh ending
- **^aigh 		** = remove -aigh ending
- **^Coim		** = Coimriú (syncopation)
- **^Fr		** = Fréamh (root) use root - i.e.don't syncopate in these cases 
- **^Do		** = d' before Past Past Imperfect (gnáthchaite0 and conditional
- **^hv		** = h before vowel e.g. ná hólaigí ...
- **+NStem	** = de-nominal verbal (action) noun

- **^IM	** = initial mutation

## New tags from 2025
- **+MWE ** = Multi word expression
- **+Err/Orth ** = Orthografical error
- **+Err/SpaceCmp ** = Compound space error

## Flag diacritics
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

- **        Nouns; 			** = ORIGINAL TEST LEXICON
- **	Dative;			** = ORIGINAL TEST LEXICON
- **	Other;			** = ORIGINAL TEST LEXICON
- **	NounsB;			** = nouns
- **	NounsC;			** = FP nouns (automatic)
- **	NounsD;			** = FP nouns (manual Decl 1-3)
- **	NounsE;			** = FP nouns (manual Decs 4-5)
- **	NounsF;			** = FP nouns (manual Irregular)
- **	NounsFGB1;		** = FGB (O Donaill) automatic (in NCI corpus) 
- **	NounsFGB2;		** = FGB (O Donaill) automatic (additional)
- **	NounsVariants;		** = Variants extracted from FGB
- **	NounsEqualVariants;	** = Variants extracted from FGB (2011 EUD)

- **	NP-Irregular;		** = ORIGINAL TEST LEXICON

- **        VerbsC1A;		** = ORIGINAL TEST LEXICON
- **        VerbsC2A;		** = ORIGINAL TEST LEXICON
- **	VerbsB;			** = verbs
- **	VerbsC;			** = FP verbs
- **	Verbs-FGB1;		** = FGB verbs
- **	Verbs-FGB2;		** = FGB verbs
- **	Verb-Variants;		** = FGB verb variants
- **	VerbsEqualVariants;	** = FGB verb = variants

- **	VerbalNouns;		** = Version 3 VNs in TEST Lex & Foclóir Póca
- **	VerbalAdjs;		** = Version 3 VAs in TEST Lex & Foclóir Póca
- **	VerbalNounsGen;		** = Version 4 VNs in TEST Lex & Foclóir Póca
- **	VNVA-FGB1;		** = Foclóir Gaeilge Béarla Ó Dónaill
- **	VN-Variants;		** = FGB VN variants (VN, VNG & VA included)

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/root.lexc)</small>

---

# src-fst-morphology-stems-abbreviations.lexc.md 

Abbreviations 
and a few English words

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/abbreviations.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/abbreviations.lexc)</small>

---

# src-fst-morphology-stems-adjectives.lexc.md 

Na hAidiactaí Tuairisciúla - Descriptive Adjectives

SEE PREP/NUM etc dá	Adj3-1;	 ! do or de +

I R R E G U L A R   A D J E C T I V E S 

the following always come at the end of the noun/pron/adj and cannot 
be intermingled with other adjectives 
Have moved to Demonstrative Determiners 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adjectives.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/adjectives.lexc)</small>

---

# src-fst-morphology-stems-adpositions.lexc.md 

Prepositions: 
Simple: le, ag, ar, etc.
Compound (Na Forainmneacha Réamhfhoclacha) Prepositional Pronouns (agam, agat...)
Emphatic Compound eg agamsa, uaimse, ...

theses are not preps only copula or conj
this "is" looks like "agus" to me ... removing the prep reading ...
should be subst except in Prep Cmpd - see below : maidir+Prep+Simp:maidir			#;
should be subst:  maille+Prep+Simp:maille			#; ! maille le = along with

le does not combine with art: but becomes leis before "an"

trí does not combine with art: but becomes tríd before "an"

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adpositions.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/adpositions.lexc)</small>

---

# src-fst-morphology-stems-adverbs.lexc.md 

Adverbs

MOVED TO ADJ annamh+Adv+Gn:annamh	#;
what about chomh mór/hálainn etc. etc. 

see PART-LEX.TXT (etc.) for following

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adverbs.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/adverbs.lexc)</small>

---

# src-fst-morphology-stems-articles.lexc.md 

Common Functional Words

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/articles.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/articles.lexc)</small>

---

# src-fst-morphology-stems-conjunctions.lexc.md 

## CONJUNCTIONS

removed items (subbord conjs) which are pre-verbal (which often have past tense inflection)
e.g. `go/gur`, `a/ar`, `nach/nár`
and which often follow (or attach to) a conjunction
e.g. `cé go`, `nuair nach`.
Remaining subordinating conjunctions can be followed by verb or copula:
`go mb'fhusa an obair ...`, `go dtógfadh sé`
e.g. `má bhíonn`, `más`.
Some still have tense marking as they are combined forms
e.g. `sula`, `sular`, `murar` etc.

### LEXICON Conjunctions

- **agus**
- **agus**
- **agus**
- **agus**
- **ná**, cf ní ... ná
- **ná**
- **nó**
- **nó**

`gur` (=NOT?) moved to Verb Part as it a) is always precede a verb b) have tense c) is preceded by conjs like `nuair`, `cé`.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/conjunctions.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/conjunctions.lexc)</small>

---

# src-fst-morphology-stems-determiners.lexc.md 

# DETERMINERS

this information is on the noun as initial mutation
use corresponding +Len / +Ecl to deternine whether sing/pl, masc/fem

SEE PRON-LEX cad_chuige+Det+Q:tuige				#;	! what
SEE PRON-LEX cad+Det+Q:cad				#;	! what
SEE PRON-LEX céard+Det+Q:céard			#;	! what
SEE PRON-LEX cé+Det+Q:cé				#;	! who
SEE ADV cá+Det+Q:cá					#;	! where

the following always come at the end of the noun/pron/adj and cannot 
be intermingled with other adjectives 
contextual tagged as demonstrative for now at least ...

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/determiners.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/determiners.lexc)</small>

---

# src-fst-morphology-stems-interjections.lexc.md 

INTERJECTIONS

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/interjections.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/interjections.lexc)</small>

---

# src-fst-morphology-stems-nouns.lexc.md 



new category 28/03/08

SEE N-LEX-IRREG muineál	 Nm1-1;	 ! gs & npl -níl

Automatically assigned CCs

Manually assigned CCs
see n-lex-stems.txt ceathracha	Nm5-1;	! gs ~d pl ~idí

CONTINUATION CLASSES MASCULINE

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/nouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/nouns.lexc)</small>

---

# src-fst-morphology-stems-numerals.lexc.md 

NUMERALS
Cardinal numbers are described seperately here rather than with other
Adjectives
For Personal Numerals (duine, beirt, triúr) SEE NOUNS

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/numerals.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/numerals.lexc)</small>

---

# src-fst-morphology-stems-particles.lexc.md 


PARTICLES
Preverbal
Unique Membership classes

tense distiction is unnecessary

relative if can be translated as "who/which/whose" (or "that")

not relative if can't be translated as "who/which/whose" ???
i.e. complementiser "that" ...

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/particles.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/particles.lexc)</small>

---

# src-fst-morphology-stems-pronouns.lexc.md 

Na Forainmneacha Pearsanta 		- The Personal Pronouns (mé,tú, sé, sí..)
Na Forainmneacha Éiginnte 		- Indefinite Pronouns (ceachtar, cibé ...)
Pronominals - words which act like pronouns

removed Pro from cén as noun complement is needed unlike cé
also include Det Art Sg in det-lex for "a shonrú cén dáta" = which

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/pronouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/pronouns.lexc)</small>

---

# src-fst-morphology-stems-propernouns.lexc.md 



South Africa
Mar 2012
Mar 2012

Added. Most popular names.
Male

Female

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/propernouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/propernouns.lexc)</small>

---

# src-fst-morphology-stems-punctuations.lexc.md 

Abbreviations

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/punctuations.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/punctuations.lexc)</small>

---

# src-fst-morphology-stems-tags.lexc.md 


Multichar_Symbols

+XMLTag		! 

LEXICON Root
	XMLTags;

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/tags.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/tags.lexc)</small>

---

# src-fst-morphology-stems-tobar.lexc.md 

Tobar - ac Grianna

PLACENAMES

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/tobar.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/tobar.lexc)</small>

---

# src-fst-morphology-stems-verbalnouns.lexc.md 



Foclóir Póca etc.
April 2008: Regenerated from verb stems by Christoph Wendler 
(v=sceamh) CHECKED

NOTE: 'druideadh' is commented out since it was not found as a verbal noun
in the corpus, yet chances are that it would get mixed up with 'druideadh'
as independed form of 'druid', i.e. 'ó druideadh an scoil'

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/verbalnouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/verbalnouns.lexc)</small>

---

# src-fst-morphology-stems-verbs.lexc.md 



DEFECTIVE VERBS

SOME COMMON COMPOUNDS
leave out _fios from lemma as it prevents some bí CG rules applying
IRREGULAR VERBS

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

NEEDS FURTHER TESTING OF -X WORDS
and TEST

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/verbs.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/verbs.lexc)</small>

---

# src-fst-orthography-urucaps.xfscript.md 



NOW COMPOSED IN LOOKUP.SCRIPT

* * *

<small>This (part of) documentation was generated from [src/fst/orthography/urucaps.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/orthography/urucaps.xfscript)</small>

---

# src-fst-phonetics-txt2ipa.xfscript.md 



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

# src-fst-transcriptions-transcriptor-abbrevs2text.lexc.md 



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

# src-fst-transcriptions-transcriptor-numbers-digit2text.lexc.md 



% komma% :,      Root ;
% tjuohkkis% :%. Root ;
% kolon% :%:     Root ;
% sárggis% :%-   Root ; 
% násti% :%*     Root ; 

* * *

<small>This (part of) documentation was generated from [src/fst/transcriptions/transcriptor-numbers-digit2text.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/transcriptions/transcriptor-numbers-digit2text.lexc)</small>

---

# tools-grammarcheckers-grammarchecker.cg3.md 


IRISH  G R A M M A R   C H E C K E R

# DELIMITERS

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

N
A
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
Ill
Loc
Com
Ess
Par
Voc
Sg
Du
Pl
Cmp/SplitR
Cmp/SgNom Cmp/SgGen
Cmp/SgGen
PxSg1
PxSg2
PxSg3
PxDu1
PxDu2
PxDu3
PxPl1
PxPl2
PxPl3
Px

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

### Lookalikes

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

INITIAL

### Sets for word or not

WORD
NOT-COMMA

### Case sets

ADLVCASE

CASE-AGREEMENT
CASE

NOT-NOM
NOT-GEN
NOT-ACC

### Verb sets

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

### Grammarchecker sets

* * *

<small>This (part of) documentation was generated from [tools/grammarcheckers/grammarchecker.cg3](https://github.com/giellalt/lang-gle/blob/main/tools/grammarcheckers/grammarchecker.cg3)</small>

---

# tools-tokenisers-tokeniser-disamb-gt-desc.pmscript.md 

# Tokeniser for gle

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

## Unknown handling
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

# tools-tokenisers-tokeniser-gramcheck-gt-desc.pmscript.md 

# Grammar checker tokenisation for gle

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

# tools-tokenisers-tokeniser-tts-cggt-desc.pmscript.md 

# TTS tokenisation for smj

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
