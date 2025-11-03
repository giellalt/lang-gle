# Noun (Gaeilge) Replace Rules
Elaine Uí Dhonnchadha
12/12/96 - continued March 1998
## INTRO
Certain vowel combinations will be represented by one symbol as these vowel
sounds should be treated as a unit.
### DIPHTHONG EXAMPLE
For example in slenderising "ua" we want "uai" not "uiai".
Diphthongs 
### LONG VOWEL EXAMPLE
In cathair (city) the "ai" is syncopated but in cathaoir (chair) "aoi" is not.
There are two other diphthongs in Irish but the are not explicitly represented
orthographically (radharc, etc see Fpóca)
### Long Vowels
## Rules 
### Definitions
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
