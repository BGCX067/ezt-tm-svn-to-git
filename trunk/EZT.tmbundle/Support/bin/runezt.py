#!/usr/bin/env python
"""runezt.py -- stub for ezt.py"""

import ezt

if __name__ == '__main__':
  import sys
  for filename in sys.argv[1:]:
    template = ezt.Template(filename)
    template.generate(sys.stdout, {})
