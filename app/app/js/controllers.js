'use strict';

/* utils */
function correct_output(plugin_output) {
  var output = '';
  if (plugin_output == "all checks were successful.") {
    output = 'ok';
  }
  else {
    if (plugin_output.length < 2) {
      output = plugin_output.length + " problème";
    }
    else {
      output = plugin_output.length + " problèmes";
    }
  }
  return output;
}


/* Controllers */

angular.module('myApp.controllers', [])

  /* home page */
  .controller('HomeCtrl', ['$scope', '$http',
    function($scope, $http) {
      /* all boxes information */
      $http.get('/adagios/rest/status/json/services/?fields=host_name,display_name,state,icon_image,plugin_output,&groups__has_field=main').success(function(data) {
        $scope.boxes = data;
        $scope.boxes.forEach(function(entry) {
          entry.output = correct_output(entry.plugin_output);
        });
      });

  }])

  /* infos page */
  .controller('InfosCtrl', ['$scope',
    function($scope) {
  }])

  /* details view page */
  .controller('DetailsCtrl', ['$scope', '$routeParams', '$http', 'mapService',
    function($scope, $routeParams, $http, mapService) {
      
      /* box general information */
      $http.get('/adagios/rest/status/json/services/?fields=display_name,state,icon_image,plugin_output,labels,notes&host_name=' + $routeParams.name).success(function(data) {
        $scope.box = data[0];
        $scope.box.output = correct_output($scope.box.plugin_output);
        $scope.box.display_map = ($.inArray('map', $scope.box.labels) == 0);

        if ($scope.box.display_map) {
          /* let's create the map */
          var map = mapService.create();
          map.map.render('map');
        }

      });

      /* elements in this box */
      $http.get('/adagios/rest/status/json/services/?fields=display_name,state,plugin_output,action_url,icon_image_alt&groups__has_field=' + $routeParams.name).success(function(data) {
        $scope.elements = data;

        /* how many problems? */
        var problems = 0;
        data.forEach(function(entry) {
          if (entry.state > 0) {
            problems++;
          }
          });

        /* gauge loader */
        var g = new JustGage({
          id: "gauge",
          value: problems,
          min: 0,
          max: data.length,
          title: "Problèmes",
          hideMinMax: true,
          valueFontColor: "white",
          titleFontColor: "white",
          gaugeWidthScale: 0.3,
          gaugeColor: "black",
          levelColors: ["#ffffff"],
          shadowOpacity: 0.5
        });

      });

  }]);
