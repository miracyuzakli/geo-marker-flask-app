var mymap = L.map('mapid').setView([43.7, -79.42], 10); // Toronto'nun varsayılan koordinatları
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
}).addTo(mymap);

var coordinates = [];
var markers = [];
var polyline = null;

function updatePolyline() {
    if (polyline) {
        mymap.removeLayer(polyline);
    }
    var polylineCoordinates = coordinates.length === 4 ? [...coordinates, coordinates[0]] : coordinates;
    polyline = L.polyline(polylineCoordinates, { color: 'red' }).addTo(mymap);
}

mymap.on('click', function (e) {
    if (coordinates.length < 4) {
        var newMarker = L.marker([e.latlng.lat, e.latlng.lng]).addTo(mymap);
        markers.push(newMarker);
        coordinates.push([e.latlng.lat, e.latlng.lng]);
        updatePolyline();
    }
});

function sendCoordinates() {
    $.ajax({
        url: '/send-coordinates',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ coordinates: coordinates }),
        success: function (response) {
            console.log(response.message);
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function undoLast() {
    if (coordinates.length > 0) {
        coordinates.pop();
        var lastMarker = markers.pop();
        mymap.removeLayer(lastMarker);
        updatePolyline();
    }
}

function clearAll() {
    for (var i = 0; i < markers.length; i++) {
        mymap.removeLayer(markers[i]);
    }
    markers = [];
    coordinates = [];
    if (polyline) {
        mymap.removeLayer(polyline);
    }
}


function updateMapToSelectedCity() {
    var selectedCityCoordinates = JSON.parse(document.getElementById('option-cities').value);
    mymap.setView(new L.LatLng(selectedCityCoordinates[0], selectedCityCoordinates[1]), 10);
}