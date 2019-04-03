#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import lmfit
import matplotlib.pyplot as plt

data = np.loadtxt('data.txt')
x = data[0]
y = data[1]


model = lmfit.models.GaussianModel()
params = model.guess(y, x=x)
params.pretty_print()
out = model.fit(y, params, x=x)
print(out.fit_report(min_correl=0.25))


plt.plot(data[0], data[1])
plt.show()
