# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from bebida_app import facade
from routes.bebidas import admin


@login_not_required
@no_csrf
def index():
    cmd = facade.list_bebidas_cmd()
    bebidas = cmd()
    public_form = facade.bebida_public_form()
    bebida_public_dcts = [public_form.fill_with_model(bebida) for bebida in bebidas]
    context = {'bebidas': bebida_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

