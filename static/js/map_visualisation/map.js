/* SET GLOBAL CONSTANTS AND VARIABLES */
// Set Gao and Bamako Coordinates
const gaoCoords = [16.2484, -0.0056]; // Gao
const bamakoCoords = [12.6392, -7.9499]; // Bamako

const radiusNM = 60; // Gao airspace limits in Nautical Miles
const radiusKM = radiusNM * 1.8512; // Convert to kilometers
/* SET GLOBAL CONSTANTS AND VARIABLES */

/* GAO AIRSPACE LIMITS */
// Initialise map and centered it on Gao
const map = L.map("map").setView(gaoCoords, 8);

// add openstreet map layers and tiles
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  maxZoom: 19,
}).addTo(map);

// draw a circle to represent Gao's airspace
const gaoAirspace = L.circle(gaoCoords, {
  color: "red",
  fillColor: "#f03",
  fillOpacity: 0.2,
  radius: radiusKM * 1000, // radius in meteres(leaflet requires units in meters)
}).addTo(map);

// a pop up to show details when the airspace is clicked
gaoAirspace.bindPopup("Gao Airspace: 60 NM Radius");

// fit the map bounds to ensure the entire circle is visible
map.fitBounds(gaoAirspace.getBounds());
/* GAO AIRSPACE LIMITS */

// hardcoded segemented waypoints for the routes
const waypoints = [
  { name: "G", coords: gaoCoords },
  { name: "A", coords: [15.8, -1.8] },
  { name: "B", coords: [15.0, -3.8] },
  { name: "C", coords: [14.2, -5.2] },
  { name: "D", coords: [13.5, -6.5] },
  { name: "S", coords: bamakoCoords },
];

// add markers for each waypoints
waypoints.forEach((point) => {
  L.marker(point.coords).addTo(map).bindPopup(`${point.name}`);
});

// extract the coordinates of the waypoints
const routeCoordinates = waypoints.map((point) => point.coords);

//draw the polyline for the flight route
const flightRoute = L.polyline(routeCoordinates, {
  color: "blue",
  weight: 4,
  opacity: 0.8,
}).addTo(map);

// adjust the map bounds to fit the entire route
map.fitBounds(flightRoute.getBounds());

/* SIMULATE THE AIRCRAFT MOVEMENTS */
// add an aircraft marker (initially at Gao)
const aircraftMarker = L.marker(gaoCoords, {
  icon: L.icon({
    iconUrl: "https://cdn-icons-png.flaticon.com/512/5447/5447568.png",
    iconSize: [30, 30],
  }),
}).addTo(map);

// function to interpolate between two points
function interpolatePosition(start, end, t) {
  return [
    start[0] + (end[0] - start[0]) * t,
    start[1] + (end[1] - start[1]) * t,
  ];
}

// animate the aircraft along the route
let segmentIndex = 0;
let t = 0;
const speed = 0.0003; // adjust speed as needed

function animateAircraft() {
  if (segmentIndex >= waypoints.length - 1) return; // stop at the last waypoint

  const start = waypoints[segmentIndex].coords;
  const end = waypoints[segmentIndex + 1].coords;

  // interpolate positions
  const newPosition = interpolatePosition(start, end, t);
  aircraftMarker.setLatLng(newPosition);

  // increment t and check if we reached the end of the segment
  t += speed;
  if (t >= 1) {
    t = 0; // reset t
    segmentIndex++;
  }

  // continue animation
  requestAnimationFrame(animateAircraft);
}

// start the animation
animateAircraft();
