#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 09:07:59 2023

@author: ahunos
bayesian for beta bernollli 
"""
import numpy as np

class bernoulli():

    def __init__(self, X, thetas):
        self.X = X #all bernoulli reponses
        self.thetas = thetas #all possible/calculable thetas you can imagine for simulatio

    def llh_bernollli(self, theta):
        """
        func to cal log likeli
        """
        singleX=np.log(pow(theta, self.X) * pow((1-theta), (1-self.X)))
        return np.sum(singleX) # total log likleihood
    
    def mle_llh(self):
        """
        use `llh_bernollli` to calculate likelikehood for all possible thetas can imagine
        """
        loglikelihood_single_theta = [self.llh_bernollli(theta=t) for t in self.thetas]
        return np.array(loglikelihood_single_theta)
    
    
    
    #define functions for beta dstribution
    '''
    expectation od beta 
    expectaion of posterio
    calculate prior 
    implement mormalizing
    plot different prior and posterior 
     concept of decision making
     geberastive process for bernoulli 
     how does bayesian differs from mle
     implement gibbs sampleing  for  bernoulli f
     
    '''