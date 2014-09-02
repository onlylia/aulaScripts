# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from bebida_app import facade
from routes.bebidas import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'bebidas/admin/form.html')


def save(_handler, bebida_alcoolica_id=None, **bebida_alcoolica_properties):
    cmd = facade.save_bebida_alcoolica_cmd(**bebida_alcoolica_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'bebida_alcoolica': cmd.form}

        return TemplateResponse(context, 'bebidas/admin/form.html')
    _handler.redirect(router.to_path(admin))

