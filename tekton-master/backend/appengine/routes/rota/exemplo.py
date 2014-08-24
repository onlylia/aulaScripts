from gaecookie.decorator import no_csrf
from gaepermission.decorator import login_not_required
from tekton import router

@login_not_required
@no_csrf
def index(_handler):
    path = router.to_path(funcao_request)
    _handler.redirect(path)


@login_not_required
@no_csrf
def funcao_request(_resp, _req, nome):
    nome = _req.get('nome')
    _resp.write('%s'%(nome))

@login_not_required
@no_csrf
def funcao(_resp, _req, nome):
    nome = _req.get('nome')
    _resp.write('%s'%(nome))