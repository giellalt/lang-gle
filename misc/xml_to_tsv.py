""" Exports a TSV from an XML file based on rules defined in a .yaml file

    python xml_to_tsv.py rules.yaml input_xml.xml

Example YAML structure is defined in iat_tsv.yaml

"""

import sys

from lxml import etree

def parse_options(path):
    """ Read a yaml file and return the options.
    """

    import yaml

    with open(path, 'r') as F:
        _yaml = yaml.load(F)

    def fix_cols(col_opts):
        """ Turn a dict into a list """
        _cs = []
        for c in col_opts:
            _cs.append((
                c.get('name'),
                c.get('xpath'),
                c.get('opts', {})
            ))
        return _cs

    opts = {}


    target_opts = _yaml.get('Target')

    opts['columns'] = fix_cols(target_opts.pop('columns'))
    opts['export_opts'] = target_opts
    opts['row_selector'] = _yaml.get('Source').get('row_selector')

    return opts


def nodes_to_row(opts, nodes):
    """ Read the nodes
    """

    from collections import OrderedDict

    columns = opts.get('columns')

    _rows = []
    # ('name', None),
    _header = OrderedDict([
        (c[0], None) for c in columns
    ])

    for n in nodes:
        _row = {}
        for c, xp, opts in columns:

            try:
                vals = n.xpath(xp)
            except etree.XPathEvalError:
                print 'invalid xpath: '
                print '  ' + xp
                sys.exit()

            if 'delim' in opts:
                _row[c] = opts.get('delim').join(vals)
            else:
                _row[c] = vals

        _rows.append(_row)
    
    return _header, _rows

def print_tsv(opts, header, rows):
    """ Print the parsed data to TSV
    """

    import csv
    from operator import itemgetter

    export_opts = opts.get('export_opts')

    def enc(_d):
        encd = {}
        for k, v in _d.iteritems():
            if v:
                try:
                    encd[k] = v.encode('utf-8')
                except AttributeError:
                    print 'cannot encode <%s> for <%s>' % (k, repr(v))
                    sys.exit()
            else:
                encd[k] = '---'
        return encd


    dw = csv.DictWriter(sys.stdout, delimiter='\t',
                        fieldnames=header)
    dw.writeheader()

    if 'sort_by' in export_opts:
        rows = sorted(rows, key=itemgetter(export_opts.get('sort_by')))

    for row in rows:
        try:
            dw.writerow(enc(row))
        except ValueError, e:
            print e
            print header
            print row
            sys.exit()

def main():
    opts_path = sys.argv[1]
    filename = sys.argv[2]

    opts = parse_options(opts_path)

    root = etree.parse(filename).getroot()

    entry_nodes = root.xpath(opts.get('row_selector'))

    header, rows = nodes_to_row(opts, entry_nodes)

    print_tsv(opts, header, rows)

if __name__ == "__main__":
    sys.exit(main())
