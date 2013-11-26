'use strict';

/* Controllers */

var app = angular.module('espio.controllers', ['firebase'])

app.controller('rawFeedController', ['$scope', 'angularFire',
    function ($scope, angularFire) {
        var ref = new Firebase('https://sarat.firebaseio.com/agents');
        angularFire(ref, $scope, 'agents');
    }
]);
