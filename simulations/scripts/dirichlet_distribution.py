#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:35:21 2023

@author: ahunos
sample from a dirchlet 
"""

import numpy as np
alphas = np.random.random_integers(low = 1, high =100, size = 100) #gen random integers to use as alphas


#sample from dirichlet
np.random.dirichlet(alpha=alphas)