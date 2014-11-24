$(document).ready(function () {
    var $produtoForm = $('#produto-form');

    $produtoForm.hide();

    $('#mostrar-form-btn').click(function () {
        $produtoForm.slideToggle();
    });

    var $descricaoInput = $('#descricaoInput');
    var $precoInput = $('#precoInput');
    var $ajaxGif = $('#ajax-gif');
    var $descricaoDiv = $('#descricaoDiv');
    var $precoDiv = $('#precoDiv');

    $ajaxGif.hide();

    var $salvarBtn = $('#salvar-btn');
    var $helpDescricaoSpan = $('#help-form-descricao');
    var $helpPrecoSpan = $('#help-form-preco');

    var $corpoTabela = $('#corpo-tabela');

    var adicionarLinha = function adicionarLinha(produto) {
       var linha = '<tr id="tr' + produto.id + '"> <td>' + produto.descricao + '</td>' +
            '<td>' + produto.preco + '</td>' +
            '<td><button id="deletar-btn' + produto.id + '" class="btn btn-danger btn-sm"><i class="glyphicon glyphicon-trash"></i></button>' +
            '</td> </tr>';

        $corpoTabela.prepend(linha);

        var $linhaHtml = $('#tr' + produto.id);
        $linhaHtml.hide();
        $linhaHtml.fadeIn();

        $('#deletar-btn' + produto.id).click(function () {
            $linhaHtml.fadeOut();

            $.post('/produtos/rest/delete', {'produto_id': produto.id }).success(function () {
                $linhaHtml.remove();
            }).error(function () {
                alert('Remoção não funcionou!');
                $linhaHtml.fadeIn();
            });
        });
    }

    $.get('/produtos/rest').success(function (listaProdutos) {
        for (var i = 0; i < listaProdutos.length; i += 1) {
            adicionarLinha(listaProdutos[i]);
        }
    });

    $salvarBtn.click(function () {
        var produto = { descricao: $descricaoInput.val(),
            preco: $precoInput.val()};
        $ajaxGif.slideDown();
        $salvarBtn.hide();
        var promessa = $.post('/produtos/rest/save', produto);
        promessa.success(function (produto_do_servidor) {
            //console.log(produto_do_servidor);
            adicionarLinha(produto_do_servidor);
        });

        promessa.error(function (erros) {
            if (erros.responseJSON != null && erros.responseJSON.descricao != null) {
                $descricaoDiv.addClass('has-error');
                $helpDescricaoSpan.text(erros.responseJSON.descricao);
            }
            if (erros.responseJSON != null && erros.responseJSON.preco != null) {
                $precoDiv.addClass('has-error');
                $helpPrecoSpan.text(erros.responseJSON.preco);
            }
        });
        promessa.always(function () {
            $ajaxGif.slideUp();
            $salvarBtn.slideDown();
        })
    });
});