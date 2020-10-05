#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as mpp
# Ввели необходимые библиотеки
# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1]
    mpp.plot(
        arguments,
        [math.sin(a) * math.cos(a) for a in arguments]
        # Ввели функцию, по которой будет строиться график
    )
    mpp.show()