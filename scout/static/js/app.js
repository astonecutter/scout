(function () {

	'use strict';

	angular.module('scout', []).run(function () {
		console.log('Scout application module running...');
	});

	window.onGoogleReady = function () {
		angular.bootstrap(document.body, ['scout']);
	};

}());