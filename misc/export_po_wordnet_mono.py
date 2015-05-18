""" A script for exporting the monolingual side wordnet from Kevin Scannell's wordnet
into TSV:

    https://github.com/kscanne/wordnet-gaeilge




"""


import os, sys
import polib

def get_line(_list, line):
    l = [a for a in _list if a.startswith(line)]

    if len(l) > 0:
        return l[0]
    else:
        return None

def clean_comment(comment):
    # TODO: first line is usually irish, comma delmited multiple words
    # second line is usually semantics

    lines = comment.split('\n')
    semantics = []

    ga_line = lines[0]

    ga_words = ga_line.split(', ')

    try:
        note_line = lines[1]
    except:
        note_line = False

    if note_line:
        semantics = ''.join(note_line).replace('IG; N=', '')
    else:
        semantics = note_line

    return {
        'gle_words': ga_words,
        'gle_semantics': semantics,
    }


def clean_eng(eng):

    pos = None
    annotation = None

    eng_desc = eng.msgid
    gle_desc = eng.msgstr

    return {
        'eng_desc': eng_desc,
        'gle_desc': gle_desc,
    }

def make_pair(msg):

    if msg.obsolete == 1:
        #~ msgid "cony  n (pika)"
        #~ msgstr "cony%1:05:02::"
        return []

    gle = clean_comment(msg.tcomment)
    gle_pos = msg.msgctxt.split(' ')[1]
    eng = clean_eng(msg)

    # NB: there will be potentially multiple ga words, with one string

    entry = { }
    entry['gle_pos'] = gle_pos
    entry.update(gle)
    entry.update(eng)

    entries = []

    for w in entry['gle_words']:
        _e = {}
        _e.update(entry)
        _e['gle_words'] = w
        _e['gle_semantics'] = _e['gle_semantics']
        entries.append(_e)

    return entries

def write_tsv(entries):
    from collections import OrderedDict
    import csv

    def enc(_d):
        encd = {}
        for k, v in _d.iteritems():
            if v:
                encd[k] = v.encode('utf-8')
            else:
                encd[k] = '---'
        return encd


    ordered_fieldnames = OrderedDict([
        ('gle_words',None),
        ('gle_semantics',None),
        ('gle_pos',None),
        ('eng_desc',None),
        ('gle_desc',None),
    ])

    dw = csv.DictWriter(sys.stdout, delimiter='\t',
                        fieldnames=ordered_fieldnames)
    dw.writeheader()

    for row in entries:
        dw.writerow(enc(row))

def main():
    """ This transforms a pofile into TSV content.
    """

    f = sys.argv[1]
    catalog = polib.pofile(f)

    pairs = []

    for msg in catalog:
        pairs.extend(make_pair(msg))

    write_tsv(pairs)

if __name__ == "__main__":
    sys.exit(main())

