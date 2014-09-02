# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from gaebusiness.business import CommandExecutionException
from tekton.gae.middleware.json_middleware import JsonResponse
from bebida_app import facade


def index():
    cmd = facade.list_bebida_alcoolicas_cmd()
    bebida_alcoolica_list = cmd()
    short_form=facade.bebida_alcoolica_short_form()
    bebida_alcoolica_short = [short_form.fill_with_model(m) for m in bebida_alcoolica_list]
    return JsonResponse(bebida_alcoolica_short)


def save(**bebida_alcoolica_properties):
    cmd = facade.save_bebida_alcoolica_cmd(**bebida_alcoolica_properties)
    return _save_or_update_json_response(cmd)


def update(bebida_alcoolica_id, **bebida_alcoolica_properties):
    cmd = facade.update_bebida_alcoolica_cmd(bebida_alcoolica_id, **bebida_alcoolica_properties)
    return _save_or_update_json_response(cmd)


def delete(bebida_alcoolica_id):
    facade.delete_bebida_alcoolica_cmd(bebida_alcoolica_id)()


def _save_or_update_json_response(cmd):
    try:
        bebida_alcoolica = cmd()
    except CommandExecutionException:
        return JsonResponse({'errors': cmd.errors})
    short_form=facade.bebida_alcoolica_short_form()
    return JsonResponse(short_form.fill_with_model(bebida_alcoolica))

