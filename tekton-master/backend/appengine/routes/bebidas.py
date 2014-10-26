from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
from bebidaTipo_app.model import BebidaTipo
from gaeforms import base
from gaeforms.base import Form
from gaeforms.ndb.form import ModelForm

from config.template_middleware import TemplateResponse
from gaecookie.decorator import no_csrf
from gaegraph.model import Node
from gaepermission.decorator import login_not_required
from tekton import router
from tekton.gae.middleware.redirect import RedirectResponse


#Classes
class Bebida(Node):
    nome = ndb.StringProperty(required=True)
    preco = ndb.FloatProperty(required=True)
    endImg = ndb.StringProperty(required=True)
    tipo = ndb.KeyProperty(BebidaTipo, required=True)

#com classe form e possivel validar ate o que nao vai para o banco
class BebidaForm(ModelForm):
    _model_class = Bebida
    _include = [Bebida.nome, Bebida.preco, Bebida.endImg]

"""
class BebidaForm(Form):
    nome = base.StringField(required=True)
    preco = base.FloatField(required=True)
    endImg = base.StringField(required=True)
    tipo = base.IntegerField(required=True)
"""

#Formularios
@no_csrf
def form():
    query = BebidaTipo.query().order(BebidaTipo.descricao)
    lista_tipos = query.fetch()
    contexto = {'save_path': router.to_path(salvar), 'lista_tipos' : lista_tipos}
    return TemplateResponse(contexto)

@no_csrf
def editar_form(bebida_id):
    bebida_id = int(bebida_id)
    bebida = Bebida.get_by_id(bebida_id)
    bebida_form = BebidaForm()
    bebida_form.fill_with_model(bebida)
    contexto = {'save_path': router.to_path(editar, bebida_id),'bebida' : bebida_form }
    return TemplateResponse(contexto, 'bebidas/form.html')


#Salvar
'''
def salvar(_resp, **propriedades):
    bebida_form = BebidaForm(**propriedades)
    erros = bebida_form.validate()
    if erros:
        contexto = {'save_path': router.to_path(salvar), 'erros': erros, 'bebida': bebida_form}
        return TemplateResponse(contexto, 'bebidas/form.html')
    else:
        #bebida = Bebida(nome=propriedades['nome'], preco=float(propriedades['preco']), endImg=propriedades['endImg'])
        bebida = bebida_form.fill_model()
        bebida.put()
        #_resp.write(propriedades)
        return RedirectResponse(router.to_path(index))
'''

@login_not_required
def salvar(tipo_id, nome, preco, endImg):
    tipo_chave = ndb.Key(BebidaTipo, int(tipo_id))
    bebida = Bebida(nome=nome, preco=float(preco), endImg=endImg, tipo=tipo_chave)
    bebida.put()
    return RedirectResponse(router.to_path(exibir, tipo_id))


#Editar
def editar(bebida_id, **propriedades):
    bebida_id = int(bebida_id)
    bebida = Bebida.get_by_id(bebida_id)
    bebida_form = BebidaForm(**propriedades)
    erros = bebida_form.validate()
    if erros:
        contexto = {'save_path': router.to_path(salvar),
                    'erros': erros,
                    'bebida': bebida_form}
        return TemplateResponse(contexto, 'bebidas/form.html')
    else:
        bebida_form.fill_model(bebida)
        bebida.put()
        return RedirectResponse(router.to_path(index))

#Index
'''
@login_not_required
@no_csrf
def index():
    query = Bebida.query().order(Bebida.preco)
    bebida_lista = query.fetch()
    form = BebidaForm()
    bebida_lista = [form.fill_with_model(bebida)for bebida in bebida_lista]
    edit_path = router.to_path(editar_form)
    delete_path = router.to_path(deletar)
    for bebida in bebida_lista:
        bebida['edit_path'] = '%s/%s'%(edit_path, bebida['id'])
        bebida['delete_path'] = '%s/%s'%(delete_path, bebida['id'])
    contexto = { 'bebida_lista' : bebida_lista }
    return TemplateResponse(contexto)
'''

@no_csrf
@login_not_required
def index():
    query = BebidaTipo.query().order(BebidaTipo.descricao)
    tipos = query.fetch()
    for tipo in tipos:
        tipo.exibir_path = router.to_path(exibir, tipo.key.id())
    contexto = { 'tipo_bebidas' : tipos }
    return TemplateResponse(contexto)

#Deletar
def deletar(bebida_id):
    chave = ndb.Key(Bebida, int(bebida_id))
    chave.delete()
    return RedirectResponse (router.to_path(index))


#Listagem de Bebidas por tipo
@login_not_required
@no_csrf
def exibir(tipo_id):
    tipo = BebidaTipo.get_by_id(int(tipo_id))
    query = Bebida.query(Bebida.tipo == tipo.key).order(Bebida.preco)
    lista_de_bebidas = query.fetch()
    form = BebidaForm()
    lista_de_bebidas = [form.fill_with_model(bebida)for bebida in lista_de_bebidas]
    edit_path = router.to_path(editar_form)
    delete_path = router.to_path(deletar)
    for bebida in lista_de_bebidas:
        bebida['edit_path'] = '%s/%s'%(edit_path, bebida['id'])
        bebida['delete_path'] = '%s/%s'%(delete_path, bebida['id'])
    contexto = {
        'lista_de_bebidas' : lista_de_bebidas,
        'tipo' : tipo,
        'salvar_path' : router.to_path(salvar),
        'return_path' : router.to_path(index)
    }
    return TemplateResponse(contexto, 'bebidas/exibir.html')

'''
@login_not_required
@no_csrf
def index():
    query = Bebida.query().order(Bebida.preco)
    bebida_lista = query.fetch()
    form = BebidaForm()
    bebida_lista = [form.fill_with_model(bebida)for bebida in bebida_lista]
    edit_path = router.to_path(editar_form)
    delete_path = router.to_path(deletar)
    for bebida in bebida_lista:
        bebida['edit_path'] = '%s/%s'%(edit_path, bebida['id'])
        bebida['delete_path'] = '%s/%s'%(delete_path, bebida['id'])
    contexto = { 'bebida_lista' : bebida_lista }
    return TemplateResponse(contexto)
'''