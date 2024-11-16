// Coordinates
const gaoCoords = [16.2484, -0.0056]; // Gao
const ildadCoords = [17.21444, 0.21583]; // ILDAD

const radiusNM = 60; // Gao airspace limits in Nautical Miles
const radiusKM = radiusNM * 1.8512; // Convert to kilometers
const waypoints = [
  { name: "ILDAD", coords: [17.21444, 0.21583] }, // ILDAD
  { name: "ERGIL", coords: [15.45139, 0.61861] }, // ERGIL
  { name: "ETRUL", coords: [15.8425, -0.98111] }, // ETRUL
  //   { name: "G", coords: gaoCoords },
  //   //   { name: "A", coords: [15.8, -1.8] },
  //   { name: "B", coords: [15.0, -3.8] },
  //   { name: "C", coords: [14.2, -5.2] },
  //   { name: "D", coords: [13.5, -6.5] },
  //   { name: "S", coords: bamakoCoords },
];

// Initialize the map, centered on Gao
const map = L.map("map").setView(gaoCoords, 8);

// Add OpenStreetMap tiles
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

// Add marker for Gao
L.marker(gaoCoords).addTo(map).bindPopup("Gao (GAQ)").openPopup();

// Add marker for ILDAD
L.marker(ildadCoords).addTo(map).bindPopup("ILDAD").openPopup();

// Draw the polyline for the route from Gao to ILDAD
const flightRoute = L.polyline([gaoCoords, ildadCoords], {
  color: "blue",
  weight: 3,
  opacity: 0.8,
}).addTo(map);

// Fit map bounds to include Gao and ILDAD
map.fitBounds(flightRoute.getBounds());

waypoints.forEach((point) => {
  // Add marker for the waypoint
  L.marker(point.coords).addTo(map).bindPopup(`${point.name}`).openPopup();

  // Draw polyline from Gao to the waypoint
  const route = L.polyline([gaoCoords, point.coords], {
    color: "blue",
    weight: 3,
    opacity: 0.8,
    dashArray: "5, 5", // Dashed line style
  }).addTo(map);
});

/* SIMULATE THE AIRCRAFT MOVEMENT */
// Aircraft icon
const aircraftIcon = L.icon({
  iconUrl: "https://cdn-icons-png.flaticon.com/512/854/854894.png", // Online aircraft icon
  iconSize: [30, 30], // Size of the icon
});

// Add the aircraft marker (initially at Gao)
const aircraftMarker = L.marker(gaoCoords, { icon: aircraftIcon }).addTo(map);

// Function to interpolate positions
function interpolatePosition(start, end, t) {
  return [
    start[0] + t * (end[0] - start[0]),
    start[1] + t * (end[1] - start[1]),
  ];
}

// Animate the aircraft along the route
let t = 0; // Initial progress (0%)
const speed = 0.001; // Speed of movement (adjust as needed)

function animateAircraft() {
  if (t > 1) {
    console.log("Simulation complete: Aircraft reached ILDAD.");
    return; // Stop animation when reaching the end
  }

  // Calculate the new position
  const newPosition = interpolatePosition(gaoCoords, ildadCoords, t);
  aircraftMarker.setLatLng(newPosition); // Update aircraft position

  t += speed; // Increment progress
  requestAnimationFrame(animateAircraft); // Continue the animation
}

// Start the simulation
animateAircraft();
