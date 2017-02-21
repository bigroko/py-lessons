# -*- coding: UTF-8 -*-

dishes = {15: 'borscht', 20: 'cutlet', 10: 'porridge', 2: 'tea'}

for k, v in sorted(dishes.items()):
    print('%s - %d' % (v, k))
