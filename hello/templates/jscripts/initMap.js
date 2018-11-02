// Initialize and add the map
function initMap() {
  var centerlatlng = new google.maps.LatLng(34.052200, -118.247300);
  var myOptions = {
    zoom: 15,
    center: centerlatlng,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  };
  var map = new google.maps.Map(document.getElementById("map"), myOptions);

  var top1 = {lat: 34.046520 , lng: -118.237411};
  var top2 = {lat: 34.050880 , lng: -118.248253};
  var top3 = {lat: 34.048550, lng: -118.259048 };
  var top4 = {lat: 34.046810 , lng: -118.256981};
  var top5 = {lat: 34.044701, lng: -118.252441};


  var marker1 = new google.maps.Marker({
    position: top1,
    map: map,
  });

  var marker2 = new google.maps.Marker({
    position: top2,
    map: map,
  });

  var marker3 = new google.maps.Marker({
    position: top3,
    map: map,
  });

  var marker4 = new google.maps.Marker({
    position: top4,
    map: map,
  });

  var marker5 = new google.maps.Marker({
    position: top5,
    map: map,
});

console.log("calling intialize google maps")
}
