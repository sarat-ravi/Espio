'use strict';

/* Controllers */

var app = angular.module('myApp.controllers', ['firebase'])

app.controller('FeedController', ['$scope', 'angularFire',
    function ($scope, angularFire) {
        var ref = new Firebase('https://sarat.firebaseio.com/test');
        angularFire(ref, $scope, 'tests');
    }
]);
