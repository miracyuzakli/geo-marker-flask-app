var mymap = L.map('mapid').setView([43.7, -79.42], 12); // Toronto'nun varsayılan koordinatları
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19
}).addTo(mymap);

var coordinates = [];
var markers = [];
var polyline = null;



// ! Loading Spin
 // Yükleme ekranını ve butonunu seç
 var loadingScreen = document.getElementById("loadingScreen");

 function closeLoadingScreen() {
     loadingScreen.classList.remove("loading-visible");
 }


function getSelectedRadioButtonId(radio_name) {
    var radios = document.getElementsByName(radio_name);
    for (var i = 0; i < radios.length; i++) {
        if (radios[i].checked) {
            return radios[i].value;
        }
    }
    // Eğer hiçbir radio butonu seçili değilse null döndür
    return null;
}


function getSelectedOptionValue(selectId) {
    var selectElement = document.getElementById(selectId);
    if (!selectElement) {
        console.log('Select elementi bulunamadı.');
        return null;
    }

    return selectElement.options[selectElement.selectedIndex].value;
}

function getSelectedOptionText(selectId) {
    var selectElement = document.getElementById(selectId);
    if (!selectElement) {
        console.log('Select elementi bulunamadı.');
        return null; // Eğer select elementi bulunamazsa, null döndür
    }

    return selectElement.options[selectElement.selectedIndex].text;
}

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

    var cities = getSelectedOptionText('option-cities');

    var sale_date_value = getSelectedRadioButtonId('sale-date-radios');
    var property_type_value = getSelectedRadioButtonId('property-type-radios');

    var price_amount_from = getSelectedOptionValue('option-price-from');
    var price_amount_to = getSelectedOptionValue('option-price-to');

    var lot_size_from = getSelectedOptionValue('option-lot-size-from');
    var lot_size_to = getSelectedOptionValue('option-lot-size-to');

    var city1 = getSelectedOptionText('option-city');

    console.log(city1);

   

    
    loadingScreen.classList.toggle("loading-visible");

    $.ajax({
        url: '/send-coordinates',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            "city": cities,
            "city_name": city1,

            "sale_date": sale_date_value,
            "property_type": property_type_value,

            "price_amount": {
                "from": price_amount_from,
                "to": price_amount_to
            },

            "lot_size": {
                "from": lot_size_from,
                "to": lot_size_to
            },

            coordinates: coordinates

        }),
        success: function (response) {
            
            if (response.status == "success") {
                closeLoadingScreen();
                alert("Data has been generated..")
            } else {
                console.log("Error!!!")
            }
            

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
    mymap.setView(new L.LatLng(selectedCityCoordinates[0], selectedCityCoordinates[1]), 12);
}