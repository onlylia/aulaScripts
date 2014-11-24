
$(document).ready(function () {

    var $bebidaform = $('#bebida-form');
    $bebidaform.hide();
    $('#mostrar-form-btn').click(function () {
        $bebidaform.slideToggle();
    });

    var $nomeInput = $('#nomeInput');
    var $precoInput = $('#precoInput');
    var $endImgInput = $('#endImgInput');
    var $tipoInput = $('#tipoInput');

    var $ajaxGif = $('#ajax-gif');
    var $formDiv = $('#formDiv');

    $ajaxGif.hide();

    var $salvarBtn = $('#salvar-btn');
    var $helpNomeSpan = $('#help-form-nome');
    var $helpPrecoSpan = $('#help-form-preco');
    var $helpImgEndSpan = $('#help-form-endImg');
    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha = function adicionarLinha(bebida){
        var linha;
        linha = '<tr id="tr' + bebida.id + '"> <td><button id="editar-btn' +
            bebida.id + '"class="btn btn-success btn-sm"><i class="glyphicon glyphicon-pencil"></i></button>' +
            '</td>' +
            '<td><button id="deletar-btn' + bebida.id + ' " class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td>' +
            '<td>' + bebida.nome + '</td>' +
            '<td>' + bebida.preco + '</td> </tr>';

//        var linha = '<tr id="tr' + bebida.id + '" > <td>' + bebida.nome + '</td>'+
//            '<td>' + bebida.preco + '</td>' +
//            '<td>' + bebida.endImg + '</td>' +
//            '<td>' + bebida.tipo + '</td>' +
//            '<td><button id="bt' + bebida.id + ' " class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>'+
//            '</td> </tr>';

        $corpoTabela.prepend(linha);
        var $linhaHtml = $('#tr' + bebida.id);
        $linhaHtml.hide();
        $linhaHtml.fadeIn();

        $('#deletar-btn' + bebida.id).click(function () {
            $linhaHtml.fadeOut();

            $.post('/bebidas/delete', {'bebida_id' : bebida.id }).success(function(){
                $linhaHtml.remove();
            }).error(function(){
                alert('Remoção não funcionou!');
                $linhaHtml.fadeIn();
            });
        });
    }
    $.get('/bebidas/listarJson').success(function(listaBebidas){
        for (var i = 0; i < listaBebidas.length; i += 1){
            adicionarLinha(listaBebidas[i]);
        }
    });

    $salvarBtn.click(function(){
        var bebida = {  nome : $nomeInput.val(),
                        preco : $precoInput.val(),
                        endImg : $endImgInput.val(),
                        tipo : $tipoInput.val()};
        $ajaxGif.slideDown();
        $salvarBtn.hide();
        var promessa = $.post('/bebidas/salvar', bebida);
        promessa.success(function (bebida_do_servidor){
            //console.log(bebida_do_servidor);
            adicionarLinha(bebida_do_servidor);
        });
        promessa.error(function (erros){
            if (erros.responseJSON != null && erros.responseJSON.nome != null){
                $formDiv.addClass('has-error');
                $helpNomeSpan.text(erros.responseJSON.nome);
            }
            if (erros.responseJSON != null && erros.responseJSON.preco != null){
                $formDiv.addClass('has-error');
                $helpPrecoSpan.text(erros.responseJSON.nome);
            }
            if (erros.responseJSON != null && erros.responseJSON.endImg != null){
                $formDiv.addClass('has-error');
                $helpImgEndSpan.text(erros.responseJSON.nome);
            }
        });
        promessa.always(function(){
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });
});