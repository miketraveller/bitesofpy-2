from collections import namedtuple
from datetime import datetime
import json


blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here

# Blog = namedtuple('Blog', 'name founders stated tags location site')


def dict2nt(dict_):
    return namedtuple('Blog', dict_.keys())(**dict_)


def nt2json(nt):
    t = dict2nt(nt)
    td = t._asddict()
    return 

