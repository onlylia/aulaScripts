/**
 * Created by User on 24/11/2014.
 */

var decoracaoModulo = angular.module('decoracao-modulo', ['decoracao-servico']);

decoracaoModulo.directive('decoracaoForm', [function () {

    return {
        restrict: 'E',
        templateUrl: '/static/decoracao/html/form.html',
        scope: {decoracaoSalva: '&'},
        controller: function ($scope, DecoracaoAPI) {
            $scope.decoracao = {endimg: 'bexiga.jpg', descricao: 'Bexiga', preco: '3'};
            $scope.executandoSalvamento = false;
            $scope.erros = {};
            $scope.salvar = function () {
                $scope.executandoSalvamento = true;
                $scope.erros = {};
                var promessa = DecoracaoAPI.salvar($scope.decoracao);
                promessa.success(function (decoracao) {
                    $scope.executandoSalvamento = false;
                    if ($scope.decoracaoSalva != null) {
                        $scope.decoracaoSalva({'decoracao': decoracao})
                    }
                });
                promessa.error(function (erros) {
                    $scope.erros = erros;
                    $scope.executandoSalvamento = false;
                });
            }
        }
    };
}]);

decoracaoModulo.directive('decoracaoLinha', [function () {

    return{
        restrict: 'A',
        replace: true,
        templateUrl: '/static/decoracao/html/linha.html',
        scope:{
            decoracao: "=",
            decoracaoDeletada : '&'
        },
        controller: function ($scope, DecoracaoAPI){
            $scope.apagandoFlag = false;
            $scope.editandoFlag = false;
            $scope.decoracaoEdicao = {};
            $scope.deletar = function () {
                $scope.apagandoFlag = true;
                DecoracaoAPI.deletar($scope.decoracao.id).success(function(){
                    $scope.apagandoFlag = false;
                    if ($scope.decoracaoDeletada != null){
                        $scope.decoracaoDeletada();
                    }
                });
            }

            function copiarDecoracao(origem, destino){
                destino.id=origem.id;
                destino.data=origem.data;
                destino.endimg=origem.endimg;
                destino.descricao=origem.descricao;
                destino.preco=origem.preco;
            }
            $scope.entrarModoEdicao = function () {
                $scope.editandoFlag = true;
                copiarDecoracao($scope.decoracao, $scope.decoracaoEdicao);
            };
            $scope.sairModoEdicao = function () {
                $scope.editandoFlag = false;
            };
            $scope.editar = function (){
                DecoracaoAPI.editar($scope.decoracaoEdicao).success(function(decoracaoServidor){
                    copiarDecoracao(decoracaoServidor, $scope.decoracao);
                    $scope.editandoFlag = false;
                });
            }
        }
    };
}]);