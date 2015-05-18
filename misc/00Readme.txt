This directory is meant as a local storage room for files that should *NOT* be
part of svn. Ie store here all and any files you as a developer need to keep for
your own private purposes as part of working with the language.

Every file in this dir will be ignored by svn, and nothing will be built by the
build system.


--

Goal:

An auto-generated lexicon from a variety of external sources, but also
allows for inclusion of our own material, and exclusion of material from
external sources that we do not need. Upstream changes should be easily
mergable.


Sources:

 * https://github.com/kscanne/wordnet-gaeilge - GNU licensed.
 * 

Dependencies:

 * q - Install instructions: http://harelba.github.io/q/install.html
 * python virtualenv

Building:

Once you have compiled the dependencies:

{{{
    make environment 
    make external 
    make all
}}}

Contents:

 * {{export_po_wordnet.py, export_po_wordnet_mono.py}} A parser for .po
   files from Kevin Scannell's wordnet

 * {{xml_to_tsv.py}} A XML -> TSV/CSV script - rules for conversion are
   stored in a YAML file.

 * {{render_tsv.py}} A TSV/CSV -> XML template language script. Read a
   TSV with columns, and then render that to XML via Jinja templates.

Thinking:

 * Keep it easy to integrate new changes from upstream. If Kevin makes a
   change to the wordnet for orthographic/grammatical reasons, we want
   to be able to get these.

 * Make it easy to override stuff from upstream too, and provide our own
   local content.

 * Try to keep individual scripts as separate as possible, 

 * Convert all resources to TSV first, because it's easier to merge
   resources that way, add POS, analyze for lemma, or find the matching
   POS between two separate languages.

 * Any repeated tasks need to be documented/codified in the Makefile.
