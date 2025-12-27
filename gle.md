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

## src-fst-morphology-affixes-adjectives.lexc.md 

## Na hAidiactaí Tuairisciúla - Descriptive Adjectives
E. Uí Dhonnchadha
(c)2001
JUN 2012 EUD: Added +Len everywhere lenition is applied i.e. ^Sé 
: May have implications for CG3
###		C O N T I N U A T I O N     C L A S S E S
```
___________________________________________________
####					T Y P E   1
##### 1st. Declension TYPE 1
	MONOSYLLABIC & ENDING IN	-LL (except dall)
1st. Declension TYPE 2
	MONOSYLLABIC : OTHERS
	POLYSYLLABIC & ENDING IN -(MH)AR
**Genitive Singular Masc.	} attenuate	(Noun Declension 1)
1st. Declension TYPE 3
	POLYSYLLABIC & ENDING IN 	-ACH
**Genitive Singular Masc.	} change each->igh, ach->aigh (like Noun Declension 1)
**Vocative Singular Masc.	}
**Genitive Singular Fem.	: change each->í,   ach->aí   (like Noun Declension 2)
1st. Declension TYPE 4
	POLYSYLLABIC & ENDING IN 	-ÍOCH
OR IS IT och -> [] + che ???????
BACK TO USING SAME AS COMPARATIVE FORM IF NECESSARY AT A LATER STAGE).
1st. Declension TYPE 5
	POLYSYLLABIC & ENDING IN 	LONG VOWEL + CH (except lách)
2nd. Declension TYPE 1
	POLYSYLLABIC & ENDS IN 	-IÚIL
2nd. Declension TYPE 2
	OTHERS
3rd. Declension TYPE 1
	ALL (except a few cases - i.e. breá, te)
- LEXICON Adj1-1 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

- LEXICON Adj1-2 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

- LEXICON Adj1-3 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

- LEXICON Adj1-4 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

- LEXICON Adj1-5 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

- LEXICON Adj2-1 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

- LEXICON Adj2-2 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

- LEXICON Adj3-1 
- AdjBASE; 
- +Adj+Comp:0 #; 

- LEXICON Adj4-1 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 
- +Adj:^Adj^Coim Fem_gen-D2A_sg;  sync + slen + e

- LEXICON Adj4-2 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

- LEXICON Adj4-3 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

- LEXICON Adj4-4 
- AdjBASE; 
- +Adj+Fem+Com:^Adj Fem_nom_voc_sg; 

#### ADJECTIVES QUALIFYING FEM SINGULAR NOUNS

- LEXICON Fem_nom_voc_sg 
adj following a fem. noun is always lenited (^Sé) regardless of whether 
the preceding noun is lenited or eclipsed (neither ??)
as is the vocative after vocative particle "a"

- +Sg+Len:^Sé #; 

- LEXICON Fem_gen-D2A_sg  like Noun Declension 2
- +Fem+Gen+Sg:^Caole #; 
- +Comp:^Caole #; 

- LEXICON Fem_gen-D2B_sg  like Noun Declension 2 but without "e" appended

- LEXICON Fem_gen-D2C_sg  a new change

- LEXICON Fem_gen-D2D_sg  a new change

- LEXICON Fem_gen-D3_sg  like Noun Declension 3

- LEXICON Masc_nom_sg 

- LEXICON Masc_gen-D4_voc_sg  like Noun Declension 4

- +Sg+Len:^Sé #;  hata an fhir bhig - the small man's hat

- LEXICON Masc_gen-D1_voc_sg  like Noun Declension 1

- +Sg+Len:^Caol^Sé #;  

- LEXICON PL-A 
- +Pl:a #;  adj is NOT lenited after a noun ending in a 
-   broad consonantor a vowel! E.G. na mná móra - the big women

- LEXICON PL-A-SLENDER 

- +Pl+Len:a^Sé #;  adj IS lenited after a noun ending in a 
-   slender consonantE.G. na fir bheaga - the small men

- +Pl:e #;  adj is NOT lenited after a noun ending in a 
-   broad consonantor a vowel

-   cathair (city) is a noun with strong plurals
-   obair na bpáistí maithe (work of the good childres)

-   vocative: a pháistí mhaithe - O good children
- LEXICON PL-E-SLENDER 

- +Pl+Len:e^Sé #;  adj IS lenited after a noun ending in a 

- LEXICON PL-TADA-ADJ 	
- +Pl:0 #;  bean (woman) is a noun with weak plurals
- LEXICON AdjBASE 
- +Adj+Base:0 #; 
- +Adj+Base+hPref:^IM^hv #;  e.g. go hiontach
- +Adj+Base+Len:^IM^Sé #;  e.g. ba bhreá, BÁC Thuaidh (adj)

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/adjectives.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/adjectives.lexc)</small>

---

## src-fst-morphology-affixes-nouns.lexc.md 

## Moirfeolaíocht na nAinmfhocail Gaeilge (Morphology of Irish Nouns)
+Idf is no longer used with base form .. just +DefArt after article ...

### FEMININE NOUN continuation classes
Weak Plurals : 
Broad singular is made slender; plural already broad

- LEXICON Nf2-SINGULAR 

- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G Gen-sg-D2; 

- LEXICON Nf2a-SINGULAR 

- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G Gen-sg-D2a; 

- LEXICON Nf2-1 
- Nf2-SINGULAR; 
- +Noun+Fem+Com:^C PL-(LEA)A; 
- +Noun+Fem+Gen+Weak:^G PL-TADA; 
- +Noun+Fem+Voc:^V PL-(LEA)A; 

- LEXICON Nf2-1a 
- Nf2a-SINGULAR; 
- +Noun+Fem+Com:^C PL-(LEA)A; 
- +Noun+Fem+Gen+Weak:^G PL-TADA; 
- +Noun+Fem+Voc:^V PL-(LEA)A; 

#### Weak Plurals : Broaden 

##### Singular already slender; plural is made broad

- LEXICON Nf2-2 
- Nf2-SINGULAR; 
- +Noun+Fem+Com:^C PL-(LEA)A; 

###### Weak Plurals : 

- LEXICON Nf2-3 

###### Weak Plurals : 

- +Noun+Fem+Com:^C PL-(CAOL)E; 
- +Noun+Fem+Gen+Weak:^G PL-LEATHNÚ; 
- +Noun+Fem+Voc:^V PL-(CAOL)E; 

- LEXICON Nf2-4 

- Nf2a-SINGULAR; 
- +Noun+Fem+Com:^C PL-(LEA)A; 

#### STRONG PLURALS

- LEXICON Nf2-5 

- Nf2-SINGULAR; 

- +Noun+Fem+Com:^C PL-TE; 
- +Noun+Fem+Gen+Strong:^G PL-TE; 
- +Noun+Fem+Voc:^V PL-TE; 

- LEXICON Nf2-6 

- Nf2-SINGULAR; 
- +Noun+Fem+Com:^C PL-(E)ANNA; 
- +Noun+Fem+Gen+Strong:^G PL-(E)ANNA; 
- +Noun+Fem+Voc:^V PL-(E)ANNA; 

- LEXICON Nf2-7 
- Nf2-SINGULAR; 
- +Noun+Fem+Com:^C PL-Í; 
- +Noun+Fem+Gen+Strong:^G PL-Í; 
- +Noun+Fem+Voc:^V PL-Í; 

- LEXICON Nf2-8 
- +Noun+Fem+Com:^C PL-(E)ACHA; 
- +Noun+Fem+Gen+Strong:^G PL-(E)ACHA; 
- +Noun+Fem+Voc:^V PL-(E)ACHA; 

- LEXICON Nf2-9 
- Nf2-SINGULAR; 
- +Noun+Fem+Com:^C PL-(LEA)THA; 
- +Noun+Fem+Gen+Strong:^G PL-(LEA)THA; 
- +Noun+Fem+Voc:^V PL-(LEA)THA; 

- LEXICON Nf2-10 
- Nf2-SINGULAR; 
- +Noun+Fem+Com:^C PL-TA; 
- +Noun+Fem+Gen+Strong:^G PL-TA; 
- +Noun+Fem+Voc:^V PL-TA; 

- LEXICON Nf2-11 
- Nf2-SINGULAR; 
- +Noun+Fem+Com:^C PL-(E)ANTA; 
- +Noun+Fem+Gen+Strong:^G PL-(E)ANTA; 
- +Noun+Fem+Voc:^V PL-(E)ANTA; 

- LEXICON Nf2-12 
- Nf2-SINGULAR; 
- +Noun+Fem+Com:^C PL-(LEA)A; 
- +Noun+Fem+Gen+Strong:^G PL-(LEA)A; 
- +Noun+Fem+Voc:^V PL-(LEA)A; 

- LEXICON Nf2-13 
- Nf2-SINGULAR; 
- +Noun+Fem+Com:^C PL-(CAOL)E; 
- +Noun+Fem+Gen+Strong:^G PL-(CAOL)E; 
- +Noun+Fem+Voc:^V PL-(CAOL)E; 

#### 3rd Declension
#### Strong Plurals : +aí

an bheannacht -> na beannachtaí

- LEXICON Nf3-SINGULAR 
- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G Gen-sg-D3; 
- +Noun+Fem+Voc:^F^V Voc-sg-0; 

- LEXICON Nf3a-SINGULAR 
- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G^Ath Gen-sg-D3;  EXCEPTION t-> th,  t->[], dh ->t
- +Noun+Fem+Voc:^F^V Voc-sg-0; 

gamhain - gamhna (gs), midheamhain - midheamhna (gs)
- LEXICON Nf3b-SINGULAR 
- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G^Coim Gen-sg-D3;  SYNC + a 
- +Noun+Fem+Voc:^F^V Voc-sg-0; 

- LEXICON Nf3-1 
- Nf3-SINGULAR; 
- +Noun+Fem+Com:^C PL-AÍ; 
- +Noun+Fem+Gen+Strong:^G PL-AÍ; 
- +Noun+Fem+Voc:^V PL-AÍ; 

- LEXICON Nf3-2 
- Nf3a-SINGULAR; 
- +Noun+Fem+Com:^C^Ath^Lea PL-AÍ; 
- +Noun+Fem+Gen+Strong:^G^Ath^Lea PL-AÍ; 
- +Noun+Fem+Voc:^V^Ath^Lea PL-AÍ; 

Strong Plurals :  +(e)anna

tóin -> tóineanna
scoth -> scothanna
EXCEPTION: an chuid -> na codanna see FIX file
EXCEPTION: an raith -> na rathanna see FIX file
- LEXICON Nf3-3 
- Nf3-SINGULAR; 
- +Noun+Fem+Com:^C PL-(E)ANNA; 
- +Noun+Fem+Gen+Strong:^G PL-(E)ANNA; 
- +Noun+Fem+Voc:^V PL-(E)ANNA; 

- LEXICON Nf3-4 
- Nf3a-SINGULAR; 
- +Noun+Fem+Com:^C PL-Í; 
- +Noun+Fem+Gen+Strong:^G PL-Í; 
- +Noun+Fem+Voc:^V PL-Í; 

- LEXICON Nf3-5 
- Nf3-SINGULAR; 
- +Noun+Fem+Com:^C^Lea PL-TA; 
- +Noun+Fem+Gen+Strong:^G^Lea PL-TA; 
- +Noun+Fem+Voc:^V^Lea PL-TA; 

- LEXICON Nf3-6 
- Nf3-SINGULAR; 
- +Noun+Fem+Com:^C PL-(E)ACHA; 
- +Noun+Fem+Gen+Strong:^G PL-(E)ACHA; 
- +Noun+Fem+Voc:^V PL-(E)ACHA; 

- LEXICON Nf3-6a 
- Nf3-SINGULAR; 
- +Noun+Fem+Com:^C PL-(LEA)ACHA; 
- +Noun+Fem+Gen+Strong:^G PL-(LEA)ACHA; 
- +Noun+Fem+Voc:^V PL-(LEA)ACHA; 

- LEXICON Nf3-7 
- Nf3-SINGULAR; 
- +Noun+Fem+Com:^C PL-TE; 
- +Noun+Fem+Gen+Strong:^G PL-TE; 
- +Noun+Fem+Voc:^V PL-TE; 

Strong Plurals :  Broaden +anna

an chuid -> na codanna see FIX file
an raith -> na rathanna
an laith -> na lathanna
an luaith -> na luathanna
- LEXICON Nf3-8 
- Nf3-SINGULAR; 
- +Noun+Fem+Com:^C^Lea PL-(E)ANNA; 
- +Noun+Fem+Gen+Strong:^G^Lea PL-(E)ANNA; 
- +Noun+Fem+Voc:^V^Lea PL-(E)ANNA; 

- LEXICON Nf4-SINGULAR 
- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G Gen-sg-D4; 
- +Noun+Fem+Voc:^F^V Voc-sg-0; 

Strong Plurals : +í

an bhearna -> na bearnaí
an eala -> na healaí

- LEXICON Nf4-1 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C PL-Í; 
- +Noun+Fem+Gen+Strong:^G PL-Í; 
- +Noun+Fem+Voc:^V PL-Í; 

Strong Plurals : Athrú e -> í

an aicme -> na haicmí (classes)
an táille -> na táillí (fees)

- LEXICON Nf4-2 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C^Ath PL-Í; 
- +Noun+Fem+Gen+Strong:^G^Ath PL-Í; 
- +Noun+Fem+Voc:^V^Ath PL-Í; 

Strong Plurals : 

- LEXICON Nf4-3 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C^Ath PL-TE; 
- +Noun+Fem+Gen+Strong:^G^Ath PL-TE; 
- +Noun+Fem+Voc:^V^Ath PL-TE; 

- LEXICON Nf4-4 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C^Ath PL-THE; 
- +Noun+Fem+Gen+Strong:^G^Ath PL-THE; 
- +Noun+Fem+Voc:^V^Ath PL-THE; 

- LEXICON Nf4-5 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C PL-(E)ACHA; 

- LEXICON Nf4-6 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C PL-(E)ANNA; 
- +Noun+Fem+Gen+Strong:^G PL-(E)ANNA; 
- +Noun+Fem+Voc:^V PL-(E)ANNA; 

- LEXICON Nf4-7 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C PL-(E)ANTA; 
various ending in vowel	! plurals +nna
- LEXICON Nf4-8 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C PL-NNA; 
- +Noun+Fem+Gen+Strong:^G PL-NNA; 
- +Noun+Fem+Voc:^V PL-NNA; 
- LEXICON Nf4-9 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C PL-ONNA; 
- +Noun+Fem+Gen+Strong:^G PL-ONNA; 
- +Noun+Fem+Voc:^V PL-ONNA; 
- LEXICON Nf4-10 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C PL-OCHA; 
- +Noun+Fem+Gen+Strong:^G PL-OCHA; 
- +Noun+Fem+Voc:^V PL-OCHA; 
- LEXICON Nf4-11 
- Nf4-SINGULAR; 
- +Noun+Fem+Com:^C^Ath PL-TÍ; 
- +Noun+Fem+Gen+Strong:^G^Ath PL-TÍ; 
- +Noun+Fem+Voc:^V^Ath PL-TÍ; 

Strong Plurals : Leathnú  +acha

an bheoir -> na beoracha (beers)

- LEXICON Nf5-1 

Gen Sg : Coim + ach
Strong Plurals : Coimriú +eacha

an chathaoir -> na cathaoireacha (chairs) (Note long vowel aoi is not sync.
an cathair -> na cathracha

- LEXICON Nf5-2 

- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G Gen-sg-D5-2; 

Gen Sg : Coim + a
Strong Plurals : Coimriú +(e)acha
samhail -> samhla
anacair -> anacra
- LEXICON Nf5-2a 
- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G Gen-sg-D5-2a; 

Gen Sg : Coim + Slen + e
Strong Plurals : Coimriú +(e)acha
crithir - critre
fothair - foithre
- LEXICON Nf5-2b 

- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G Gen-sg-D5-2b; 

- LEXICON Nf5-3 
- +Noun+Fem+Com:^F^C Nom-sg; 

- LEXICON Nf5-4 
- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G Gen-sg-D5-5; 

tarraingt - tarraingthe - tarraingtí
- LEXICON Nf5-7  11/04/08

- +Noun+Fem+Com:^F^C Nom-sg; 
- +Noun+Fem+Gen:^F^G Gen-sg-D5-7; 

### MASCULINE NOUN continuation classes

- LEXICON Nm1-SINGULAR 
- +Noun+Masc+Com:^M^C Nom-sg; 
- +Noun+Masc+Gen:^M^G Gen-sg-D1; 
- +Noun+Masc+Voc:^M^V Voc-sg-1; 

WEAK PLURALS (i.e. where the nominative and genitive plurals are different) 
TYPE 1 Nom pl. ends in conson. eg cat : cait, fear : fir, marcach: marcaigh 

- LEXICON Nm1-1 

- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C PL-CAOLÚ; 
- +Noun+Masc+Gen+Weak:^G PL-TADA; 
- +Noun+Masc+Voc:^V PL-(LEA)A; 

TYPE 2 Nom pl. formed by adding -a eg cos : cosa, úll : úlla 

- LEXICON Nm1-2 

- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C PL-(LEA)A; 
- +Noun+Masc+Gen+Weak:^G PL-TADA; 

(TYPE 3) Nom pl. formed by adding -ta eg 

- LEXICON Nm1-3 
- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C PL-TA; 
- +Noun+Masc+Gen+Strong:^G PL-TA; 

- LEXICON Nm1-4 
- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C PL-(LEA)THA; 
- +Noun+Masc+Gen+Strong:^G PL-(LEA)THA; 

- LEXICON Nm1-5 
- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C PL-ATHRÚ; 
- +Noun+Masc+Gen+Strong:^G PL-ATHRÚ; 

- LEXICON Nm1-6 
- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C PL-(E)ANNA; 
- +Noun+Masc+Gen+Strong:^G PL-(E)ANNA; 
- LEXICON Nm1-7 
- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C^Caol PL-Í; 

- LEXICON Nm1-8 
- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C^Coim PL-(E)ANNA; 

- LEXICON Nm1-9 
- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C^Coim PL-(CAOL)E; 

- LEXICON Nm1-10 
- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C^Coim PL-(CAOL)EACHA; 

- LEXICON Nm1-11 
- Nm1-SINGULAR; 
- +Noun+Masc+Com:^C PL-(E)ACHA; 
### 2nd Declension
sliabh -> na sléibhte 

- LEXICON Nm2-SINGULAR 
- +Noun+Masc+Com:^M^C Nom-sg; 

- LEXICON Nm2-1 
- Nm2-SINGULAR; 
- +Noun+Masc+Com:^C^Caol PL-TE; 

- LEXICON Nm3-SINGULAR 
- +Noun+Masc+Com:^M^C Nom-sg; 
- LEXICON Nm3a-SINGULAR 
- +Noun+Masc+Com:^M^C Nom-sg; 
3rd Declension
Strong Plurals : +í 
as in Nm7 but singular are different

eg. bádóir -> na bádóirí

- LEXICON Nm3-1 
- Nm3-SINGULAR; 
- +Noun+Masc+Com:^C PL-Í; 

Strong Plurals : +anna

eg. an bláth -> na bláthanna

- LEXICON Nm3-2 
- Nm3-SINGULAR; 
- +Noun+Masc+Com:^C PL-(E)ANNA; 
Strong Plurals : +aí

- LEXICON Nm3-3 
- Nm3-SINGULAR; 
- +Noun+Masc+Com:^C PL-AÍ; 

gen briocht -> breachta
Strong Plurals : +aí
briocht -> briochtaí

- LEXICON Nm3-3a 
- Nm3a-SINGULAR; 
- +Noun+Masc+Com:^C PL-AÍ; 

Strong Plurals : +anna
eg. an bláth -> na bláthanna

- LEXICON Nm3-4a 

^Lea,broadening, is required, in gen sg: io -> ea (bior, crios) 
and this is done using ^Ath (change)
pl bior -> bioranna

- Nm3a-SINGULAR; 
- +Noun+Masc+Com:^C PL-(E)ANNA; 

#### Strong Plurals : Athrú +anna (io->ea)
eg. an cith -> na ceathanna
- LEXICON Nm3-4 
- Nm3a-SINGULAR; 
^Lea,broadening, is required, in gen sg: cith -> ceatha, greim -> greama
and this is done using ^Ath (change)
pl also broadened cith -> ceathanna
- +Noun+Masc+Com:^C^Ath^Lea PL-(E)ANNA; 

- LEXICON Nm3-5 
- Nm3-SINGULAR; 
- +Noun+Masc+Com:^C PL-(E)ACHA; 

- LEXICON Nm3-6 
- Nm3-SINGULAR; 
- +Noun+Masc+Com:^C PL-(LEA)A; 

- LEXICON Nm3-7 
- Nm3-SINGULAR; 
- +Noun+Masc+Com:^C PL-TA; 

- LEXICON Nm3-8 
- Nm3a-SINGULAR; 
- +Noun+Masc+Com:^C PL-(LEA)A; 

- LEXICON Nm3-8a  sliocht - sleachta gs & pl
- Nm3a-SINGULAR; 
- +Noun+Masc+Com:^C^Ath PL-(LEA)A; 

Strong Plurals : +í

(A) nouns ending in -ín (a diminutive)
smidiríní (smithereens) no singular
eg. an cailín -> na cailíní (girls)
eg. an báidín -> na báidíní (small boats)

(B) nouns ending in -a
eg. an balla -> na ballaí (walls)

- LEXICON Nm4-SINGULAR 
- +Noun+Masc+Com:^M^C Nom-sg; 

- LEXICON Nm4-1 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-Í; 

- LEXICON Nm4-2 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C^Ath PL-Í; 

- LEXICON Nm4-3 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C^Ath PL-TE; 

- LEXICON Nm4-4 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C^Ath PL-THE; 

- LEXICON Nm4-5 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-(E)ACHA; 

- LEXICON Nm4-6 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-NNA; 

- LEXICON Nm4-7 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-(E)ANNA; 

- LEXICON Nm4-8 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-ITE; 

- LEXICON Nm4-9 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-ONNA; 

- LEXICON Nm4-10 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-OCHA; 

- LEXICON Nm4-11 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-(LEA)THA; 

01/04/08
- LEXICON Nm4-12 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-AÍ; 

- LEXICON Nm4-13 
- Nm4-SINGULAR; 
- +Noun+Masc+Com:^C PL-THANNA; 

Strong Plurals : +idí
an fiche -> na fichidí (the twenties) eidí needs correcting
an caoga -> na caogaidí (the fifties)
- LEXICON Nm5-1 
- +Noun+Masc+Com:^M^C Nom-sg;  
- +Noun+Masc+Com:^C PL-IDÍ; 

- LEXICON Nm5-2 
- +Noun+Masc+Com:^M^C Nom-sg;  

- LEXICON Nm5-3 
- +Noun+Masc+Com:^M^C Nom-sg;  

GS +the
- LEXICON Nm5-4 
- +Noun+Masc+Com:^M^C Nom-sg; 

GS +te
- LEXICON Nm5-5-SINGULAR 
- +Noun+Masc+Com:^M^C Nom-sg; 

- LEXICON Nm5-5  PL +TÍ 
- Nm5-5-SINGULAR; 
- +Noun+Masc+Com:^C^Atht PL-Í; 

GS +tha
PL +thaí
bascadh - basctha - bascthaí
- LEXICON Nm5-6 

GS +ta
- LEXICON Nm5-7-SINGULAR 
- +Noun+Masc+Com:^M^C Nom-sg; 

- LEXICON Nm5-7 
- Nm5-7-SINGULAR; 

moladh / gs = molta / pl = moltaí
- LEXICON Nm5-7a 
- Nm5-7-SINGULAR; 

- LEXICON Ns 
- +Subst+Noun+Sg:0 NounSéUrú; 

- LEXICON Nspl 
- +Subst+Noun+Pl:0 NounSéUrú; 

### INITIAL MUTATIONS
#### NOMINATIVE SINGULAR 
- LEXICON Nom-sg-initial 
- NounSéUrú; 
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

- LEXICON NounSéUrú 
- Emphasis; 
- +Ecl:^IM^Urú Emphasis; 
adds ^h to vowel-initial words ...  but adds the +hPref to all words ... see fix file

- LEXICON Emphasis 
- #; 
- +Emph:s^Emph #;   NEEDS 1PL NE/NA & 3PL SEAN/SAN ALSO

#### GENITIVE SINGULAR 

- LEXICON Gen-sg-initial 
#### VOCATIVE SINGULAR 
Since this is trivial (always ^Sé) it is included with Final Mutations
in Voc-sg-0 and Voc-sg-1.

#### ALL PLURALS
Note: Vocative Plural does not require Def & Idf but it is easier to generate 
them and remove all Voc Pl Idfs at the end (the Def form is correct 
although the Def marker is unnecessary)

- LEXICON Pl-initial 

### FINAL MUTATIONS
#### NOMINATIVE SINGULAR
- LEXICON Nom-sg 
- +Sg:0 Nom-sg-initial; 

#### GENITIVE SINGULAR 

- LEXICON Gen-sg-D1  1st. Declension - Caolú (Slenderise)
- +Sg:^Caol Gen-sg-initial; 

- LEXICON Gen-sg-D2  2nd. Declension - Caolú (Slenderise) and

- LEXICON Gen-sg-D2a  2nd. Declension - each -> í, ach -> aí 

- LEXICON Gen-sg-D3  3rd. Declension -  Broaden (Leathnú) and

- LEXICON Gen-sg-D4  4th. Declension - No change

- LEXICON Gen-sg-D5-1  5th. Declension - (Broaden) + ach
- LEXICON Gen-sg-D5-2  5th. Declension - Sync + (e)ach
- LEXICON Gen-sg-D5-2a  5th. Declension - Sync + a
- LEXICON Gen-sg-D5-2b  5th. Declension - Sync + Slen + e
- LEXICON Gen-sg-D5-3  5th. Declension - Add "n"
- LEXICON Gen-sg-D5-4  5th. Declension - Add "d"
- LEXICON Gen-sg-D5-5  5th. Declension -  Broaden (Leathnú)
- LEXICON Gen-sg-D5-6  5th. Declension -  Change + ithe
- LEXICON Gen-sg-D5-7  5th. Declension -  Change + Slen + the
- LEXICON Gen-sg-D5-8  5th. Declension -  Change + Slen + te

#### VOCATIVE SINGULAR 

- LEXICON Voc-sg-0 
- +Sg+Len:^Sé #;  eg. a rún, a phobal

- LEXICON Voc-sg-1 

#### ALL PLURALS

- LEXICON PL-TADA  NO CHANGE (LIT. NOTHING)

- LEXICON PL-CAOLÚ  CAOLÚ (SLENDERISE)

- LEXICON PL-LEATHNÚ  LEATHNÚ (BROADEN)

- LEXICON PL-(LEA)A  ADD "A" & LEATHNÚ (BROADEN) IF SLENDER

- LEXICON PL-TA  ADD "TA"

- LEXICON PL-(LEA)THA  ADD "THA" & LEATHNÚ IF SLENDER

- LEXICON PL-(E)ANNA  ADD "ANNA" IF BROAD & ADD "EANNA" IF SLENDER

- LEXICON PL-Í  ADD "Í"

- LEXICON PL-TÍ  ADD "TÍ"

- LEXICON PL-(CAOL)E  ADD "E" & CAOLÚ IF BROAD

- LEXICON PL-(CAOL)EACHA  ADD "EACHA" & CAOLÚ

- LEXICON PL-(LEA)ACHA  ADD "ACHA" & LEATHNÚ

- LEXICON PL-(E)ACHA  ADD "ACHA" IF BROAD & ADD "EACHA" IF SLENDER

- LEXICON PL-THANNA  ADD "THANNA"

- LEXICON PL-TE  ADD "TE"

- LEXICON PL-AÍ  ADD "AÍ"

- LEXICON PL-NNA  ADD "NNA"

- LEXICON PL-THE  ADD "THE"

- LEXICON PL-NA  ADD "NA"

- LEXICON PL-IDÍ  ADD "IDÍ"

- LEXICON PL-ATHRÚ  ATHRÚ (CHANGE LAST SYLLABLE)

- LEXICON PL-(E)ANTA  ADD "ANTA" IF BROAD & ADD "EANTA" IF SLENDER

- LEXICON PL-ITE  ADD "ITE"

- LEXICON PL-ONNA  ADD "ONNA"

- LEXICON PL-OCHA  ADD "OCHA"

E. Uí Dhonnchadha 
ADDED THE +SG TAG 20/2/2004
ADDED NP-Fam Aug 2004

- LEXICON NP-PLACE 

- LEXICON NP-PLACE-EN 

- LEXICON NP-PLACE-sg 

- LEXICON NP-PLACE-fem 

- LEXICON NP-PLACE-pl 

- LEXICON NP-FAM-EN 

- LEXICON NP-PERS-EN-fem 

- LEXICON NP-PERS-EN 

- LEXICON NP-Fam 

- LEXICON NP-Fam-0 

- LEXICON NP-Fam-V 

- LEXICON NP-Fam-chg 

when it is a place name
as well as the usual inflections for propernouns  (4 classes)
we want to generate an adjectival form e.g. Beilg - Beilgeach

new 5-6-2024
Place and Personal name files both use Nf1-Prop and Nm1-Prop etc.

- LEXICON Nf2-Prop-Place 

- LEXICON Nf3-Prop-Place 

- LEXICON Nf4-Prop-Place 

- LEXICON Nf5-Prop-Place 

- LEXICON Nm1-Prop-Place 

- LEXICON Nm4-Prop-Place 

- LEXICON Nm1-Prop-PName 

- LEXICON Nm3-Prop-PName 

- LEXICON Nm4-Prop-PName 

- LEXICON Nf2-Prop-PName 

- LEXICON Nf3-Prop-PName 

- LEXICON Nf4-Prop-PName 

masc nouns - slenderise
- LEXICON Nm1-Prop 

fem nouns - slenderise and add e
- LEXICON Nf2-Prop 

fem nouns - broaden and add a
- LEXICON Nf3-Prop 

fem nouns - no change

masc nouns - no change

fem nouns - Albain/na hAlban

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/nouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/nouns.lexc)</small>

---

## src-fst-morphology-affixes-prefixes.lexc.md 

## Prefixes
Prefixes in the Irish language are bound to beginning of other words.

- LEXICON Prefixes 
- nounprefix- Nouns ; 
- verbprefix- Verbs ; 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/prefixes.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/prefixes.lexc)</small>

---

## src-fst-morphology-affixes-propernouns.lexc.md 

## Proper noun inflection
The Irish language proper nouns inflect in the same cases as regular
nouns, but with a colon (':') as separator.

- LEXICON ProperNounCases 
- +N+Prop:%: Cases ; 
- - Nouns ; 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/propernouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/propernouns.lexc)</small>

---

## src-fst-morphology-affixes-symbols.lexc.md 

## Symbol affixes

## Symbol affixes

- LEXICON Noun_symbols_possibly_inflected 
+N+Symbol: SYMBOL_connector ; 

- LEXICON Noun_symbols_never_inflected 
- +N+Symbol: # ; 

- LEXICON SYMBOL_connector 

- LEXICON SYMBOL_NO_suff 
- +Sg+Nom: # ; 

- LEXICON SYMBOL_suff 
- # ; todo

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/symbols.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/symbols.lexc)</small>

---

## src-fst-morphology-affixes-verbs.lexc.md 

## Verb morphology

- LEXICON V1-SL =  1st. Conjugation - slender

- +PastInd+1P+Sg:^Verbis NegQPast; = variation shílis as well as shíleas

- LEXICON V1-BR = 1st. Conjugation - broad

- LEXICON V1b-PresInd = Present Tense - Aimsir Láithreach
- +Auto:tar NegQ; = +Auto = Autonomous - saor briathar

- LEXICON V1b-PastInd = Past Tense - Aimsir Chaite
- +1P+Sg:as NegQPast; = 14 Feb

- LEXICON V1b-FutInd = Future Tense - Aimsir Fháistineach
- +1P+Sg:fad NegQ; = 14 Feb

- LEXICON V1b-PastImp = Imperfect  - Aimsir Ghnáthchaite ( past hab.)

- LEXICON V1b-Cond = Conditional Mood - Modh Coinníollach

- +CM:fadh #; = munster variation

- LEXICON V1b-PresSubj = Present Subj. Mood - Modh Foshuiteach Láith.

- LEXICON V1b-Imper = Imperative Mood - Modh Ordaitheach

- LEXICON V1-BR-LV = 1st. Conjugation - ! Broad F Slender T 

- LEXICON V1xa-PresInd = Present Tense - Aimsir Láithreach
- +Auto:itear NegQ; = +Auto = Autonomous - saor briathar

- LEXICON V1xa-PastInd = Past Tense - Aimsir Chaite

- +1P+Sg:s NegQPast; = 14 Feb

- LEXICON V1xa-FutInd = Future Tense - Aimsir Fháistineach

- LEXICON V1xa-PastImp = Imperfect  - Aimsir Ghnáthchaite ( past hab.)

- LEXICON V1xa-Cond = Conditional Mood - Modh Coinníollach

- LEXICON V1xa-PresSubj = Present Subj. Mood - Modh Foshuiteach Láith.

- LEXICON V1xa-Imper = Imperative Mood - Modh Ordaitheach

- LEXICON V1-SL-LV = 1st. Conjugation - ! Slender F Slender T 

- LEXICON V1xb-PresInd = Present Tense - Aimsir Láithreach

- LEXICON V1xb-PastInd = Past Tense - Aimsir Chaite

- LEXICON V1xb-FutInd = Future Tense - Aimsir Fháistineach
- +1P+Sg:ifad NegQ; = ?????  14 Feb

- LEXICON V1xb-PastImp = Imperfect  - Aimsir Ghnáthchaite ( past hab.)

- LEXICON V1xb-Cond = Conditional Mood - Modh Coinníollach

- LEXICON V1xb-PresSubj = Present Subj. Mood - Modh Foshuiteach Láith.

- LEXICON V1xb-Imper = Imperative Mood - Modh Ordaitheach

- LEXICON V1-SV = 1st. Conjugation - ! Slender F Slender T 

- LEXICON V1xc-PresInd = Present Tense - Aimsir Láithreach

- LEXICON V1xc-PastInd = Past Tense - Aimsir Chaite
- +1P+Sg:^igh^Verbíos NegQPast; = 14 Feb

- LEXICON V1xc-FutInd = Future Tense - Aimsir Fháistineach
- +1P+Sg:íos NegQ; = 14 Feb

- LEXICON V1xc-PastImp = Imperfect  - Aimsir Ghnáthchaite ( past hab.)

- LEXICON V1xc-Cond = Conditional Mood - Modh Coinníollach
- +CM:ífeadh #; = munster variation

- LEXICON V1xc-PresSubj = Present Subj. Mood - Modh Foshuiteach Láith.

- LEXICON V1xc-Imper = Imperative Mood - Modh Ordaitheach

- LEXICON V1-SL-X = 1st. Conjugation - slender becomes broad

- LEXICON V1-SL-BR-sync = 1st. Conjugation - slender is sync. and becomes broad

- LEXICON V1-SL-BR = 1st. Conjugation - slender becomes broad

- LEXICON V1xd-Imper = Imperative Mood - Modh Ordaitheach

- LEXICON V1xd-PastInd = Past Tense - Aimsir Chaite
- +1P+Sg:^Verbeas NegQPast; = 14 Feb

- LEXICON V1-SL-LC = 1st. Conjugation - slender becomes broad except where

- LEXICON V2-BR = 2nd. Conjugation - broad

- LEXICON V2-SL = 2nd. Conjugation - slender

- LEXICON V2-BR-sync = 2nd. Conjugation - broad - syncopated

- LEXICON V2-SL-sync = 2nd. Conjugation - slender - syncopated

- LEXICON V2-BR-0 = 2nd. Conjugation - broad

- LEXICON V2-BR-PresInd = Present Tense - Aimsir Láithreach
- +Auto:aítear NegQ; = +Auto = Autonomous - saor briathar

- LEXICON V2-BR-PastInd = Past Tense - Aimsir Chaite

- +1P+Sg:aíos NegQPast; = 14 Feb

- LEXICON V2-BR-FutInd = Future Tense - Aimsir Fháistineach
- +1P+Sg:aíos NegQ; = 14 Feb
- +Rel:ós^Sé #; = a chosnós

- LEXICON V2-BR-PastImp = Imperfect  - Aimsir Ghnáthchaite ( past hab.)

- LEXICON V2-BR-Cond = Conditional Mood - Modh Coinníollach

- LEXICON V2-BR-PresSubj = Present Subj. Mood - Modh Foshuiteach Láith.

- LEXICON V2-BR-Imper = Imperative Mood - Modh Ordaitheach

inserted +Len +Uru to distinguish between a bhíonn & a mbíonn Dir/Indir
Rel clauses Dec 2004

- LEXICON NegQ 

- LEXICON NegQPast 

- LEXICON NegQSaor 

- LEXICON NegQLen 

- LEXICON NegImper 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/verbs.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/affixes/verbs.lexc)</small>

---

## src-fst-morphology-phonology.init.xfscript.md 

## Noun (Gaeilge) Replace Rules
### INITIAL MUTATIONS
Elaine Uí Dhonnchadha
12/12/96 - continued March 1998
and January 2001
- ^Sé : (Séimhiú) Lenition : insert "h" after certain initial consonants
- ^Urú : Eclipsis
- ^tv & ^hv : Prefix "t-" or "h" to words with an initial vowel
- ^ts : prefix "t" to words starting with "s" followed by "l", "n", "r" or a vowel
- ^Poss : possessive m', d' etc on nouns
Oct 2003
INITIAL MUTATION OF 2nd. PART OF COMPOUND
#### DEFINITIONS
- define VowelAll a|e|i|o|u|á|é|í|ó|ú|%^AO|%^IA|%^AE|%^UA|A|E|I|O|U|Á|É|Í|Ó|Ú ; 
- define VowelLC a|e|i|o|u|á|é|í|ó|ú|%^AO|%^IA|%^AE|%^UA ; 
- define VowelUC A|E|I|O|U|Á|É|Í|Ó|Ú ; 
- define Len b|c|d|f|g|m|p|t|B|C|D|F|G|M|P|T ; 
- define SLen S|s ; 
- define SWord l|n|r ; 

#### Rules
- read regex [..] -> h || %^CB [m|b|c|d|f|g|p|t] _ 
- [..] -> h || %^CB s _ [VowelLC|l|n|r] 
- [..] -> %^FH h || .#. Len _ ?+ [[%^F %^C]|[%^M %^G]|[%^M %^V]|[%^F %^V]|[%^IM]|[%^Adj]|[%^Verb]|[%^VN]] ?* %^Sé 
- ,, 
- [..] -> %^FH h || .#. [S|s] _ [l|n|r] VowelLC ?+ 
- [[%^F %^C] 
- |[%^M %^G] 
- |[%^F %^V] 
- |[%^M %^V] 
- |[%^IM] 
- |[%^Adj] 
- |[%^Verb] 
- |[%^VN]] 
- ?* %^Sé 
- ,, 
- [..] -> %^FH h || .#. [S|s] _ VowelLC ?* [[%^F %^C]|[%^M %^G]|[%^F %^V]|[%^M %^V]|[%^IM]|[%^Adj]|[%^Verb]|[%^VN]] ?* %^Sé 

- h -> [] || [d|n|t|l|s] ([%-|%_]) %^CB [d|n|t|l|s] _ 

- %^Sé -> [] 
- %^Do -> [] 
- %^VN -> []  used for séimhiú on f without d' e.g. a fheiceáil not a d'fheiceáil

- b -> %^FU m b ,  consonants
- B -> %^FU m B ,  consonants
- c -> %^FU g c , 
- C -> %^FU g C , 
- d -> %^FU n d , 
- D -> %^FU n D , 
- f -> %^FU b h f , 
- F -> %^FU b h F , 
- g -> %^FU n g , 
- G -> %^FU n G , 
- p -> %^FU b p , 
- P -> %^FU b P , 
- T -> %^FU d T , 
- t -> %^FU d t || .#. _ ?+ [[%^G]| [[%^M | %^F] %^C]|[%^Verb]|[%^Adj]|[%^IM]] ?* %^Urú  Gen Pl & comp prep.
- [..] -> %^FU n %- || .#. (%^X) _ VowelAll ?* [[%^G]| [[%^M | %^F] %^C]|[%^Verb]|[%^IM]] ?* %^Urú  Gen Pl only

- [%^Urú -> []] 

#### VOWEL PREFIXING t-, h, ts
- [..] -> %^FV t %- || .#. (%^X) _ VowelLC ?* %^M %^C ?* %^tv 
- [..] -> %^FV t || .#. (%^X) _ VowelUC ?* %^M %^C ?* %^tv 
- [%^tv -> []] 

- [..] -> %^FV h || .#. (%^X) _ VowelAll ?* [[%^F %^G] | [%^C]|[%^Verb]|%^IM] ?* %^hv 
- [%^hv -> []] 

- s -> %^FU t s || .#. _ (%^FH) [VowelAll|l|n|r|h] ?* [[%^F %^C]|[%^M %^G]] ?* %^ts 

- S -> %^FU t S || .#. _ (%^FH) [VowelAll|l|n|r|h] ?* [[%^F %^C]|[%^M %^G]] ?* %^ts 

- %^FH h -> [] || .#. %^FU t [s|S] _ 

- %^ts -> [] 

#### POSSESSIVE PREFIX 

the following are performed in parallel as we want all forms

- [..] -> %^FV h || .#. _ VowelAll ?+ %^Poss  a hathair - her father
- [..] -> %^FV n %- || .#. _ VowelAll ?+ %^Poss  n-athair - our/your/their
- %^Poss -> [] 

- %^IM -> []  initial mutations caused by compound prepp, possessives etc.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.init.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.init.xfscript)</small>

---

## src-fst-morphology-phonology.nounadj.xfscript.md 

## Noun (Gaeilge) Replace Rules
Elaine Uí Dhonnchadha
12/12/96 - continued March 1998
### INTRO
Certain vowel combinations will be represented by one symbol as these vowel
sounds should be treated as a unit.
#### DIPHTHONG EXAMPLE
For example in slenderising "ua" we want "uai" not "uiai".
Diphthongs 
#### LONG VOWEL EXAMPLE
In cathair (city) the "ai" is syncopated but in cathaoir (chair) "aoi" is not.
There are two other diphthongs in Irish but the are not explicitly represented
orthographically (radharc, etc see Fpóca)
#### Long Vowels
### Rules 
#### Definitions
- define Vowel a|e|i|o|u|á|é|í|ó|ú|%^AO|%^IA|%^AE|%^UA ; 
- define Nountag %^F|%^M|%^C|%^G|%^V ; 
- define Cons b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z|%^FC|%^FY|%^FS|%^FB ; 

Regex
- read regex [ a e -> %^AE ]  Long vowel symbol

- [ a o -> %^AO ]  Long vowel symbol

- [ u a -> %^UA ]  Diphthong symbol

- [e a n n] -> [%^FY n e] || Cons _ [Nountag+ |%^Adj] %^Coim 

- [e a l l] -> [%^FY l e], 
- [a l l] -> [%^FY l e] || Cons _ [Nountag+ |%^Adj] %^Coim 

- [a i l l] -> [%^FY l a] || Cons _ [Nountag+ |%^Adj] %^Coim 

- [a|e|i|o|u] -> [%^FY] || Cons (a|e) _ ?^<3 [Nountag+ |%^Adj] %^Coim 
- %^Coim -> [] 

- %^M -> [] 
- %^F -> [] 
- %^C -> [] 
- %^G -> [] 
- %^V -> [] 
- %^Adj -> [] 

- é -> %^FC é i || _ %^Ath  finné -> finnéi+the
- í -> %^FC i || _ %^Ath t  ainmhí -> ainmhi+the
-   NOTE must fire before ch->í rule as we
-   don't want the new í being turned into i
- i ú -> %^FC i || _ %^Ath t  deimhniú -> deimhni+the (pl)

- ú -> %^FC u i || _ %^Ath t  tarlú -> tarlui+the (pl)

- i ú -> [%^FC ] || _ %^Ath i  deimhniú -> deimhn+ithe (gen sg)

- ú -> [%^FC a] || _ %^Ath i  tarlú -> tarla+ithe (gen sg)

- a í -> [%^FC ] || _ %^Ath a  cónaí -> cón+aithe (gen sg)

- d l %^X a d h -> [%^FC d l a] || _ %^Ath (%^Caol) t  codladh -> codlata

- t h %^X a d h -> [%^FC ] || _ %^Ath (%^Caol) t  leathadh -> leata

- t h %^X a d h -> [%^FC ] || _ %^Ath (%^Caol) t  leathadh -> leata

- t e %^X a d h -> [%^FC ] || _ %^Ath (%^Caol) t 

- t %^X a d h -> [%^FC ] || _ %^Ath (%^Caol) t 

- e a d h -> [%^FC ] || %^X _ %^Ath (%^Caol) t 

- g t -> [%^FC g] || _ %^Ath (%^Caol) t  tarrXaingt -> tarrXaingthe

- a d h -> [%^FC ] || %^X _ %^Ath (%^Caol) t 

end new

Nouns :final syllable "ach"  and "adh" become "aí" , eg bealach 
"each" and "eadh" become "í"
stems must be polysyllabic e.g. not beach, sceach etc (teach is an exception)
Adj Like Nouns :final syllable "ach"  (no "adh"?) become "aí" , eg déanach  - déanaí

- c h -> %^FC í ,  bealach -> bealaí, soitheach -> soithí
-   margadh -> margaí, geimhreadh -> geimhrí
- d h -> %^FC í || Vowel+ Cons+ %^X (e) a _ %^Ath (%^Caol) (t)  added \t 31/08/06
- e a -> [] || _ %^FC í %^Ath  correction : geimhrea^FCí->geimhr^FCí, 
-   soitheaí->soithí
-   Adj: leochaileaí -> leochailí
- b h -> %^FC a í || _ %^Ath  leanbh -> leanaí

- d h -> %^FC t || i _ %^Ath %^Lea  iarraidh(aí) -> iarrait(aí)

- t -> [%^FC ] || n _ %^Ath  tiomáint -> tiomána  ( was t->a but D3 appenda a)

- t -> %^FC t h || r _ %^Ath  tagairt -> tagartha, buairt -> buartha

- e -> [%^FC ] || _ %^Ath  "e" is removed and "í" or "te" is appended
-   buille -> buillí, císte -> cístí
-   míle -> mílte, sloinne -> sloinnte
- i o -> %^FC e a || _ [c|n|s|r] (h t) %^Ath  sioc(m) -> seaca, 
-   briocht -> breachta 
-   smior(m) -> smeara
-   fios(m) -> feasa, crios(m) -> creasa
-   cion(m) -> ceana
-   gion(m) -> geana

- o c h -> [%^FC ] || %^X (?) í _ %^Ath  buíoch -> buí +thí

- c h -> [%^FC ] || %^X [á|ó|o|%^UA] _ %^Ath  sách,sóch,gleoch,díomuach (^UA=ua)

- [ %^Caol -> [] || [i|í] Cons* _  search to check if 
-   the last vowel is an "i" or "í" 

- %^Lea -> [] || [a|o|u|á|ó|ú|%^UA|%^AO|%^AE|%^IA] Cons* _ 
-   check that the last vowel is NOT an "i" or "í" 
-   U=ua O=ao E=ae (I=ia included though not in use)

- c h -> %^FC g h || Vowel+ Cons+ %^X (e) a _ %^Caol 

- c h -> %^FC g h || Vowel+ Cons+ %^X í o _ %^Caol 

- c h -> %^FC g h || d ú _ %^Caol 

- a -> %^FS i || %^X [e|u] _ [[c (h)] cuach - cuiche, 
- |[b (h)] dealbh - deilbhe
- |[d (h)] nead - neide, fleadh - fleidhe
- |[l b h] dealbh - deilbhe
- |[n g] reang - reinge
- |[r c] searc - seirce, leac - leice
- |[r g] fearg - feirge
- |[t h] leath - leithe
- |[s] greas - greise
- |[m (h)] neamh - neimhe (added '(h)') - CW 09/08
- ] %^Caol e 

- e a -> %^FS i || Cons+ %^X _ Cons+ %^Caol 

- a -> %^FS i || %^X é _ Cons+ %^Caol 

- [..] -> %^FS i || %^X (e) [%^AO|a|á|o|ó|u|ú|%^UA] _ Cons+ %^Caol 

- [..] -> %^FS i || %^X (i) ú _ Cons+ %^Caol 
- o -> [%^FS ] || %^X (a|u) [i|í] _ Cons+ %^Caol 

- u -> [%^FS ] || %^X [i|í] _ Cons+ %^Caol 
- i a -> %^FS é i || %^X (h) _ Cons+ %^Caol (t) e 
- [..] -> %^FS i || %^X i a _ Cons+ %^Caol .#. 

- i a -> %^FS e a || %^X _ Cons+ %^Caol a 

- %^Caol -> [] 

May 1998
Leathú (^Lea) :Broadening of slender words
Usually by removing "i"
but also by substituting vowels eg io->ea
and also by inserting a broad vowel eg í->ío
included %^FH in i -> ea rule

- o i -> %^FB a || r _ Cons+ %^Lea  roinn -> rann 

- i -> %^FB a || [e|é] _ Cons+ %^Lea  greim(m) -> greama, spéir -> spéartha

- i -> %^FB e a || [b|c|m|r] (%^FH h) %^X _ Cons+ %^Lea 
-   binn -> beanna, rith -> reatha
-   cith(m) -> ceatha, crith(m) -> creatha
-   scian -> sceana (I) imirt -> imeartha

- i -> [%^FB] || [a|á|%^AE|o|ó|ú|%^UA|%^AO] _ Cons+ %^Lea 
-   CHECK WHETHER "u" SHOULD BE HERE TOO???
-   OR DOES "ui" ALWAYS GO TO "o" (see next rule)
-   it appears so ...
-   súil - súl, dúil, glúin
-   cóir - córa, móin - móna
-   deoir - deora, feoil - feola
-   troid - troda, cainteoir - cainteora
-   droim(m) - droma, goin - gona, toil
-   gáir - gártha, tiomáint - tiomána
-   síocháin - síochána, cáisc - cásca
-   stair - startha, flaith(m) - flatha
-   bliain - bliana
-   grósaeir - grósaera (E), traein - traen(E)
-   bádóir - bádóra, buairt(U) -> buartha
-   aoir - aortha (O)

- u i -> %^FB o || _ Cons+ %^Lea  cuid -  na coda, fuil - fola

- [..] -> %^FB o || (a) í _ Cons+ %^Lea 
-   feadaíl - feadaíola, tír - tíortha
- %^Lea -> [] 

Vowel Harmony of Broad and Slender Vowels: 
Endings (which are appended to the root) must be broad or slender to agree with root 
NB: this must be tested after ^Coim, ^Caol or ^Lea tags have been applied
Examples 
- (1) (e)acha	: neadacha (nests), stoirmeacha (storms)
- (2) (e)anna	: carranna (cars),  áiteanna (places)
The broad ending "acha" or "anna" will be applied as standard. If the root
is now found to be slender an "e" will be inserted
- %^X -> []  no longer required and it would 
-   get in the way of the next rule

- [ %^VH -> e || [i|í] Cons* _ ]  check if the last vowel before the %^VH
-   is slender (ie an "i" or "í" )
- [ a -> [] || a %^VH _ ]  remove extre "a" in  Havana^VHach

- %^VH -> [] 

- [..] -> e || [e|é|i|í|%^AE] Cons* s _ %^Emph 

- [..] -> a || [a|á|o|ó|u|ú|%^UA|%^IA|%^AO] Cons* s _ %^Emph 

- [..] -> %- || s _ s (a|e) %^Emph 

- %^Emph -> [] 

- [ %^AE -> a e] 
- [ %^AO -> a o] 
- [ %^UA -> u a] 
- [%^F -> []] 
- [%^M -> []] 
- [%^N -> []] 
- [%^G -> []] 
- [%^V -> []] 
- [%^CB -> []] 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.nounadj.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.nounadj.xfscript)</small>

---

## src-fst-morphology-phonology.tidy.xfscript.md 

## Gaeilge: Replace Rules
Elaine Uí Dhonnchadha
May 2001
Apr 2004
### Last Part - tidy up
- read regex [ %^AE -> a e] 
- [ %^AO -> a o] 
- [ %^UA -> u a] 
- [%^F -> []] 
- [%^M -> []] 
- [%^N -> []] 
- [%^G -> []] 
- [%^V -> []] 
- [%^CB -> []] 
- [%^FB -> []]  broadened
- [%^FC -> []]  last syllable changed
- [%^FH -> []]  séimhiú i.e. h inserted
- [%^FU -> []]  urú
- [%^FV -> []]  prefing of vowel-initial words
- [%^FS -> []]  slenderised
- [%^FY -> []]  syncopated
- [%^FT -> []]  verb stem truncated
- [%^CB -> []]  compound boundary e.g. from pref + verb/adj scripts

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.tidy.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.tidy.xfscript)</small>

---

## src-fst-morphology-phonology.verb.xfscript.md 

## Verb (Gaeilge) Replace Rules
Elaine Uí Dhonnchadha
(c) 2001 - NEW
2005 - new vn/va triggers
### PastInd & Imper use stem
- regex [i g h -> [%^FT] || _ (%^Caol) %^igh ?* %^Verb [[%^Fr]|.#.]] 
- [%^igh ->[]] 
- [a i g h -> [%^FT] || _ %^aigh ?* %^Verb [%^Fr]] 
- [%^aigh ->[]] 
Verbal Noun Gen
- [á i l t e -> %^FT á l a || _ %^áil %^Verb ] 
- [%^áil ->[]] 
- [t h -> [%^FT] || _ %^th %^Verb ] 
- [%^th ->[]] 
- [b h -> [%^FT] , 
- g h -> [%^FT] , 
- m h -> [%^FT] || _ %^bgmh %^Verb ] 
- [%^bgmh ->[]] 

### 2nd. Conjugation Syncopation of Stem

- [a i l -> %^FY l || _ %^Coim %^Verb [%^Fr]] 
- [a i n -> %^FY n || _ %^Coim %^Verb [%^Fr]] 
- [a i r -> %^FY r || _ %^Coim %^Verb [%^Fr]] 
- [a i s -> %^FY s || _ %^Coim %^Verb [%^Fr]] 
- [i l -> %^FY l || _ %^Caol %^Coim %^Verb [%^Fr]] 
- [i n -> %^FY n || _ %^Caol %^Coim %^Verb [%^Fr]] 
- [i r -> %^FY r || _ %^Caol %^Coim %^Verb [%^Fr]] 
- [i s -> %^FY s || _ %^Caol %^Coim %^Verb [%^Fr]] 
- [%^Coim ->[]] 
- [%^Fr ->[]] 

### 1st Conjugation Slender Stems => broaden stems; leave slender for t endings

- [%^LC -> %^Caol || _ %^Verb [t|.#.]] 
- [i -> [%^FB ] || ?+ _ ? %^LC %^Verb] 
- [%^LC -> 0 ] 

### 1st Conjugation Slender Stems => slenderise endings ! order is important

- [a i -> %^FS i || %^Caol %^Verb [f|t]* _ ?+] 
- [a í -> %^FS í || %^Caol %^Verb [f|t]* _ ?* .#.] 
- [a -> %^FS e || %^Caol %^Verb [f|t]* _ .#.] 
- [á -> %^FS e á || %^Caol %^Verb [f|t]* _ .#.] 
- [a -> %^FS e a || %^Caol %^Verb [f|t]* _ ?+]  f/t - to prevent  amar - eamear
- [ó -> %^FS e o || %^Caol %^Verb [f|t]* _ ?+] 
- [%^Caol -> []] 

### 1st Conjugation Slender Stems => broaden root eg sábháil

- [i -> [%^FB ] || _ ? %^Lea] 
- [%^Lea -> []] 
- [%^Verb -> []] 

- [%^VAdj -> [] ] TEMPORARY - VERBAL ADJS. AND VERBAL NOUNS
IN 2 MUST BE SORTED OUT

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

## Abbreviations 

**LEXICON Abbrev**

Dochtúir+Abr+Sem/Title:Dr. #;
Miss+Abr+Sem/Title:Ms. #;

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/abbreviations.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/abbreviations.lexc)</small>

---

## src-fst-morphology-stems-adjectives.lexc.md 

## Na hAidiactaí Tuairisciúla - Descriptive Adjectives
(c)2001
(1) New Irish Grammar by The Christian Brothers  
(2) Réchúrsa Gramadaí, Brian Mac Giolla Phádraig
(3) Graméir Gaeilge na mBráithre Críostaí
(4) Nuachúrsa Gaeilge na mBráithre Críostaí
(5) A Handbook of Irish Vol 2.An Outline of Modern Irish Grammar,
Alfred Bammesberger
(6) Ó Dónaill Irish-English Dictionary
(7) Gléacht - Ó Dónaill Online Dictionary 
Descriptive adjectives can be used in two ways (REF P59 NIG)
a) predicatively - quailifies a noun/pronoun *indirectly* as a predicate 
or part of a predicate
E.G. Is BREÁ an lá é (It is a LOVELY day, lit. it is lovely that the day is (approx!)
E.G. Tá mé TUIRSEACH (I am TIRED)
E.G. Tá sé FUAR (It is COLD)
E.G. Tá an fhuinneog GLAN (The window is CLEAN) !    Used in this way the base form IS NOT INFLECTED to agree with case/number/gender
of the noun - except in a few cases ... see p 59 s4 NIG
The base form (positive degree) is used
b) attributively - qualifies a noun *directly*
E.G. Tá an páiste ÓG ar scoil (The YOUNG child is a at school
E.G. Níl pingin RUA agam (I haven't a RED penny)
E.G. Chonaic mé an fhuinneog GHLAN (I saw the CLEAN window)
Used in this form the adjective IS INFLECTED to agree with case/number/gender of the noun
The adjective usually follows the noun though some forms can be prefixed
to the noun e.g. SEANfhear (old man) LAGmhisneach ((in) low spirits),
ARDeagalis (cathedral - lit. high church) 
					L E X I C O N
**LEXICON AdjA**

SEE PREP/NUM etc dá	Adj3-1;	 ! do or de +

I R R E G U L A R   A D J E C T I V E S 

the following always come at the end of the noun/pron/adj and cannot 
be intermingled with other adjectives 
Have moved to Demonstrative Determiners 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adjectives.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/adjectives.lexc)</small>

---

## src-fst-morphology-stems-adpositions.lexc.md 

## Prepositions: 
Simple: le, ag, ar, etc.
Compound (Na Forainmneacha Réamhfhoclacha) Prepositional Pronouns (agam, agat...)
Emphatic Compound eg agamsa, uaimse, ...
E. Uí Dhonnchadha

- (1) New Irish Grammar by The Christian Brothers  
- (2) Gramadach na Gaeilge agus Litríocht na Gaeilge - An Caighdeán Oifigiúil
- (3) Foclóir Póca - An Gúm
- (4) Nuachúrsa Gaeilge na mBráithre Críostaí
- (5) Ó Dónaill Irish-English Dictionary

**LEXICON Prepositions**

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

## Adverbs
- E. Uí Dhonnchadha
- REMOVED FEB 2004: +Phr
ADDED FEB 2004: +Temp 
CHANGED +Gen to +Gn to avoid confusion with +Gen = genitive

**LEXICON Adverb**

word for word, i.e. literally (2019)

MOVED TO ADJ annamh+Adv+Gn:annamh	#;
what about chomh mór/hálainn etc. etc. 

see PART-LEX.TXT (etc.) for following

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adverbs.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/adverbs.lexc)</small>

---

## src-fst-morphology-stems-articles.lexc.md 

## Common Functional Words - Articles
E. Uí Dhonnchadha
(c)2001
- (1) New Irish Grammar by The Christian Brothers  
- (2) Réchúrsa Gramadaí, Brian Mac Giolla Phádraig
- (3) Graméir Gaeilge na mBráithre Críostaí
- (4) Nuachúrsa Gaeilge na mBráithre Críostaí
- (5) A Handbook of Irish Vol 2.An Outline of Modern Irish Grammar,
-     Alfred Bammesberger
- (6) Ó Dónaill Irish-English Dictionary
- (7) Gléacht - Ó Dónaill Online Dictionary 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/articles.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/articles.lexc)</small>

---

## src-fst-morphology-stems-bardic.lexc.md 

## Bardic - Classical Irish
E. Uí Dhonnchadha

**LEXICON Bardiclex**

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/bardic.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/bardic.lexc)</small>

---

## src-fst-morphology-stems-conjunctions.lexc.md 

## CONJUNCTIONS
E. Uí Dhonnchadha
- New Irish Grammar by The Christian Brothers, etc.
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

## DETERMINERS
E. Uí Dhonnchadha

Determiners: Possessives

Determiners: INTERROGATIVES

(definite & indefinite amounts)

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/determiners.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/determiners.lexc)</small>

---

## src-fst-morphology-stems-english.lexc.md 

E. Uí Dhonnchadha
JULY 2013
ENGLISH LEX & COMMUNICATORS (CHILDES term)
AUG 2025 added +OLang/ENG for Giellalt integration

**LEXICON Communicators-English**

@dm discourse marker added to distinguish this from Irish so=seo=here

as in Air France, Air India etc.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/english.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/english.lexc)</small>

---

## src-fst-morphology-stems-interjections.lexc.md 

## INTERJECTIONS
& SPOKEN TAGS (Irish Only)
For English Communicators see english-lex.txt
EUD 2011
FILLED PAUSES (CHILDES term)
COMMUNICATORS (CHILDES term)
SIMPLE EVENTS (CHILDES term)
Unknown/unintelligible/inaudible

**LEXICON Interjections**
Interjections

FILLED PAUSES
**LEXICON Fillers**
Fillers in speech

**LEXICON Communicators**
Communicators in speech

Events in speech transcripts, e.g. cough, sneeze etc.

Anonymisation in transcripts/exam scripts

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/interjections.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/interjections.lexc)</small>

---

## src-fst-morphology-stems-latin.lexc.md 

JUN 2016
## LATIN LEX (RIACORPAS 1)
AUG 2025 added +OLang/LAT for Giellalt integration

**LEXICON Latinlex**
vobis+OLang/LAT+Foreign+Latin:vobis #;
nivus+OLang/LAT+Foreign+Latin:nivus #;

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/latin.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/latin.lexc)</small>

---

## src-fst-morphology-stems-nouns.lexc.md 

## Moirfeolaíocht na nAinmfhocail Gaeilge (Morphology of Irish Nouns)
E. Uí Dhonnchadha 
January 2001 
April 2003:  ^IM general initial mutation flag
REFERENCES 
- (1) New Irish Grammar by The Christian Brothers   
- (2) Gramadach na Gaeilge agus Litriú na Gaeilge - An Caighdeán Oifigiúil 
- (3) Foclóir Póca - An Gúm 
- (4) Nuachúrsa Gaeilge na mBráithre Críostaí 
- (5) Gléacht & Ó Dónaill Irish-English Dictionary 
GENERAL NOTES
0.	Alphabet : a b c d e f g h i l m n o p r s t u + á é í ó ú.
1.	There are three principal cases : Nominative, Genitive and Vocative
2.	Nouns are inflected for number, gender and case. They can be inflected at 
2.1	Gender.
	After the definite article "an" 
In the case of an initial "s", a "t" will be placed before it 
	(b) Masculine nouns will have "t-" inserted before an initial vowel.
2.2	Vowel Harmony must be maintained within words ie a word must be Broad or Slender 
3.	Number.
	1st. Declension - All Masculine - nouns all end in broad consonant
	2nd. Declension - All Feminine -  nouns end in broad or slender consonant
	3rd. Declension - Feminine & Masculine - nouns end in a broad or slender consonant.
	4th. Declension - Feminine & Masculine - all end in a vowel or "ín"
-  **LEXICON Nouns** 
###					1st DECLENSION 
(1) WEAK PLURALS 
Nom												
	an cat (the cat)				na cait	(the cats)		}
	an suipéar (the supper)			na suipéir (the suppers)}
Gen
	ceol an éin (the birds's song)	ceol na n-éan (the birds' song)	
	am an suipéir (the supper's time) an na suipéar (the suppers' time)
Voc
	

-  **airgeadas Nm1-SINGULAR;** 
-  **áireamh Nm1-SINGULAR;** 
-  **amhras Nm1-SINGULAR;** 
-  **aonar Nm1-SINGULAR;** 
etc. 

(2) WEAK PLURALS
EXAMPLE:
Nom	
Gen	
Voc	
	

-  **bruas Nm1-2;**  (thick) lip 
-  **cág Nm1-2;**  jackdaw 
-  **ceart Nm1-2;**  right
-  **cor Nm1-2;** 
-  **fionn Nm1-2;**  fair, white
-  **gnáth Nm1-2;** 
-  **íol Nm1-2;**  idol 

(3) STRONG PLURALS - ADD "TA"
	LONG VOWEL (áéíóú ao ae o[mh] u[mh] i[á|ó] u[á|ó] a[rd|rl|rn|rr])

-  **ál Nm1-3;**  clutch, brood
-  **aon Nm1-3;**  one, ace 
etc.

(4) STRONG PLURALS - ADD "THA"
-  **glór Nm1-4;**  voice
-  **múr Nm1-4;**  wall, shower

(5) STRONG PLURALS - ADD (A)Í

-  **bealach Nm1-5;**  way, road
-  **cogadh Nm1-5;** 
-  **Domhnach Nm1-5;**  Sunday
etc

(6) STRONG PLURALS - ADD  "ANNA"

-  **bás Nm1-6;** 

(7) STRONG PLURALS - ADD "Í"

(8) STRONG PLURALS - SYNCOPATE + ADD "ANNA"

(9) STRONG PLURALS - SYNCOPATE, ATTENUATE + ADD "E"

(10) STRONG PLURALS - SYNCOPATE + ADD "EACHA"

			1 MASC.
		list the categories here ......

-  **baint Nf2-SINGULAR;** 
-  **réir Nf2-SINGULAR;** 
-  **spéis Nf2-SINGULAR;** 
-  **suim Nf2-SINGULAR;** 
-  **teilifís Nf2-SINGULAR;** 
-  **titim Nf2-SINGULAR;** 

(1) WEAK PLURALS (no longer used)
(2) WEAK PLURALS (ie Nom, Gen & Voc plurals are not the same)
ONE SYLLABLE - Broad/Slender
-  **binn Nf2-2;**  peak		
-  **cliath Nf2-2;** 
-  **deoir Nf2-2;**  tear

(3) WEAK PLURALS 

- (4) WEAK PLURALS 
- 	MORE THAN ONE SYLLABLE, 
- 	ENDS IN (E)ACH WHICH CHANGES TO (A)Í IN GEN. SG. (USES ^ATH TAG & D4)
- 	
- 	Nom Pl : Append "a"		(PL-3)
- 	Gen Pl : No change		(PL-0)
- 	Voc Pl : Append "a"		(PL-3)

(5) STRONG PLURALS - ADD "TE"

(7) STRONG PLURALS - ADD "Í"
more than one syllable - SLENDER

BROAD & SLENDER
(8) STRONG PLURALS - ADD -(E)ACHA

) STRONG PLURALS - ADD "THA"

3 Masculine words in 2nd Declension 

###					3rd DECLENSION 

3rd declension FEMININE NOUNS 
-  **coinneáil Nf3-SINGULAR;** 
-  **éisteacht Nf3-SINGULAR;** 
-  **imirt Nf3-4;**  -SINGULAR;

3rd declension MASCULINE NOUNS 

###					4th DECLENSION 

###					5th DECLENSION 

####                   5th Declension MASCULINE NOUNS 

=======================end of 5th declension==========================!

-  **LEXICON NounsB** 

-  **LEXICON NounsC** 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/nouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/nouns.lexc)</small>

---

## src-fst-morphology-stems-numerals.lexc.md 

## NUMBERS
E. Uí Dhonnchadha
Cardinal numbers are described seperately here rather than with other
Adjectives
For Personal Numerals (duine, beirt, triúr) SEE NOUNS

-  **LEXICON Numerals** 

CARDINAL Numbers
-  **aon+Num+Card:aon NumSéUrú;** 
-  **aon+Num+Card+hPref:haon #;**  le haon cheann de na ...
-  **aon+Num+Card+Bare:haon #;**  a haon
-  **aon+Num+Card+DefArt:t-aon #;**  the one; the ace
-  **seacht+Num+Card:seacht NumSéUrú;** 
-  **ocht+Num+Card:ocht NumSéUrú;** 
-  **naoi+Num+Card:naoi NumSéUrú;** 

≈ -  **naoi+Num+Card:naoi NumSéUrú;** 

-  **céad+Num+Ord:céad NumSéUrú;**  first
-  **aon+Num+Ord:aonú NumSéUrú;** 
-  **aon+Num+Ord+Def:t-aonú #;** 

Number  Operators
-  **++Num+Op:+ #;** 
-  **-+Num+Op:- #;** 

-  **LEXICON NumSéUrú** 
-  **#;** 
-  **+Len:^IM^Sé^tv #;** 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/numerals.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/numerals.lexc)</small>

---

## src-fst-morphology-stems-particles.lexc.md 

## PARTICLES
E. Uí Dhonnchadha
- Preverbal
Unique Membership classes
-  **LEXICON Particles** 

-  **a+Part+Vc+Voc:a #; !**  a Shíle  Vc 12/03/2022
-  **a+Part+Nm:a #;**  a haon, a dó
-  **a+Part+Inf:a #;**  uisce a ól (in vn phrase) 

-  **go+Part+Ad:go #;**  go maith
-  **ro+Part+Ad:ro #;**  ro lag (Historical)

-  **Ní+Part+Pat:Ní #;**  Ní Ghráda

VERBAL PARTICLES

tense distiction is unnecessary

relative if can be translated as "who/which/whose/to,on,of etc. whom etc." or "that"

not relative if can't be translated as "who/which/whose/to,on,of etc. whom etc." ???
i.e. complementiser "that" ...

Reflexive (or emphatic) 'féin' moved from pronouns file

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/particles.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/particles.lexc)</small>

---

## src-fst-morphology-stems-pronouns.lexc.md 

## Na Forainmneacha Pearsanta 		- The Personal Pronouns (mé,tú, sé, sí..)
Na Forainmneacha Éiginnte 		- Indefinite Pronouns (ceachtar, cibé ...)
E. Uí Dhonnchadha

-(1) New Irish Grammar by The Christian Brothers  
-(2) Gramadach na Gaeilge agus Litriú na Gaeilge - An Caighdeán Oifigiúil
-(3) Foclóir Póca - An Gúm
-(4) Nuachúrsa Gaeilge na mBráithre Críostaí
-(5) Ó Dónaill Irish-English Dictionary
Pronominals - words which act like pronouns

-  **LEXICON Personal_Pronouns** 
Personal Pronouns

-  **mé+Pron+Pers+1P+Sg:mé #;**  me
-  **tú+Pron+Pers+2P+Sg:tú #;**  you

Emphatic/Contrastive Pronouns

this is not an independent pronoun - it accompanies an pronoun or noun

Indefinite Pronouns
Interrogative Pronouns (added Feb 05) 
removed Pro from cén as noun complement is needed unlike cé
also include Det Art Sg in det-lex for "a shonrú cén dáta" = which

Copular DEMONSTRATIVE  See also Determiners

PREPOSITIONAL PRONOUNS (CONJUGATED PREPOSITIONS)

-  **LEXICON Emph_sa**  Broad: 1S & 2S & 3S(Fem) & 2P

-  **LEXICON Emph_se**  Slender: 1S & 2S & 3S(Fem) & 2P

-  **LEXICON Emph_san**  Broad: 3S(Masc) & 3P

-  **LEXICON Emph_sean**  Slender: 3S(Masc) & 3P

-  **LEXICON Emph_e** Br/Sl: 1P

-  **LEXICON Demonstrative** 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/pronouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/pronouns.lexc)</small>

---

## src-fst-morphology-stems-propernouns.lexc.md 

Moirfeolaíocht na nAinmfhocail Gaeilge (Morphology of Irish Nouns)
##		PROPER NOUNS
E. Uí Dhonnchadha 
2003
2024 Updated for +Sem/Org, +PersName, etc for Semantic tagging and NER
-  **LEXICON NP-LEX-EIRE** 

-  **< Á t h %_:% C l i a t h > NP-PLACE;** 
-  **< Á i t h %_:% C l i a t h > NP-PLACE;** 
-  **< Á t h a %_:% C l i a t h > NP-PLACE;** 

-  **Oileán Nm1-Prop-Place;** 
-  **Oileáin NP-PLACE-pl;** 
-  **Meán Nm1-Prop-Place;** 
-  **Oírr Nm1-Prop-Place;** 

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

## Punctuation
E. Uí Dhonnchadha

May 2004 : +Quo instead of +St & +End for quotation marks
Feb 2023 : +Curr for currency symbols

-  **LEXICON Punctuation_ga** 
-  **%. Final;** 
-  **<%!> Final;** 
-  **%.%.%. Final;** 
-  **%.%. Final;** 
-  **%? FinalQ;** 

-  **%" Quote;** 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/punctuations.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/punctuations.lexc)</small>

---

## src-fst-morphology-stems-tags.lexc.md 

## XML Tags
E Uí Dhonnchadha

**LEXICON XMLTags**

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/tags.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/tags.lexc)</small>

---

## src-fst-morphology-stems-tobar.lexc.md 

## Tobar
Tobar - ac Grianna
- E. Uí Dhonnchadha
Jan 2009

**LEXICON Tobar** 

-  abair+Verb+VTI+Vow+PastImp:adeireadh #; 

-  is_ea+Cop+Pres+Pron+Pers+3P+Sg:is_ea #;  is ea
-  is_éard+Cop+Pres+Noun+Masc+Com+Sg:is_éard #; is éard

PLACENAMES

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/tobar.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/tobar.lexc)</small>

---

## src-fst-morphology-stems-verbalnouns.lexc.md 

## Verbal nouns
Ainm Briathra & Aidiacht Briathra - 
Verbal Nouns & Verbal Adjectives
- E Uí Dhonnchadha
2003 
- Nov 2005 version 3 
Updated May 2008
- verbal nouns have vn lemma rather than verb lemma
verbal noun gen is same as verbal adj except for new vns ending in -áil
and some other e.g. úsáide, úsáidte 
CW manually checked Foclóir Póca entries and added FGB entries
- Updated Dec 2018: reorganised and verbal nouns have verb lemma again

-  **LEXICON VerbalNounsV** 
-  ábhraigh+Verbal+Noun+VI:ábhrú VN-INIT;
-  achainigh+Verbal+Noun+VTI:achainí VN-INIT;
-  achair+Verbal+Noun+VTI:achairt VN-INIT;
-  achoimrigh+Verbal+Noun+VT:achoimriú VN-INIT;
-  achtáil+Verbal+Noun+VT:achtáil VN-INIT;
-  achtaigh+Verbal+Noun+VT:achtú VN-INIT;
-  aclaigh+Verbal+Noun+VTI:aclú VN-INIT;
-  adamhaigh+Verbal+Noun+VT:adamhú VN-INIT;
-  adhain+Verbal+Noun+VTI:adhaint VN-INIT;
etc... appro 7400 stems

NOTE: 'druideadh' is commented out since it was not found as a verbal noun
in the corpus, yet chances are that it would get mixed up with 'druideadh'
as independed form of 'druid', i.e. 'ó druideadh an scoil'

INCLUDED HERE AS THEY ARE NOT SHARED WITH ANY OTHER POS
**LEXICON VN-INIT**
- #;
- +Len:^IM^Sé #;
- +Ecl:^IM^Urú #;
- +hPref:^IM^hv #;

**LEXICON VA-INIT**
- #;
- +Len:^IM^Sé #;

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/verbalnouns.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/stems/verbalnouns.lexc)</small>

---

## src-fst-morphology-stems-verbs.lexc.md 

## Verb stems
Briathra Gaeilge - Irregular
E. Uí Dhonnchadha
14/10/96
- (1) New Irish Grammar by The Christian Brothers  
- (2) Gramadach na Gaeilge agus Litriú na Gaeilge - An Caighdeán Oifigiúil
- (3) Foclóir Póca - An Gúm
- (4) Nuachúrsa Gaeilge na mBráithre Críostaí
- (5) Ó Dónaill Irish-English Dictionary

```
oct 2004 - removed PastSubj
may 2012 - added +Suf, +Var, +Typo and tidied many things
dec 2019 - added non-std fuair for bardic
****************************************************************************
! First Conjugation Verb Stems
------------------------------------------------------------------------
V1-BR: 	one syllable (broad vowel - gutha leathan)
------------------------------------------------------------------------
V1-SL: 	one syllable (slender vowel - gutha caol )
------------------------------------------------------------------------
V1-BR-LV: Broad F-sufixes Slender T-suffixes (áigh, eoigh, óigh, uaigh, úigh)
------------------------------------------------------------------------
V!-SL-LV: Slender F-suffixes Slender T-suffixes (verbs ending in -éigh ) p99
------------------------------------------------------------------------
V1-SV:	Slender F Slender T ( verbs ending in -igh preceded
		by a cons. or cons. + short vowel ) p100
------------------------------------------------------------------------
V1-SL-BR:	eisceachtaí do V1-SL; e.g. siúil
		leathnaítear iad SEACHAS
		a) Imperative 2P Sg, e.g. siúil
		b) All of Past Ind. except 1P Pl, e.g. shiúlamar
------------------------------------------------------------------------
V1-BR-SL:	eisceachtaí do V1-BR; a mhalairt de V1-SL-BR; e.g. tafann 
		caolaítear agus coimrítear iad SEACHAS
		a) Imperative 2P Sg, e.g. tafann
		b) All of Past Ind. except 1P Pl, e.g. ????
------------------------------------------------------------------------
V1-SL-X:	eisceachtaí do V1-SL; leathnaítear iad ; 
		?? polysyllabic with stress on second syllable  
		is this a reason why they are in the first declension?
------------------------------------------------------------------------
V1-SL-LC:	ends in áil
```
-  **LEXICON VerbsC1A** 

-  mol+Verb+VTI:mol V1-BR; 
-  glac+Verb+VT:glac V1-BR;  ta -. tha (glactha)
-  lúb+Verb+VTI:lúb V1-BR; 

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

## src-fst-transcriptions-transcriptor-symbols2text.lexc.md 



This file contains mappings from abbreviations and some acronyms to full
forms for text-to-speech purposes. This is a supplement to the analyser;
the analyser must tag the strings as +ABBR or similar for the transcriptions
to work. The resulting full form must be lemmas known to the analyser,
for further processing.

We describe here how abbreviations in Irish are read out,
for text-to-speech systems.

The file contains:

- miscellaneous symbols

- smileys

- Clause boundary symbols

- Single punctuation marks

- Paired punctuation marks

* * *

<small>This (part of) documentation was generated from [src/fst/transcriptions/transcriptor-symbols2text.lexc](https://github.com/giellalt/lang-gle/blob/main/src/fst/transcriptions/transcriptor-symbols2text.lexc)</small>

---

## tools-grammarcheckers-grammarchecker.cg3.md 


##      I R I S H  G R A M M A R   C H E C K E R

### DELIMITERS

* DELIMITERS = "<.>" "<!>" "<?>" "<...>" "<¶>" sent ; 

### TAGS AND SETS

### Tags

This section lists all the tags inherited from the fst, and used as tags
in the syntactic analysis. The next section, **Sets**, contains sets defined
on the basis of the tags listed here, those set names are not visible in the output.

#### Beginning and end of sentence
BOS
EOS

#### Parts of speech tags

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
Ad hoc tag for i > sa, to be revised.

* COMMA
* ¶

#### Tags for POS sub-categories

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

#### Tags for morphosyntactic properties

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
* Inf
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

### Noun errors (Len vs. not Len) after prepositions

The following prepositions cause the following noun to be eclipsed and there are different rules for each preposition.
* LIST ECLIPSE-PREP =  "<ag>" ("ag" Prep Simp SUGGEST) "<ar>" ("ar" Prep Simp SUGGEST) <"as"> ("as" Prep Simp SUGGEST) "<i>" "<I>" ("i" Prep Simp SUGGEST) "<chuig>" ("chuig" Prep Simp SUGGEST) "<roimh>"; 

* LIST ECLIPSE-TRID = "<trí>" ("trí" Prep Simp SUGGEST) "<Trí>"; 
* LIST ECLIPSE-LEIS = "<le>" ("le" Prep Simp SUGGEST) "<Le>"; 

These prepositions always cause the nouns after them to be lenited:
* LIST ART-LEN-PREP = "<ar>" "<de>" "<do>" "<faoi>" "<gan>" "<idir>" "<mar>" "<ó>" "<roimh>" "<trí>";	

Noun errors (Ecl vs. not Ecl) after prepositions

* LIST NUM-LEN = "aon" "<chéad>" "<dhá>" "trí" "<ceithre>" "cúig" "sé" "beirt" "uile"; 		
* LIST NUM-ECL = "seacht" "ocht" "naoi" "deich" ; 
* LIST NUM-PL-ADJ = "<dhá>" "trí" "ceithre" "cúig" "sé" "seacht" "ocht" "naoi" "deich" "beirt" ; 	
* LIST ECL-NON-ECL-N = (".*ó"r) (".*án"r) ; 

* LIST COMMONWORD = ("carr" Noun Masc) ("athair" Noun Masc) ; 	
* LIST RAREWORD = ("carr" Noun Fem) ("athair" Noun Fem) ; 	

####  Syntactic tags

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

* ADLVCASE

* CASE-AGREEMENT
* CASE

* NOT-NOM
* NOT-GEN
* NOT-ACC

#### Verb sets

##### Verbs and their complements

* NOT-V

#### Sets for finiteness and mood

MOOD-V

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

##### Genitive rules

1. N N => N N.Gen (When two nouns come together, the second noun has to be in the genitive case.)

2. N DefArt N => N DefArt N.Gen (When two nouns come together and there is the definite article between the nouns.)

3. N DetPoss N => N DetPoss N.Gen (When two nouns come together and there is a possessive adjective between the nouns, the possessive adjective does not cancel the rule of the second noun being in the genitive case.)

4. N A => N A.Gen When adjectives come after nouns in the genitive, the adjective must be rendered into the genitive case as well.)

5. VN N.Gen => VN N.Gen (When a definite noun follows a verbal noun, the definite noun has to be in the genitive case.)

6. But in singular we want com (??)

Other gen tags:
* LIST &msyn-gen-case-nouns = &msyn-gen-case-nouns ;    is the old genrule tag we want to get rid of

####  Other tags

* LIST &use-ellipsis = &use-ellipsis ;    
* LIST &use-guillemets = &use-guillemets ;    
* LIST &lex-ar-a-haon-a-chlog = &lex-ar-a-haon-a-chlog ; 
* LIST &lex-ar-an-aonach = &lex-ar-an-aonach ; 
* LIST &lex-ar-an-gcaife = &lex-ar-an-gcaife;    
* LIST &lex-ar-an-tae = &lex-ar-an-tae;    
* LIST &lex-tá-is = &lex-tá-is ;      
* LIST &lex-part-comparative-adj = &lex-part-comparative-adj ; 
* LIST &msyn-adj-gender = &msyn-adj-gender ;      
* LIST &msyn-beag-is-fiu-de = &msyn-beag-is-fiu-de ; 
* LIST &msyn-cúpla-plnoun-sgnoun = &msyn-cúpla-plnoun-sgnoun ;     
* LIST &msyn-ecl-after-prep-plus-art = &msyn-ecl-after-prep-plus-art ;     
* LIST &msyn-ecl-after-prep2 = &msyn-ecl-after-prep2 ;     
* LIST &msyn-len-after-roimh = &msyn-len-after-roimh ;     
* LIST &msyn-ecl-after-prep4 = &msyn-ecl-after-prep4 ;     
* LIST &msyn-fada-o = &msyn-fada-o ;    
* LIST &msyn-gen-chun-noun = &msyn-gen-chun-noun ; 
* LIST &msyn-gen-chun-defart-noun = &msyn-gen-chun-defart-noun ; art
* LIST &msyn-gen-vn-femnoun-with-article = &msyn-gen-vn-femnoun-with-article ;	
* LIST &msyn-gen-vn-mascnoun-with-article = &msyn-gen-vn-mascnoun-with-article ;	
* LIST &msyn-ecl-after-verb-particle-q = &msyn-ecl-after-verb-particle-q ; 
* LIST &msyn-hPref-after-copula = &msyn-hPref-after-copula ; 
* LIST &msyn-lenition-after-coppast = &msyn-lenition-after-coppast ; 
* LIST &msyn-hPref-after-neg-imp = &msyn-hPref-after-neg-imp ; 
* LIST &msyn-n-after-i-prep-vowel = &msyn-n-after-i-prep-vowel ; 
* LIST &msyn-hPref-after-na = &msyn-hPref-after-na ; 
* LIST &msyn-hPref-after-sna = &msyn-hPref-after-sna ; 
* LIST &msyn-hPref-after-prep = &msyn-hPref-after-prep ; 
* LIST &msyn-i-mbliana = &msyn-i-mbliana ; 
* LIST &msyn-inis-do = &msyn-inis-do ;    
* LIST &msyn-len-after-prep = &msyn-len-after-prep ;    
* LIST &msyn-lenition-after-ni = &msyn-lenition-after-ni ; 
* LIST &msyn-lenition-after-nior = &msyn-lenition-after-nior ; 
* LIST &msyn-len-after-da = &msyn-len-after-da ; 
* LIST &msyn-len-after-ma = &msyn-len-after-ma ; 
* LIST &msyn-eclipse-after-numbers = &msyn-eclipse-after-numbers ; 
* LIST &msyn-lenition-after-numbers = &msyn-lenition-after-numbers ; 
* LIST &msyn-lenition-after-sa = &msyn-lenition-after-sa ; 
* LIST &msyn-plural-after-sna = &msyn-plural-after-sna ; 
* LIST &msyn-prep-lámh = &msyn-prep-lámh ; 
* LIST &msyn-sna-before-plural = &msyn-sna-before-plural ; 
* LIST &msyn-lenition-after-thar = &msyn-lenition-after-thar ; 
* LIST &msyn-lenition-after-um = &msyn-lenition-after-um ; 
* LIST &lex-conj-plus-copula = &lex-conj-plus-copula ; 
* LIST &msyn-ecl-after-mura = &msyn-ecl-after-mura ;	 
* LIST &msyn-ecl-after-da = &msyn-ecl-after-da ;	 
* LIST &msyn-ecl-after-go = &msyn-ecl-after-go ;	 
* LIST &msyn-ecl-after-nach = &msyn-ecl-after-nach ; 
* LIST &msyn-lenition-after-possessive-adjective = &msyn-lenition-after-possessive-adjective ;      
* LIST &msyn-noun-defart = &msyn-noun-defart ;    
* LIST &msyn-ce-plus-defart = &msyn-ce-plus-defart ; 
* LIST &msyn-prepart-prep = &msyn-prepart-prep ;    
* LIST &msyn-prep-detposs = &msyn-prep-detposs ;    
* LIST &msyn-le-plus-defart = &msyn-le-plus-defart ; 
* LIST &msyn-tri-plus-defart = &msyn-tri-plus-defart ;  
* LIST &msyn-ecl-after-trí-defart = &msyn-ecl-after-trí-defart ; 
* LIST &msyn-possadj-nom-gen = &msyn-possadj-nom-gen ;    
* LIST &msyn-prep-pron = &msyn-prep-pron ;    
* LIST &msyn-sa = &msyn-sa ; 
* LIST &msyn-san = &msyn-san ; 
* LIST &msyn-teastaigh-ó = &msyn-teastaigh-ó ;    
* LIST &lex-da-bharr-sin = &lex-da-bharr-sin ; 	
* LIST &lex-os-a-choinne-sin = &lex-os-a-choinne-sin ; 
* LIST &lex-ina-ainneoin-sin = &lex-ina-ainneoin-sin ; 
* LIST &lex-de-ainneoin = &lex-de-ainneoin ; 
* LIST &lex-chomh = &lex-chomh ; 
* LIST &lex-dairire = &lex-dairire ; 
* LIST &lex-ar-leibheal = &lex-ar-leibheal ; 
* LIST &punct-question-mark = &punct-question-mark ; 
* LIST &syn-a-before-verb-relativephrase = &syn-a-before-verb-relativephrase ;    
* LIST ADDED = ADDED ;   tag ensuring ... hmm
* LIST ADDED-BEFORE-BLANK = ADDED-BEFORE-BLANK ;   tag ensuring ... hmm
* LIST SUGGEST = SUGGEST ;   tag ensuring generation of a suggestion for an errouneous word

* MAPPING-PREFIX = & ;    

Here ends the list and set section

## BEFORE-SECTIONS      

* LIST <fixedcase> = <fixedcase>;       
* ADD:fixedcase-np <fixedcase> TARGET Prop ;     	 ,  Never change case of proper nouns

## SECTION      

### spellchecking

* ADD:spell-it-all (&botún-litrithe SUGGESTWF) (<spelled>) ;      		 = add rule marking typos

* LIST HUMAN-N = "dochtúir" "múinteoir" "bean" "fear" ;    	 (to be moved to other tags)

* **RULE: lex-tá-is ** To change *TÁ* to *IS*

### Gender errors in adjectives

**RULE: msyn-genitive-adj-gender** to change adjectives in the nominative case to adjectives in the genitive case after Feminine genitive nouns.

**RULE: msyn-adj-gender** to change Masculine adjective to Feminine if the adjective follows a feminine noun !!IT WORKS!!

**RULE: msyn-adj-masc-gender** to correct Feminine adjectives to Masculine if the noun is masculine

### Prepositions and pronouns fused

**ADD:msyn-prep-pron** RULE TO CHANGE A PREPOSITION AND A PRONOUN INTO A PREPOSITIONAL PRONOUN (e.g., AG MÉ = AGAM, ROIMH SIBH = ROMHAIBH) !!IT WORKS!!

### Prepositions and possessive adjectives fused

**ADD:msyn-h-after-fem-possessive-adjective**: rule to add h to noun following possessor

#### RULE TO LENITE VERBS AFTER THE NEGATIVE PARTICLE NÍ

#### RULE TO LENITE VERBS IN THE PAST TENSE AFTER THE NEGATIVE PARTICLE NÍOR

Template rule to delete A and modify B in A B strings:

#### rule to correct lenition (séimhiú) errors for nouns after certain prepositions

#### rule to take away lenition for nouns after certain prepositions

#### Rules for lenition

**ADD:msyn-teastaigh-ó**: exchange pronoun with the preposition "ó" when following "teastaigh" IT WORKS

**ADD:msyn-inis-do** ...

**ADD:msyn-fada-o** ...

**ADD:msyn-beag-is-fiu-de** "beag is fiú de" A + "de"

**ADD:msyn-cúpla-plnoun-sgnoun** ..

#### RULE TO CORRECT PLURAL NOUNS AFTER THE WORD CÚPLA AS THE NOUN AFTER CÚPLA SHOULD BE IN THE SINGULAR FORM. !!IT WORKS!!

##### Genitive rule 1. Noun + Noun => Noun + Noun.Gen  Noun <ComGen> Fem Com Sg

##### Genitive rule 2. Noun DefArt Noun => Noun DefArt Noun.Gen

##### Genitive rule 3. Noun DetPoss Noun

A RULE TO CHANGE THE NOUN AFTER A NOUN AND A POSSESIVE ADJECTIVE TO THE GENITIVE CASE.
Note: Rule says target is Noun.Com + Det.Poss + Noun.Com, and changes the final noun.

##### Genitive rule 4 N A

##### Genitive rule 5. Verbal noun + noun e.g., ag scríobh an litir > ag scríobh na litreach VN NOUN ART NOUN.Com > VN Noun Art.Gen Noun.Gen

### Definiteness errors in nouns, e.g., an asal > an t-asal, an bean > an bhean, an sráid > an tsráid.

#### A simple grammar checker rule without suggestions: Ensure preceding nominal agrees with the verb

**ADD:use-guillemets**: Simple punctuation rules showing how to change the lemma in the suggestions:

**ADD:use-ellipsis**

**ADD:use-ie.i.** ...

####  A RULE TO INSERT THE PARTICLE A BEFORE A VERB RELATIVE PHRASE !!IT WORKS!!

**ADD:lex-ar-an-aonach**: A rule to correct the error "ag an aonach" to the correct form "ar an aonach".

**ADD:lex-ar-a-haon-a-chlog** ...

**ADD:lex-ar-an-tae**: This rule is for when people put milk in tea. In Irish, the correct way toy it is that milk is put on tea.

This rule is for when people put milk in coffee. In Irish, the correct way to say it is that milk is put on coffee. At is stands, the rule works for Ulaidh Irish. It needs to be changed to work for standard Irish.

**ADD:lex-ar-an-gcaife** ...

**ADD:faoi an - faoin **: A rule to correct the error "faoi an" to the correct form "faoin".

Rules to insert an h after the negative copula "ní" and certain prepositions

**ADD:msyn-ecl-after-prep-sfem**: Eclipse after preposition ... (sfem?)

* * *

<small>This (part of) documentation was generated from [tools/grammarcheckers/grammarchecker.cg3](https://github.com/giellalt/lang-gle/blob/main/tools/grammarcheckers/grammarchecker.cg3)</small>

---

## tools-grammarcheckers-grc-disambiguator.cg3.md 



* Len
* hPref, for h prefixation
* Ecl

* * *

<small>This (part of) documentation was generated from [tools/grammarcheckers/grc-disambiguator.cg3](https://github.com/giellalt/lang-gle/blob/main/tools/grammarcheckers/grc-disambiguator.cg3)</small>

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
