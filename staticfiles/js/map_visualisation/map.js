// Initialize the map
const map = L.map("map").setView([0, 0], 2);

// Add tile layer
L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
  attribution:
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

// Example airports
const airports = [
  { name: "JFK Airport", coords: [40.6413, -73.7781] },
  { name: "LAX Airport", coords: [33.9416, -118.4085] },
];

// Add markers
airports.forEach((airport) => {
  L.marker(airport.coords).addTo(map).bindPopup(`<b>${airport.name}</b>`);
});

// Example route
const route = [
  [40.6413, -73.7781],
  [33.9416, -118.4085],
];

// Add polyline for route
L.polyline(route, { color: "blue" }).addTo(map);

// Fit the map to the route
map.fitBounds(route);
