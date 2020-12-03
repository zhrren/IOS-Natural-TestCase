# -*- encoding=utf8 -*-
__author__ = "ren"

from airtest.core.api import *
from poco.drivers.ios import iosPoco

auto_setup(__file__)

poco = iosPoco()

keyevent("HOME")


touch(Template(r"tpl1606972189981.png", record_pos=(-0.351, -0.311), resolution=(1170, 2532)))

touch(touch(Template(r"tpl1606985178786.png", record_pos=(-0.214, -0.655), resolution=(1170, 2532)))
)

touch(Template(r"tpl1606966480833.png", record_pos=(-0.399, -0.895), resolution=(1170, 2532)))
