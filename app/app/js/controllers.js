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
        /* nicer output to show */
        $scope.boxes.forEach(function(entry) {
          entry.output = correct_output(entry.plugin_output);
        });

        /* compute the global state */
        var global_state = 0;
        $scope.boxes.forEach(function(entry) {
          var s = entry.state;
          global_state += (s == 0 ? 2 : (s == 1 ? -1 : (s == 2 ? -2 : 0)));
        });
        /* if we obtain n<0, global state CRITICAL
                        n>0, global state WARNING
                        n>2, global state OK */
        $scope.global_state = (global_state < 0 ? 2 : (global_state > 2 ? 0 : 1));
      });

  }])

  /* infos page */
  .controller('InfosCtrl', ['$scope',
    function($scope) {
  }])

  /* details view page */
  .controller('DetailsCtrl', ['$scope', '$routeParams', '$http', 'mapService', 'gaugeService',
    function($scope, $routeParams, $http, mapService, gaugeService) {
      
      /* box general information */
      $http.get('/adagios/rest/status/json/services/?fields=display_name,state,icon_image,plugin_output,labels,notes,notes_url&host_name=' + $routeParams.name).success(function(data) {
        $scope.box = data[0];
        $scope.box.output = correct_output($scope.box.plugin_output);
        $scope.box.display_map = ($.inArray('map', $scope.box.labels) == 0);

        /* elements in this box */
        $http.get('/adagios/rest/status/json/services/?fields=display_name,state,plugin_output,action_url,icon_image_alt&groups__has_field=' + $routeParams.name).success(function(data) {
          $scope.elements = data;

          /* how many elements for each state (0,1,2,3)? */
          var nb_problems = [0,0,0,0];
          data.forEach(function(entry) {
            nb_problems[entry.state]++;
          });
          $scope.nb_problems = nb_problems;

          /* gauge loader */
          var gaugeValue = nb_problems[1]+nb_problems[2]+nb_problems[3];
          var g = gaugeService.create(gaugeValue, data.length);

          /* let's create the map */
          if ($scope.box.display_map) {

            /* compute the coords */
            var coords = [];
            $scope.elements.forEach(function(entry) {
              coords.push([entry.state, entry.icon_image_alt]);
            });

            /* get the map */
            var map = mapService.create(coords);
            $scope.map = map;

            /* map init function */
            $scope.renderMap = function(){
              $scope.map.map.render('map');
            }

            /* map rendering */
            $scope.renderMap();
          }
        });
      });
    }]);
