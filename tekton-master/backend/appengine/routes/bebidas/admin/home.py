# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from config.template_middleware import TemplateResponse
from tekton import router
from gaecookie.decorator import no_csrf
from bebida_app import facade
from routes.bebidas.admin import new, edit


def delete(_handler, bebida_alcoolica_id):
    facade.delete_bebida_alcoolica_cmd(bebida_alcoolica_id)()
    _handler.redirect(router.to_path(index))


@no_csrf
def index():
    cmd = facade.list_bebida_alcoolicas_cmd()
    bebida_alcoolicas = cmd()
    edit_path = router.to_path(edit)
    delete_path = router.to_path(delete)
    short_form = facade.bebida_alcoolica_short_form()

    def short_bebida_alcoolica_dict(bebida_alcoolica):
        bebida_alcoolica_dct = short_form.fill_with_model(bebida_alcoolica)
        bebida_alcoolica_dct['edit_path'] = router.to_path(edit_path, bebida_alcoolica_dct['id'])
        bebida_alcoolica_dct['delete_path'] = router.to_path(delete_path, bebida_alcoolica_dct['id'])
        return bebida_alcoolica_dct

    short_bebida_alcoolicas = [short_bebida_alcoolica_dict(bebida_alcoolica) for bebida_alcoolica in bebida_alcoolicas]
    context = {'bebida_alcoolicas': short_bebida_alcoolicas,
               'new_path': router.to_path(new)}
    return TemplateResponse(context)

