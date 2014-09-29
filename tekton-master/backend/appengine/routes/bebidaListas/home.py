from __future__ import absolute_import, unicode_literals
from google.appengine.ext import ndb
from bebidaTipo_app.model import BebidaTipo
from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


@login_not_required
@no_csrf
def index():
    query = BebidaTipo.query().order(BebidaTipo.descricao)
    tipos = query.fetch()
    contexto = {'tipos': tipos}
    return TemplateResponse(contexto)


@login_not_required
@no_csrf
def exibir(bebida_tipo_id):
    tipo = BebidaTipo.get_by_id(int(bebida_tipo_id))
    query=Bebida.query(Bebida.tipo==tipo.key)
    lista_de_bebidas = query.fetch()
    contexto = {'lista_de_bebidas':lista_de_bebidas,
                'tipo': tipo,
                'salvar_path':router.to_path(salvar_bebida)}
    return TemplateResponse(contexto, 'bebidaListas/exibir.html')


@login_not_required
def salvar_bebida(bebida_tipo_id, nome, endImg, price):
    tipo_chave = ndb.Key(BebidaTipo, int(bebida_tipo_id))
    bebida = Bebida(nome=nome, endImg=endImg, preco=float(price), tipo=tipo_chave)
    bebida.put()
    return RedirectResponse(router.to_path(exibir, bebida_tipo_id))

# Modelo e formulario

class Bebida(ndb.Model):
    nome = ndb.StringProperty(required=True)
    endImg = ndb.StringProperty(required=True)
    price = ndb.FloatProperty(required=True)
    tipo = ndb.KeyProperty(BebidaTipo, required=True)
