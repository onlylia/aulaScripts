/**
 * Created by User on 26/10/2014.
 */


$(document).ready(function () {

    var $bebidaform = $ ('#bebida-form');
    $bebidaform.hide();
    $('mostrar-form-btn').click(function () {
        $bebidaform.slideToggle();
    });

    var $nomeInput = $('#nomeImput');
    var $precoInput = $('#precoInput');
    var $endImgInput = $('#endImgInput');
    var $tipoInput = $('#tipoInput');

    var $ajaxGif = $('#ajax-gif');
    var $formDiv = $('#formDiv');
    $ajaxGif.hide();

    var $salvarBtn = $('#salvar-btn');
    var $helpFormSpan = $('#help-form');
    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha = function adicionarLinha(bebida){
        var linha = '<tr id="tr' + bebida.id + '" > <td>' + bebida.nome + '</td>'+
            '<td>' + bebida.preco + '</td>' +
            '<td>' + bebida.endImg + '</td>' +
            '<td>' + bebida.tipo + '</td>' +
            '<td><button id="bt' + bebida.id + ' " class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>'+
            '</td> </tr>';

        $corpoTabela.prepend(linha);
        var $linhaHtml = $('#tr' + bebida.id);
        $linhaHtml.hide();
        $linhaHtml.fadeIn();

        $('#bt' + bebida.id).click(function () {
            $linhaHtml.fadeOut();

            $.post('/bebidas/delete', {'bebida_id' : bebida.id }).success(function(){
                $linhaHtml.remove();
            }).error(function(){
                alert('Remoção não funcionou!');
                $linhaHtml.fadeIn();
            });
        });
    }
    $.get('/bebidas').success(function(listaDeBebidas){
        for (var i = 0; i < listaDeBebidas.length; i += 1){
            adicionarLinha(listaDeBebidas[i]);
        }
    });

    $salvarBtn.click(function(){
        var bebida = {  nome : $nomeInput.val(),
                        preco : $precoInput.val(),
                        endImg : $endImgInput.val()};
        $ajaxGif.slideDown();
        $salvarBtn.hide();
        var promessa = $.post('/bebidas/save', bebida);
        promessa.success(function (bebida_do_servidor){
            adicionarLinha(bebida_do_servidor);
        });
        promessa.error(function (erros){
            if (erros.responseJSON != null && erros.responseJSON.nome != null){
                $formDiv.addClass('has-error');
                $helpFormSpan.text(erros.responseJSON.nome);
            }
        });
        promessa.always(function(){
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });
});