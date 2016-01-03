// Author: Vikram
// Description: Angular Directive to display the locationMap using google apis
// In code, use <locationMap></locationMap>
mainApp.directive('locationMap', function(){
    // Runs during compile
    return {
        restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
        replace: true,
        transclude: false,
        compile: function(tElement, tAttrs){ 

            var html = "<div id='map'></div>";
            var newElem = $(html);
            tElement.replaceWith(newElem);

            return function linking(scope, elm, attrs){
                var mapOptions = {
                    center: new google.maps.LatLng(-33.885631, 151.201677),
                    zoom: 17,
                    draggable:false,
                    scrollwheel: true,
                    disableDefaultUI: true,
                    mapTypeId: google.maps.MapTypeId.ROADMAP,
                    styles: [{ stylers: [{saturation: -50}]}]
                    };
                
                var mapCanvas = document.getElementById('map');
                var map = new google.maps.Map(mapCanvas, mapOptions);
            }
        },
    };
});