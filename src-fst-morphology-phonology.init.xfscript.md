# Noun (Gaeilge) Replace Rules
## INITIAL MUTATIONS
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
### DEFINITIONS
- define VowelAll a|e|i|o|u|á|é|í|ó|ú|%^AO|%^IA|%^AE|%^UA|A|E|I|O|U|Á|É|Í|Ó|Ú ; 
- define VowelLC a|e|i|o|u|á|é|í|ó|ú|%^AO|%^IA|%^AE|%^UA ; 
- define VowelUC A|E|I|O|U|Á|É|Í|Ó|Ú ; 
- define Len b|c|d|f|g|m|p|t|B|C|D|F|G|M|P|T ; 
- define SLen S|s ; 
- define SWord l|n|r ; 

### Rules
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

### VOWEL PREFIXING t-, h, ts
- [..] -> %^FV t %- || .#. (%^X) _ VowelLC ?* %^M %^C ?* %^tv 
- [..] -> %^FV t || .#. (%^X) _ VowelUC ?* %^M %^C ?* %^tv 
- [%^tv -> []] 

- [..] -> %^FV h || .#. (%^X) _ VowelAll ?* [[%^F %^G] | [%^C]|[%^Verb]|%^IM] ?* %^hv 
- [%^hv -> []] 

- s -> %^FU t s || .#. _ (%^FH) [VowelAll|l|n|r|h] ?* [[%^F %^C]|[%^M %^G]] ?* %^ts 

- S -> %^FU t S || .#. _ (%^FH) [VowelAll|l|n|r|h] ?* [[%^F %^C]|[%^M %^G]] ?* %^ts 

- %^FH h -> [] || .#. %^FU t [s|S] _ 

- %^ts -> [] 

### POSSESSIVE PREFIX 

the following are performed in parallel as we want all forms

- [..] -> %^FV h || .#. _ VowelAll ?+ %^Poss  a hathair - her father
- [..] -> %^FV n %- || .#. _ VowelAll ?+ %^Poss  n-athair - our/your/their
- %^Poss -> [] 

- %^IM -> []  initial mutations caused by compound prepp, possessives etc.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.init.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.init.xfscript)</small>
