mainApp.service('F2PicturesDetailsService', ['$http', function($http){

    return{
    getF2PicturesDetails: function(){
        return $http.get('company/1')
        .then(
            function(res) {
                return res.data
            },
            function(res) {
                console.log("Unable to return data for F2Pictures")
            }
        );    
    }
}
}]);