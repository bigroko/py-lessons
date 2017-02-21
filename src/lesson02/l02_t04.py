# -*- coding: UTF-8 -*-

from collections import defaultdict

en_la_dict = {'apple': ['malum', 'pomum', 'popula'],
              'fruit': ['baca', 'bacca', 'popum'],
              'punishment': ['malum', 'multa']}
la_en_dict = defaultdict(list)

for k, l in en_la_dict.items():
    for v in l:
        la_en_dict[v].append(k)

la_en_dict.default_factory = None

for k, l in sorted(la_en_dict.items()):
    print('%s - %s' % (k, l))
