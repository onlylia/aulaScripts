# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from gaegraph.model import Node
from gaeforms.ndb import property


class Produto(Node):
    codigo = ndb.StringProperty(required=True)
    nome = ndb.StringProperty(required=True)
    precouni = ndb.FloatProperty(required=True)

