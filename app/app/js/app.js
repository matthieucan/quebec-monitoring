'use strict';


// Declare app level module which depends on filters, and services
angular.module('myApp', [
  'ngRoute',
  'myappAnimations',
  'myApp.filters',
  'myApp.services',
  'myApp.directives',
  'myApp.controllers',
  'ui.bootstrap'
])
  .config(['$routeProvider', function($routeProvider) {
    $routeProvider.when('/', {templateUrl: 'partials/home.html', controller: 'HomeCtrl'});
    $routeProvider.when('/infos', {templateUrl: 'partials/infos.html', controller: 'InfosCtrl'});
    $routeProvider.when('/details/:name', {templateUrl: 'partials/details.html', controller: 'DetailsCtrl'});
    $routeProvider.otherwise({redirectTo: '/'});
  }])

  .factory('mapService', function () {
    return {
      create: function (coords) {
        var fromProjection = new OpenLayers.Projection("EPSG:4326");
        var toProjection   = new OpenLayers.Projection("EPSG:900913");

        var icons = [new OpenLayers.Icon('img/marker-0.png'),
                     new OpenLayers.Icon('img/marker-1.png'),
                     new OpenLayers.Icon('img/marker-2.png'),
                     new OpenLayers.Icon('img/marker-3.png')];

        var position = new OpenLayers.LonLat(-71.59765625,47.346927610556655).transform(fromProjection, toProjection);
        var zoom = 6;
        var markers = new OpenLayers.Layer.Markers("Markers");
        var OSMLayer = new OpenLayers.Layer.OSM('OSM Map', null, {});
        var map = new OpenLayers.Map({
          layers: [OSMLayer, markers],
          center: position,
          zoom: zoom,
        });
        /* add all markers */
        coords.forEach(function(state_loc) {
          var state = state_loc[0];
          var loc = state_loc[1];
          var marker = new OpenLayers.Marker(
            new OpenLayers.LonLat.fromString(loc).transform(fromProjection, toProjection),
            icons[state].clone()
          );
          markers.addMarker(marker);
        });

        return {map: map, markers: markers};
      }
    }
  })

  .factory('gaugeService', function () {
    return {
      create: function (value, dataSize) {
        var g = new JustGage({
          id: "gauge",
          value: value,
          min: 0,
          max: dataSize,
          title: "Aujourd'hui",
          hideMinMax: true,
          valueFontColor: "white",
          titleFontColor: "white",
          gaugeWidthScale: 0.3,
          gaugeColor: "black",
          levelColors: ["#ffffff"],
          shadowOpacity: 0.5,
          label: "problème" + (value > 1 ? "s" : ""),
          labelFontColor: "white"
        });
        return g;
      }
    }
  });
