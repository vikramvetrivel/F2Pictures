mainApp.controller('F2PicturesDetails', ['$scope', 'F2PicturesDetailsService', function($scope, F2PicturesDetailsService){

    F2PicturesDetailsService.getF2PicturesDetails()
        .then(
            function(data){
                $scope.details=data;
            }
        );
}]);