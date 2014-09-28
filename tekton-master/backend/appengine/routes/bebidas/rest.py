# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from bebida_app import facade


def index():
    cmd = facade.list_bebidas_cmd()
    bebida_list = cmd()
    short_form=facade.bebida_short_form()
    bebida_short = [short_form.fill_with_model(m) for m in bebida_list]
    return JsonResponse(bebida_short)


def save(**bebida_properties):
    cmd = facade.save_bebida_cmd(**bebida_properties)
    return _save_or_update_json_response(cmd)


def update(bebida_id, **bebida_properties):
    cmd = facade.update_bebida_cmd(bebida_id, **bebida_properties)
    return _save_or_update_json_response(cmd)


def delete(bebida_id):
    facade.delete_bebida_cmd(bebida_id)()


def _save_or_update_json_response(cmd):
    try:
        bebida = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.bebida_short_form()
    return JsonResponse(short_form.fill_with_model(bebida))

