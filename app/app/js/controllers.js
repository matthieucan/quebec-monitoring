'use strict';

/* Controllers */

angular.module('myApp.controllers', [])
  /* home page */
  .controller('HomeCtrl', ['$scope', '$http',
    function($scope, $http) {
      /* all boxes information */
      $http.get('/adagios/rest/status/json/services/?fields=host_name,display_name,state,icon_image,plugin_output,&groups__has_field=main').success(function(data) {
        $scope.boxes = data;
      });

  }])

  /* infos page */
  .controller('InfosCtrl', ['$scope',
    function($scope) {
  }])

  /* details view page */
  .controller('DetailsCtrl', ['$scope', '$routeParams', '$http',
    function($scope, $routeParams, $http) {
      
      /* box general information */
      $http.get('/adagios/rest/status/json/services/?fields=display_name,state,icon_image&host_name=' + $routeParams.name).success(function(data) {
        $scope.box = data[0];
      });
      
      /* elements in this box */
      $http.get('/adagios/rest/status/json/services/?fields=display_name,state,plugin_output,action_url&groups__has_field=' + $routeParams.name).success(function(data) {
        $scope.elements = data;
      });
      
  }]);
