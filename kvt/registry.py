# -*- encoding: utf-8 -*-
'''
@Time : 2020/10/4 15:00 
@Author : qinhanluo
@File : registry.py 
@Software: PyCharm
@Description ： TODO
'''
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from kvt.utils import Registry


BACKBONES = Registry('backbone')
MODELS = Registry('models')
LOSSES = Registry('losses')
OPTIMIZERS = Registry('optimizer')
SCHEDULERS = Registry('scheduler')

DATASETS = Registry('dataset')
TRANSFORMS = Registry('transform')
HOOKS = Registry('hook')
