""" Iterate over a TSV and render it via a Jinja template. 

    python render_tsv.py template.j2 input.tsv > output.whatever

IDEA / TODO: create a template filter that analyzes in an FST, and makes
the output accesssible as a python obj, allows comparing eng tags, and
inserting lemmas where they don't exist. This could be done as a
separate step on a TSV, but what if we also want access to tagsets

IDEA / TODO: merge in additional files by selecting TSV column as ID
field, but this can be done by merging TSVs before.

"""

from jinja2 import Template, Environment, FileSystemLoader
import sys
import os
import csv

PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_ENVIRONMENT = Environment(
    autoescape=False,
    loader=FileSystemLoader(os.path.join(PATH, '.')),
    trim_blocks=False,
    extensions=[
        'jinja2.ext.autoescape',
    ]
)

def render_template(template_filename, context):
    return TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context)

def read_tsv(f):
    def enc(_d):
        encd = {}
        for k, v in _d.iteritems():
            if v:
                try:
                    encd[k] = v.decode('utf-8')
                except AttributeError:
                    print 'cannot encode <%s> for <%s>' % (k, repr(v))
                    sys.exit()
            else:
                encd[k] = '---'
        return encd

    with open(f, 'r') as R:
        read = csv.DictReader(R, delimiter='\t')
        rows = map(enc, read)
    return rows

def main():
    template_file = sys.argv[1]
    input_file = sys.argv[2]
    env = Environment()
    rows = read_tsv(input_file)

    print >> sys.stdout, render_template(template_file, {'rows': rows}).encode('utf-8')

if __name__ == "__main__":
    sys.exit(main())
