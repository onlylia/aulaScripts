# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.gaeutil import SaveCommand, ModelSearchCommand
from gaeforms.ndb.form import ModelForm
from gaegraph.business_base import UpdateNode
from bebida_app.model import BebidaAlcoolica

class BebidaAlcoolicaPublicForm(ModelForm):
    """
    Form used to show properties on app's home
    """
    _model_class = BebidaAlcoolica
    _include = [BebidaAlcoolica.codigo, 
                BebidaAlcoolica.precouni, 
                BebidaAlcoolica.nome]


class BebidaAlcoolicaForm(ModelForm):
    """
    Form used to save and update operations on app's admin page
    """
    _model_class = BebidaAlcoolica
    _include = [BebidaAlcoolica.codigo, 
                BebidaAlcoolica.precouni, 
                BebidaAlcoolica.nome]


class BebidaAlcoolicaDetailForm(ModelForm):
    """
    Form used to show entity details on app's admin page
    """
    _model_class = BebidaAlcoolica
    _include = [BebidaAlcoolica.codigo, 
                BebidaAlcoolica.creation, 
                BebidaAlcoolica.precouni, 
                BebidaAlcoolica.nome]


class BebidaAlcoolicaShortForm(ModelForm):
    """
    Form used to show entity short version on app's admin page, mainly for tables
    """
    _model_class = BebidaAlcoolica
    _include = [BebidaAlcoolica.codigo, 
                BebidaAlcoolica.creation, 
                BebidaAlcoolica.precouni, 
                BebidaAlcoolica.nome]


class SaveBebidaAlcoolicaCommand(SaveCommand):
    _model_form_class = BebidaAlcoolicaForm


class UpdateBebidaAlcoolicaCommand(UpdateNode):
    _model_form_class = BebidaAlcoolicaForm


class ListBebidaAlcoolicaCommand(ModelSearchCommand):
    def __init__(self):
        super(ListBebidaAlcoolicaCommand, self).__init__(BebidaAlcoolica.query_by_creation())

