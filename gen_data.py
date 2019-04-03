#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def gauss(x):
    """Gaußian function with variable x."""
    a = 10
    sigma = .3
    m = 2.5

    return a * np.exp(-0.5 * ( (x-m)/sigma )**2)
    
N = 100

x = np.linspace(0, 5, N)
data = gauss(x)

np.random.seed(2638439)
y = data + np.random.rand(N)

np.savetxt('data.txt', (x, y))