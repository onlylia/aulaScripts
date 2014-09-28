# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from bebida_app import facade
from routes.bebidas import admin


@no_csrf
def index(bebida_id):
    bebida = facade.get_bebida_cmd(bebida_id)()
    detail_form = facade.bebida_detail_form()
    context = {'save_path': router.to_path(save, bebida_id), 'bebida': detail_form.fill_with_model(bebida)}
    return TemplateResponse(context, 'bebidas/admin/form.html')


def save(_handler, bebida_id, **bebida_properties):
    cmd = facade.update_bebida_cmd(bebida_id, **bebida_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'bebida': cmd.form}

        return TemplateResponse(context, 'bebidas/admin/form.html')
    _handler.redirect(router.to_path(admin))

