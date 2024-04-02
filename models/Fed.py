#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import copy
import torch


def Aggregation(w, lens):
    w_avg = None
    if lens == None:
        total_count = len(w)
        lens = []
        for i in range(len(w)):
            lens.append(1.0)
    else:
        total_count = sum(lens)

    for i in range(0, len(w)):
        if i == 0:
            w_avg = copy.deepcopy(w[0])
            for k in w_avg.keys():
                w_avg[k] = w[i][k] * lens[i]
        else:
            for k in w_avg.keys():
                w_avg[k] += w[i][k] * lens[i]

    for k in w_avg.keys():
        w_avg[k] = torch.div(w_avg[k], total_count)

    return w_avg


def Weighted_Aggregation_FedASync(w_local, w_global, alpha):
    for i in w_local.keys():
        w_global[i] = alpha * w_local[i] + (1 - alpha) * w_global[i]
    return w_global


def Weighted_Aggregation_FedSA(update_w, lens, w_global):
    w_avg = None
    total_count = sum(lens.values())
    alpha = sum([lens[idx] / total_count for idx in update_w.keys()])

    for i, idx in enumerate(update_w.keys()):
        if i == 0:
            w_avg = copy.deepcopy(update_w[idx])
            for k in w_avg.keys():
                w_avg[k] = update_w[idx][k] * lens[idx]
        else:
            for k in w_avg.keys():
                w_avg[k] += update_w[idx][k] * lens[idx]

    for k in w_avg.keys():
        w_avg[k] = torch.div(w_avg[k], total_count)
    # return w_avg

    for i in w_avg.keys():
        w_global[i] = w_avg[i] + (1 - alpha) * w_global[i]
    return w_global
