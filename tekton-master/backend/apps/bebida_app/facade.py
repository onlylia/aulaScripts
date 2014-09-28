# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaegraph.business_base import NodeSearch, DeleteNode
from bebida_app.commands import ListBebidaCommand, SaveBebidaCommand, UpdateBebidaCommand, \
    BebidaPublicForm, BebidaDetailForm, BebidaShortForm


def save_bebida_cmd(**bebida_properties):
    """
    Command to save Bebida entity
    :param bebida_properties: a dict of properties to save on model
    :return: a Command that save Bebida, validating and localizing properties received as strings
    """
    return SaveBebidaCommand(**bebida_properties)


def update_bebida_cmd(bebida_id, **bebida_properties):
    """
    Command to update Bebida entity with id equals 'bebida_id'
    :param bebida_properties: a dict of properties to update model
    :return: a Command that update Bebida, validating and localizing properties received as strings
    """
    return UpdateBebidaCommand(bebida_id, **bebida_properties)


def list_bebidas_cmd():
    """
    Command to list Bebida entities ordered by their creation dates
    :return: a Command proceed the db operations when executed
    """
    return ListBebidaCommand()


def bebida_detail_form(**kwargs):
    """
    Function to get Bebida's detail form.
    :param kwargs: form properties
    :return: Form
    """
    return BebidaDetailForm(**kwargs)


def bebida_short_form(**kwargs):
    """
    Function to get Bebida's short form. just a subset of bebida's properties
    :param kwargs: form properties
    :return: Form
    """
    return BebidaShortForm(**kwargs)

def bebida_public_form(**kwargs):
    """
    Function to get Bebida'spublic form. just a subset of bebida's properties
    :param kwargs: form properties
    :return: Form
    """
    return BebidaPublicForm(**kwargs)


def get_bebida_cmd(bebida_id):
    """
    Find bebida by her id
    :param bebida_id: the bebida id
    :return: Command
    """
    return NodeSearch(bebida_id)


def delete_bebida_cmd(bebida_id):
    """
    Construct a command to delete a Bebida
    :param bebida_id: bebida's id
    :return: Command
    """
    return DeleteNode(bebida_id)

