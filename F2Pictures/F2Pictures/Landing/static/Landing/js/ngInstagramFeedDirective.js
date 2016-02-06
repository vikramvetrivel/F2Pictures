// Author: Vikram
// Description: Angular Directive to display the locationMap using google apis
// In code, use <locationMap></locationMap>
mainApp.directive('instagramfeed', function(){
    // Runs during compile
    return {
        restrict: 'E', // E = Element, A = Attribute, C = Class, M = Comment
        replace: true,
        transclude: false,
        templateUrl: 'static/Landing/ngTemplates/instagramDirectiveTemplate.html',
        compile: function(tElement, tAttrs){ 
            return function linking(scope, elm, attrs){
            }
        },
    };
});