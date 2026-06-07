#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B-HİG W* hesap modeli v1."""
from dataclasses import dataclass
from typing import Tuple
import math
import numpy as np

@dataclass
class BHIGParams:
    L: int = 4
    Q: int = 3
    xi_geo: float = 1.0
    lambda_family: float = 0.22501
    chiral_count: int = 2
    chirality_coupling: float = 1.0
    self_weight: float = 0.0
    q_Q: Tuple[float,float,float] = (3.5,2.5,0.0)
    q_uR: Tuple[float,float,float] = (4.0,1.0,0.0)
    q_dR: Tuple[float,float,float] = (3.5,2.5,2.5)
    q_lL: Tuple[float,float,float] = (0.0,0.0,0.0)
    q_eR: Tuple[float,float,float] = (8.5,5.0,3.0)

class BHIGWStarModel:
    def __init__(self, params: BHIGParams = BHIGParams()):
        self.p = params
        self.states = self._states()
        self.N = len(self.states)

    def _states(self):
        p = self.p
        return [(x,y,z,f,chi) for x in range(p.L) for y in range(p.L) for z in range(p.L) for f in range(p.Q) for chi in range(p.chiral_count)]

    def torus_dist2(self, a, b):
        L = self.p.L
        vals = []
        for idx in (0,1,2):
            d = abs(a[idx] - b[idx])
            vals.append(min(d, L-d))
        return sum(v*v for v in vals)

    def relation(self, a, b):
        if a == b:
            return self.p.self_weight
        w_geo = math.exp(-math.sqrt(self.torus_dist2(a,b)) / self.p.xi_geo)
        w_family = self.p.lambda_family ** abs(a[3] - b[3])
        w_chiral = 1.0 if a[4] == b[4] else self.p.chirality_coupling
        return w_geo * w_family * w_chiral

    def build_W(self):
        W = np.zeros((self.N, self.N), dtype=float)
        for i,a in enumerate(self.states):
            for j in range(i, self.N):
                w = self.relation(a, self.states[j])
                W[i,j] = W[j,i] = w
        return W

    @staticmethod
    def laplacian(W):
        return np.diag(W.sum(axis=1)) - W

    def yukawa_values(self):
        p = self.p; lam = p.lambda_family
        exps = {
            'up': {'u': p.q_Q[0]+p.q_uR[0], 'c': p.q_Q[1]+p.q_uR[1], 't': p.q_Q[2]+p.q_uR[2]},
            'down': {'d': p.q_Q[0]+p.q_dR[0], 's': p.q_Q[1]+p.q_dR[1], 'b': p.q_Q[2]+p.q_dR[2]},
            'charged_lepton': {'e': p.q_lL[0]+p.q_eR[0], 'mu': p.q_lL[1]+p.q_eR[1], 'tau': p.q_lL[2]+p.q_eR[2]}
        }
        return {sec: {k: float(lam**e) for k,e in vals.items()} for sec, vals in exps.items()}

    def ckm_scaling(self):
        lam = self.p.lambda_family; q = self.p.q_Q
        return {'Vus': float(lam**abs(q[0]-q[1])), 'Vcb': float(lam**abs(q[1]-q[2])), 'Vub': float(lam**abs(q[0]-q[2]))}

def demo():
    model = BHIGWStarModel()
    W = model.build_W()
    L = model.laplacian(W)
    eig = np.linalg.eigvalsh(L)
    return {
        'N_states': model.N,
        'first_10_laplacian_eigenvalues': [float(x) for x in eig[:10]],
        'yukawa_values': model.yukawa_values(),
        'ckm_scaling': model.ckm_scaling(),
    }
