# -*- coding: utf-8 -*-
import abc

# ニューラルネットワーク用の抽象クラスを定義
class AbstractNeuralNetwork(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self):         # 初期化
        raise NotImplemented()
    @abc.abstractmethod
    def train(self):            # 学習
        raise NotImplemented()
    @abc.abstractmethod
    def query(self):            # 照会
        raise NotImplemented()

