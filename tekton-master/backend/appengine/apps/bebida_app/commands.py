# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from bebida_app.model import Bebida

class BebidaPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = Bebida
    _include = [Bebida.preco, 
                Bebida.endImagem, 
                Bebida.nome]


class BebidaForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = Bebida
    _include = [Bebida.preco, 
                Bebida.endImagem, 
                Bebida.nome]


class BebidaDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = Bebida
    _include = [Bebida.creation, 
                Bebida.preco, 
                Bebida.endImagem, 
                Bebida.nome]


class BebidaShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = Bebida
    _include = [Bebida.creation, 
                Bebida.preco, 
                Bebida.endImagem, 
                Bebida.nome]


class SaveBebidaCommand(SaveCommand):
    _model_form_class = BebidaForm


class UpdateBebidaCommand(UpdateNode):
    _model_form_class = BebidaForm


class ListBebidaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListBebidaCommand, self).__init__(Bebida.query_by_creation())

