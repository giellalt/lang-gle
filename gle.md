
# Irish morphological analyser                      !
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.


 # Definitions for Multichar_Symbols

## Analysis symbols
The morphological analyses of wordforms for the Irish
language are presented in this system in terms of the following symbols.
(It is highly suggested to follow existing standards when adding new tags).









































Subj is used for subjunctive



 * +Symbol = independent symbols in the text stream, like £, €, ©
















































































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














# Irish morphological analyser                      !
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.


 # Definitions for Multichar_Symbols

## Analysis symbols
The morphological analyses of wordforms for the Irish
language are presented in this system in terms of the following symbols.
(It is highly suggested to follow existing standards when adding new tags).









































Subj is used for subjunctive



 * +Symbol = independent symbols in the text stream, like £, €, ©
















































































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














# Irish morphological analyser                      !
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.


 # Definitions for Multichar_Symbols

## Analysis symbols
The morphological analyses of wordforms for the Irish
language are presented in this system in terms of the following symbols.
(It is highly suggested to follow existing standards when adding new tags).









































Subj is used for subjunctive



 * +Symbol = independent symbols in the text stream, like £, €, ©
















































































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







































































































































































































































Proper noun inflection
The Irish language proper nouns inflect in the same cases as regular
nouns, but with a colon (':') as separator.




# Symbol affixes





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

























































































































































































inserted +Len +Uru to distinguish between a bhíonn & a mbíonn Dir/Indir
Rel clauses Dec 2004
inserted ^Verb (x5) in NegQ (EUD 14-10-2017)



FORMS NOT LENITED IN POSITIVE PAST TENSE incl IMPERFECT













áil -> Gen ála

=================================== !
The Irish morphophonological/twolc rules file !
=================================== !








* *primus%>s*
* *primus%>0*


* examples:*

* examples:*


* examples:*

* examples:*

# Irish morphological analyser                      !
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.


 # Definitions for Multichar_Symbols

## Analysis symbols
The morphological analyses of wordforms for the Irish
language are presented in this system in terms of the following symbols.
(It is highly suggested to follow existing standards when adding new tags).









































Subj is used for subjunctive



 * +Symbol = independent symbols in the text stream, like £, €, ©
















































































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














# Irish morphological analyser                      !
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF Irish LANGUAGE.


 # Definitions for Multichar_Symbols

## Analysis symbols
The morphological analyses of wordforms for the Irish
language are presented in this system in terms of the following symbols.
(It is highly suggested to follow existing standards when adding new tags).









































Subj is used for subjunctive



 * +Symbol = independent symbols in the text stream, like £, €, ©
















































































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





































































































new category 28/03/08
















































































































SEE N-LEX-IRREG muineál	 Nm1-1;	 ! gs & npl -níl


















Automatically assigned CCs

Manually assigned CCs
see n-lex-stems.txt ceathracha	Nm5-1;	! gs ~d pl ~idí



























CONTINUATION CLASSES MASCULINE




















































no because Na hAfraice Láir/Theas etc ..<A f r a i c %_:%  T h e a s>	Nf2-Prop;	! !!!!South Africa
Mar 2012
Mar 2012

Added. Most popular names.
Male


Female































PARTICLES
Preverbal
Unique Membership classes










tense distiction is unnecessary





relative if can be translated as "who/which/whose" (or "that")



not relative if can't be translated as "who/which/whose" ???
i.e. complementiser "that" ...



Multichar_Symbols

+XMLTag		! 

LEXICON Root
	XMLTags;











Abbreviations

















Prefixes
Prefixes in the Irish language are bound to beginning of other words.



 Na Forainmneacha Pearsanta 		- The Personal Pronouns (mé,tú, sé, sí..)
 Na Forainmneacha Éiginnte 		- Indefinite Pronouns (ceachtar, cibé ...)
Pronominals - words which act like pronouns






















removed Pro from cén as noun complement is needed unlike cé
also include Det Art Sg in det-lex for "a shonrú cén dáta" = which
































INTERJECTIONS

















Foclóir Póca etc.
April 2008: Regenerated from verb stems by Christoph Wendler 
(v=sceamh) CHECKED







NOTE: 'druideadh' is commented out since it was not found as a verbal noun
in the corpus, yet chances are that it would get mixed up with 'druideadh'
as independed form of 'druid', i.e. 'ó druideadh an scoil'



DETERMINERS





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
Abbreviations 
and a few English words










Adverbs










MOVED TO ADJ annamh+Adv+Gn:annamh	#;
what about chomh mór/hálainn etc. etc. 



see PART-LEX.TXT (etc.) for following






Na hAidiactaí Tuairisciúla - Descriptive Adjectives





























































SEE PREP/NUM etc dá	Adj3-1;	 ! do or de +









































  I R R E G U L A R   A D J E C T I V E S 




the following always come at the end of the noun/pron/adj and cannot 
be intermingled with other adjectives 
Have moved to Demonstrative Determiners 






































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








Tobar - ac Grianna


















PLACENAMES


### CONJUNCTIONS
removed items (subbord conjs) which are pre-verbal (which often have past tense inflection)
e.g. go/gur a/ar nach/nár 
and which often follow (or attach to) a conjunction
e.g. cé go, nuair nach, 
remaining subordinating conjunctions can be followed by verb or copula 
go mb'fhusa an obair ..., go dtógfadh sé
e.g. má bhíonn, más
some still have tense marking as they are combined forms
e.g. sula, sular, murar etc.





gur NOT moved to Verb Part as a)always precede a verb b) have tense c) preceded by conjs like nuair, cé











Common Functional Words






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
































NUMERALS
Cardinal numbers are described seperately here rather than with other
Adjectives
For Personal Numerals (duine, beirt, triúr) SEE NOUNS























































% komma% :,      Root ;
% tjuohkkis% :%. Root ;
% kolon% :%:     Root ;
% sárggis% :%-   Root ; 
% násti% :%*     Root ; 




We describe here how abbreviations are in Irish are read out, e.g.
for text-to-speech systems.

For example:

 * s.:syntynyt # ;  
 * os.:omaa% sukua # ;  
 * v.:vuosi # ;  
 * v.:vuonna # ;  
 * esim.:esimerkki # ; 
 * esim.:esimerkiksi # ; 


