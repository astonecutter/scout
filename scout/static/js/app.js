(function () {

	'use strict';

	angular.module('scout', ['ui.map'])
		.run(function () {
			console.log('Scout application module running...');
		}).controller('MapCtrl', ['$scope', function($scope) {
			$scope.mapOptions = {
				center: new google.maps.LatLng(54.5104237, -2.6434287),
				mapTypeControl: false,
				mapTypeId: google.maps.MapTypeId.ROADMAP,
				zoom: 6
			};
		}]);

	window.onGoogleReady = function () {
		angular.bootstrap(document.body, ['scout']);
	};

}());