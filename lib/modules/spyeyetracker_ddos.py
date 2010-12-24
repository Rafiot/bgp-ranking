# -*- coding: utf-8 -*-
import re
import os
import datetime 

from modules.abuse_ch import AbuseCh

class SpyeyetrackerDdos(AbuseCh):
    directory = 'spyeye/ddos/'
    list_type = 2

    def __init__(self, raw_dir):
        AbuseCh.__init__(self)
        self.class_name = self.__class__.__name__
