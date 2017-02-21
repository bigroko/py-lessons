# -*- coding: UTF-8 -*-

import random


rnd_list = [random.randint(-100, 100) for i in range(10)]
print(rnd_list, sorted(rnd_list))
