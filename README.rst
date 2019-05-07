================
 search-replace
================

``search-replace`` is a trivial Python script that implements
 search/replace in text files.

Copyright (c) 2019 Luís Gomes <luismsgomes@gmail.com>

Usage
-----

    search-replace <json-table> [<input-file> [<output-file>]]

Where <json-table> is either:

* an object with search strings as keys and replacement
  strings as values, e.g. ``{"search": "replace"}``

* an array of arrays containing search and replacement
  string pairs, e.g. ``[["search1", "replace1"], ["search2", "replace2"]]``

* a filename preceeded by ``@``, such as ``@table.json``,
  and the file should contain the replacement table in one
  of the two JSON formats described above

In the second form, the order of replacements is ensured
to follow the order of the array.