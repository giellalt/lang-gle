""" A script for exporting the wordnet from Kevin Scannell's wordnet
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
    # some comments begin with ...
    #    #. IG; N=Dinneenism
    #    #. IG; N=office, jurisdiction, tenure of an abbot
    # but otherwise, ga= and a list

    lines = comment.split('\n')
    ga_line = get_line(lines, 'ga=')
    note_line = get_line(lines, 'IG; ')
    ga_words = ga_line.replace('ga=', '').split(', ')

    if note_line:
        note = ''.join(note_line).replace('IG; N=', '')
    else:
        note = note_line

    return {
        'gle_words': ga_words,
        'gle_annotation_in_eng': note,
    }


def clean_eng(eng):

    pos = None
    annotation = None

    parts = eng.split('  ')

    eng, pos = parts[0], parts[1]

    if ' (' in pos:
        pos, _, annotation = pos.partition(' (')
        annotation = annotation.replace(')', '')

    return {
        'eng': eng,
        'eng_pos': pos,
        'eng_annotation_in_eng': annotation
    }

def make_pair(msg):

    if msg.obsolete == 1:
        #~ msgid "cony  n (pika)"
        #~ msgstr "cony%1:05:02::"
        return []

    gle = clean_comment(msg.comment)
    eng = clean_eng(msg.msgid)

    # NB: there will be potentially multiple ga words, with one string

    entry = { }
    entry.update(gle)
    entry.update(eng)

    entries = []

    for w in entry['gle_words']:
        _e = {}
        _e.update(entry)
        _e['gle_words'] = w
        _e['gle_annotation_in_eng'] = _e['gle_annotation_in_eng']
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
        ('gle_annotation_in_eng',None),
        ('eng',None),
        ('eng_pos',None),
        ('eng_annotation_in_eng',None),
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
