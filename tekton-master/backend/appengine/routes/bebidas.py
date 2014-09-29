from __future__ import absolute_import, unicode_literals

from google.appengine.ext import ndb
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
    # tipo = ndb.KeyProperty(BebidaTipo, required=True)

class BebidaForm(ModelForm):
    _model_class = Bebida
    _include = [Bebida.nome, Bebida.preco, Bebida.endImg]

# #com classe form e possivel validar ate o que nao vai para o banco
# class BebidaFormOld(Form):
#    nome = base.StringField(required=True)
#    preco = base.FloatField(required=True)
#    endImg = base.StringField(required=True)



#Formularios
@no_csrf
def form():
    contexto = {'save_path': router.to_path(salvar)}
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



#Editar
def editar(bebida_id, **propriedades):
    bebida_id = int(bebida_id)
    bebida = Bebida.get_by_id(bebida_id)
    bebida_form = BebidaForm(**propriedades)
    erros = bebida_form.validate()
    if erros:
        contexto = {'save_path': router.to_path(salvar), 'erros': erros, 'bebida': bebida_form}
        return TemplateResponse(contexto, 'bebidas/form.html')
    else:
        bebida_form.fill_model(bebida)
        bebida.put()
        return RedirectResponse(router.to_path(index))



#Index
@login_not_required
@no_csrf
def index():
    query = Bebida.query().order(Bebida.preco)
    bebida_lista = query.fetch()
    form = BebidaForm()
    bebida_lista = [form.fill_with_model(bebida)for bebida in bebida_lista]
    edit_path = router.to_path(editar_form)
    for bebida in bebida_lista:
        bebida['edit_path'] = '%s/%s'%(edit_path, bebida['id'])
    contexto = { 'bebida_lista' : bebida_lista }
    return TemplateResponse(contexto)