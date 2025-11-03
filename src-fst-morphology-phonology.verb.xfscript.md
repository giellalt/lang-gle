# Verb (Gaeilge) Replace Rules
Elaine Uí Dhonnchadha
(c) 2001 - NEW
2005 - new vn/va triggers
## PastInd & Imper use stem
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

## 2nd. Conjugation Syncopation of Stem

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

## 1st Conjugation Slender Stems => broaden stems; leave slender for t endings

- [%^LC -> %^Caol || _ %^Verb [t|.#.]] 
- [i -> [%^FB ] || ?+ _ ? %^LC %^Verb] 
- [%^LC -> 0 ] 

## 1st Conjugation Slender Stems => slenderise endings ! order is important

- [a i -> %^FS i || %^Caol %^Verb [f|t]* _ ?+] 
- [a í -> %^FS í || %^Caol %^Verb [f|t]* _ ?* .#.] 
- [a -> %^FS e || %^Caol %^Verb [f|t]* _ .#.] 
- [á -> %^FS e á || %^Caol %^Verb [f|t]* _ .#.] 
- [a -> %^FS e a || %^Caol %^Verb [f|t]* _ ?+]  f/t - to prevent  amar - eamear
- [ó -> %^FS e o || %^Caol %^Verb [f|t]* _ ?+] 
- [%^Caol -> []] 

## 1st Conjugation Slender Stems => broaden root eg sábháil

- [i -> [%^FB ] || _ ? %^Lea] 
- [%^Lea -> []] 
- [%^Verb -> []] 

- [%^VAdj -> [] ] TEMPORARY - VERBAL ADJS. AND VERBAL NOUNS
IN 2 MUST BE SORTED OUT

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.verb.xfscript](https://github.com/giellalt/lang-gle/blob/main/src/fst/morphology/phonology.verb.xfscript)</small>
