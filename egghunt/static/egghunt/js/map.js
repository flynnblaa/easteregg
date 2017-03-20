function initialize() {
	var myLatlng = new google.maps.LatLng(54.110359, 7.341932);
	var mapOptions = {
	  center: myLatlng,
	  zoom: 5
};
var map = new google.maps.Map(document.getElementById('map-canvas'),
	mapOptions);
 var marker = new google.maps.Marker({  });
 var lat = document.getElementById("lat");
 var lng = document.getElementById("lng");

google.maps.event.addListener(map, 'click', function(event) {
 marker.setPosition(event.latLng);
 lat.setAttribute("value", marker.getPosition().lat());
 lng.setAttribute("value", marker.getPosition().lng());
 if (marker.getMap() == null)
	 {
	   marker.setMap(map);
	 }
 });
 
// Create the search box and link it to the UI element.
var input = /** @type {HTMLInputElement} */(
  document.getElementById('pac-input'));
map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);

var searchBox = new google.maps.places.SearchBox(
/** @type {HTMLInputElement} */(input));

// Listen for the event fired when the user selects an item from the
// pick list. Retrieve the matching places for that item.
google.maps.event.addListener(searchBox, 'places_changed', function() {
    var places = searchBox.getPlaces();

    if (places.length == 0) {
      return;
    }
    

    // For each place, get the icon, place name, and location.
    
    var bounds = new google.maps.LatLngBounds();
    place = places[0];
    bounds.extend(place.geometry.location);
    map.fitBounds(bounds);
	map.setZoom(15);
  });
  
  // Bias the SearchBox results towards places that are within the bounds of the
  // current map's viewport.
  google.maps.event.addListener(map, 'bounds_changed', function() {
    var bounds = map.getBounds();
    searchBox.setBounds(bounds);
  });
 
}

function validateForm() {
	var lat = document.getElementById("lat");
	return (lat.getAttribute("value") != "");
}
 
google.maps.event.addDomListener(window, 'load', initialize);