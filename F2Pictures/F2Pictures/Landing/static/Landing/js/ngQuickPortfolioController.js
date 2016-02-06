mainApp.controller('QuickPortfolioController', ['$scope', function($scope){

    //Ensure that the 'QuickPorfolio' is highlighted in the navbar
    $scope.getClass = function(pageName) {
        if (pageName == 'quickportfolio')
            return 'menu-item menu-item-has-children current-menu-parent';
        else
            return 'menu-item menu-item-has-children'; 
    }

    //This needs to be populated from the DB
    $scope.images = [
    {
      'url': 'static/img/quickportfolio_thumbs (10).jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (10).jpg',
      'genre' : 'fashion'
    },
    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (24).jpg',
      'genre' : 'wedding'
    },
    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (12).jpg',
      'genre' : 'wedding'
    },
    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (20).jpg',
      'genre' : 'fashion'
    },
    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (17).jpg',
      'genre' : 'glamour'
    },
    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (18).jpg',
      'genre' : 'fashion'
    },
    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (7).jpg',
      'genre' : 'fashion'
    },
    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (21).jpg',
      'genre' : 'glamour'
    },

    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (19).jpg',
      'genre' : 'wedding'
    },
    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (22).jpg',
      'genre' : 'fashion'
    },
    {
      'url': 'static/img/recent-post-4.jpg',
      'thumbUrl': 'static/img/quickportfolio_thumbs (27).jpg',
      'genre' : 'fashion'
    }
  ];

}])