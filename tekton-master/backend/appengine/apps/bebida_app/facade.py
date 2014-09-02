# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from bebida_app.commands import ListBebidaAlcoolicaCommand, SaveBebidaAlcoolicaCommand, UpdateBebidaAlcoolicaCommand, \
    BebidaAlcoolicaPublicForm, BebidaAlcoolicaDetailForm, BebidaAlcoolicaShortForm


def save_bebida_alcoolica_cmd(**bebida_alcoolica_properties):
    """
    Command to save BebidaAlcoolica entity
    :param bebida_alcoolica_properties: a dict of properties to save on model
    :return: a Command that save BebidaAlcoolica, validating and localizing properties received as strings
    """
    return SaveBebidaAlcoolicaCommand(**bebida_alcoolica_properties)


def update_bebida_alcoolica_cmd(bebida_alcoolica_id, **bebida_alcoolica_properties):
    """
    Command to update BebidaAlcoolica entity with id equals 'bebida_alcoolica_id'
    :param bebida_alcoolica_properties: a dict of properties to update model
    :return: a Command that update BebidaAlcoolica, validating and localizing properties received as strings
    """
    return UpdateBebidaAlcoolicaCommand(bebida_alcoolica_id, **bebida_alcoolica_properties)


def list_bebida_alcoolicas_cmd():
    """
    Command to list BebidaAlcoolica entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListBebidaAlcoolicaCommand()


def bebida_alcoolica_detail_form(**kwargs):
    """
    Function to get BebidaAlcoolica's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return BebidaAlcoolicaDetailForm(**kwargs)


def bebida_alcoolica_short_form(**kwargs):
    """
    Function to get BebidaAlcoolica's short form. just a subset of bebida_alcoolica's properties
    :param kwargs: form properties
    :return: Form
    """
    return BebidaAlcoolicaShortForm(**kwargs)

def bebida_alcoolica_public_form(**kwargs):
    """
    Function to get BebidaAlcoolica'spublic form. just a subset of bebida_alcoolica's properties
    :param kwargs: form properties
    :return: Form
    """
    return BebidaAlcoolicaPublicForm(**kwargs)


def get_bebida_alcoolica_cmd(bebida_alcoolica_id):
    """
    Find bebida_alcoolica by her id
    :param bebida_alcoolica_id: the bebida_alcoolica id
    :return: Command
    """
    return NodeSearch(bebida_alcoolica_id)


def delete_bebida_alcoolica_cmd(bebida_alcoolica_id):
    """
    Construct a command to delete a BebidaAlcoolica
    :param bebida_alcoolica_id: bebida_alcoolica's id
    :return: Command
    """
    return DeleteNode(bebida_alcoolica_id)

