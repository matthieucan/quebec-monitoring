'use strict';

/* Filters */

angular.module('myApp.filters', [])
  .filter('interpolate', ['version', function(version) {
    return function(text) {
      return String(text).replace(/\%VERSION\%/mg, version);
    };
  }])

  .filter('state_to_icon', function() {
    return function(state) {
      return (state == 0 ? 'fa-thumbs-o-up' : (state == 1 ? 'fa-hand-o-right' : 'fa-thumbs-o-down'));
    };
  });
