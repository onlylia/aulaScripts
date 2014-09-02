# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from gaebusiness.business import CommandExecutionException
from tekton import router
from gaecookie.decorator import no_csrf
from produtos_app import facade
from routes.produtoss import admin


@no_csrf
def index():
    return TemplateResponse({'save_path': router.to_path(save)},'produtoss/admin/form.html')


def save(_handler, produto_id=None, **produto_properties):
    cmd = facade.save_produto_cmd(**produto_properties)
    try:
        cmd()
    except CommandExecutionException:
        context = {'errors': cmd.errors,
                   'produto': cmd.form}

        return TemplateResponse(context, 'produtoss/admin/form.html')
    _handler.redirect(router.to_path(admin))

