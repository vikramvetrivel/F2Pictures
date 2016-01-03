var mainApp = angular.module('mainApp', ['ngRoute']);

mainApp.controller('TopLevelServicesController', ['$scope', function($scope){
    
    $scope.topLevelServices = ['Photography', 'Films and Videos'];
    $scope.topLevelServiceTagLine = ['Weddings and Events', 'Corporate and Weddings']
}])


mainApp.config(['$routeProvider', function($routeProvider) {
    $routeProvider

        .when('/home', {
            controller: 'TopLevelServicesController',
            templateUrl: 'static/Landing/ngTemplates/mainpage.html'
        })

        .when('/', {
            controller: 'TopLevelServicesController',
            templateUrl: 'static/Landing/ngTemplates/mainpage.html'
        })

        .when('/contact', {
            controller: 'LeadGeneratorController',
            templateUrl: 'static/Landing/ngTemplates/contact.html'
        })

        .otherwise({
            redirectTo: '/'     
        });
}])