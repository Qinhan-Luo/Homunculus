# -*- encoding: utf-8 -*-
'''
@Time : 2020/10/4 14:59 
@Author : qinhanluo
@File : __init__.py 
@Software: PyCharm
@Description ： TODO
'''
from .registry import (
        BACKBONES,
        LOSSES,
        OPTIMIZERS,
        SCHEDULERS,
        DATASETS,
        TRANSFORMS,
        HOOKS,
)
from .initialization import initialize
