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
    cmd = facade.list_bebida_alcoolicas_cmd()
    bebida_alcoolicas = cmd()
    public_form = facade.bebida_alcoolica_public_form()
    bebida_alcoolica_public_dcts = [public_form.fill_with_model(bebida_alcoolica) for bebida_alcoolica in bebida_alcoolicas]
    context = {'bebida_alcoolicas': bebida_alcoolica_public_dcts,'admin_path':router.to_path(admin)}
    return TemplateResponse(context)

