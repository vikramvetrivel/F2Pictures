var mainApp = angular.module('mainApp', ['ngRoute', 'ui.bootstrap']);

mainApp.controller('TopLevelServicesController', ['$scope', '$location',  function($scope, $location){
    
    $scope.topLevelServices = ['Photography', 'Films and Videos'];
    $scope.topLevelServiceTagLine = ['Fashion Portfolios, Weddings and Events', 'Corporate and Weddings']

    $scope.getClass = function(pageName) {
        if (pageName == 'home')
            return 'menu-item menu-item-has-children current-menu-parent';
        else
            return 'menu-item menu-item-has-children'; 
    }

}]);


/*mainApp.config(['cfpLoadingBarProvider', function(cfpLoadingBarProvider) {
    cfpLoadingBarProvider.includeSpinner = false;
}]);*/


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

        .when('/photography', {
            templateUrl: 'static/Landing/ngTemplates/photography/campaigns.html'
        })

        .when('/photography/campaigns', {
            templateUrl: 'static/Landing/ngTemplates/photography/campaigns.html'
        })

        .when('/videos', {
            templateUrl: 'static/Landing/ngTemplates/videos/about.html'
        })

        .when('/videos/about', {
            templateUrl: 'static/Landing/ngTemplates/videos/about.html'
        })

        .when('/photography/models', {
            templateUrl: 'static/Landing/ngTemplates/photography/beamodel.html'
        })

        .when('/quickportfolio', {
            controller: 'QuickPortfolioController',
            templateUrl: 'static/Landing/ngTemplates/quickportfolio.html'
        })

        .otherwise({
            redirectTo: '/'     
        });
}]);