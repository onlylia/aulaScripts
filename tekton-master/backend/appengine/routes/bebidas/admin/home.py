# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from bebida_app import facade
from routes.bebidas.admin import new, edit


def delete(_handler, bebida_id):
    facade.delete_bebida_cmd(bebida_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_bebidas_cmd()
    bebidas = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.bebida_short_form()

    def short_bebida_dict(bebida):
        bebida_dct = short_form.fill_with_model(bebida)
        bebida_dct['edit_path'] = router.to_path(edit_path, bebida_dct['id'])
        bebida_dct['delete_path'] = router.to_path(delete_path, bebida_dct['id'])
        return bebida_dct

    short_bebidas = [short_bebida_dict(bebida) for bebida in bebidas]
    context = {'bebidas': short_bebidas,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

