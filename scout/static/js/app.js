(function () {

	'use strict';

	scout.app = angular.module('scout', ['ui.map'])
		.run(function () {
			console.log('Scout application module running...');
		}).controller('MapCtrl', ['$scope', function($scope) {

			var geocoder = new google.maps.Geocoder(),
				bounds = new google.maps.LatLngBounds();

			$scope.myMarkers = [];

			$scope.mapOptions = {
				center: new google.maps.LatLng(54.5104237, -2.6434287),
				mapTypeControl: false,
				mapTypeId: google.maps.MapTypeId.ROADMAP
			};

			$scope.openMarkerInfo = function(marker) {
				$scope.currentMarker = marker;
				$scope.currentMarkerLat = marker.getPosition().lat();
				$scope.currentMarkerLng = marker.getPosition().lng();
				$scope.myInfoWindow.open($scope.myMap, marker);
			};

			$scope.onMapIdle = function () {
				if ($scope.myMarkers.length === 0) {
					// load each of the existing markers
					angular.forEach(scout.markers, function (marker) {
						if (marker.address) {
							geocoder.geocode({'address': marker.address}, function (results, status) {
								if (status == google.maps.GeocoderStatus.OK) {
									var marker = new google.maps.Marker({
										map: $scope.myMap,
										position: results[0].geometry.location
									});
									$scope.myMarkers.push(marker);
									bounds.extend(marker.position);
									$scope.myMap.fitBounds(bounds);
								} else {
									console.log("Geocode was not successful for the following reason: " + status);
								}
							});
						} else if (marker.lat && marker.long) {
							var gmarker = new google.maps.Marker({
								map: map,
								position: new google.maps.LatLng(marker.lat, marker.long),
								icon: icon
							});
							$scope.myMarkers.push(marker);
							bounds.extend(gmarker.position);
							$scope.myMap.fitBounds(bounds);
						}
					})
				}
			}

		}]);

	window.onGoogleReady = function () {
		angular.bootstrap(document.body, ['scout']);
	};

}());