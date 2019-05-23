"""
A convenience script to search and replace strings in files.

usage: search-replace.py <json-table> [<input-file> [<output-file>]]

Where <json-table> is either:

* an object with search strings as keys and replacement
  strings as values, e.g. {"search": "replace"}

* an array of arrays containing search and replacement
  string pairs, e.g. [["search1", "replace1"], ["search2", "replace2"]]

* a filename preceeded by @, such as @table.json, and the
  file should contain the replacement table in one of the
  two JSON formats described above

In the second form, the order of replacements is ensured
to follow the order of the array.

"""

__version__ = "0.1.2"


import json
from docopt import docopt
from openfile import openfile


def get_table(table_source):
    if table_source.startswith("@"):
        with openfile(table_source[1:], "rt") as f:
            table = json.loads(f.read())
    else:
        table = json.loads(table_source)
    if isinstance(table, dict):
        assert all(isinstance(key, str) for key in table.keys())
        assert all(isinstance(value, str) for value in table.values())
        table = list(table.items())
    else:
        assert all(len(pair) == 2 for pair in table)
        assert all(
            isinstance(search, str) and isinstance(replacement, str)
            for search, replacement in table
        )
    return table


def search_replace(table, input_file, output_file):
    for line in input_file:
        for search, replacement in table:
            line = line.replace(search, replacement)
        output_file.write(line)


def main():
    options = docopt(__doc__)
    table = get_table(options["<json-table>"])
    with openfile(options["<input-file>"]) as input_file:
        with openfile(options["<output-file>"], "wt") as output_file:
            search_replace(table, input_file, output_file)


if __name__ == "__main__":
    main()
