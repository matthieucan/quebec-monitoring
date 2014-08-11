'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
  'ngRoute',
  'myappAnimations',
  'myApp.filters',
  'myApp.services',
  'myApp.directives',
  'myApp.controllers'
]).
config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {templateUrl: 'partials/home.html', controller: 'HomeCtrl'});
  $routeProvider.when('/infos', {templateUrl: 'partials/infos.html', controller: 'InfosCtrl'});
  $routeProvider.when('/details/:name', {templateUrl: 'partials/details.html', controller: 'DetailsCtrl'});
  $routeProvider.otherwise({redirectTo: '/'});
}]);
