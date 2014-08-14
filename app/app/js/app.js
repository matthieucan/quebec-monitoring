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
      create: function () {
        var position = new OpenLayers.LonLat(-7864933.6056233 ,7223393.3176719);
        var zoom = 4;
        var markers = new OpenLayers.Layer.Markers("Markers");
        var OSMLayer = new OpenLayers.Layer.OSM('OSM Map', null, {});
        var map = new OpenLayers.Map({
          layers: [OSMLayer, markers],
          center: position,
          zoom: zoom,
        });
        return {map: map, markers: markers};
      },
      icon_0: new OpenLayers.Icon('img/marker-0.png'),
      icon_1: new OpenLayers.Icon('img/marker-1.png'),
      icon_2: new OpenLayers.Icon('img/marker-2.png'),
      icon_3: new OpenLayers.Icon('img/marker-3.png')

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
          title: "Aujourd'hui :",
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
