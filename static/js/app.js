document.addEventListener("DOMContentLoaded", () => {
    const flightsTable = document.querySelector("#flights-table tbody");
    const radiusInput = document.querySelector("#radius");
    const refreshButton = document.querySelector("#refresh");

    // Fetch flights and render table
    async function fetchFlights() {
        const radius = radiusInput.value || 15;

        try {
            const response = await fetch(`/flights?radius=${radius}`);
            const flights = await response.json();

            flightsTable.innerHTML = "";

            if (flights.length === 0) {
                flightsTable.innerHTML = `
                    <tr><td colspan="7" class="no-flights">No flights found</td></tr>
                `;
                return;
            }

            flights.forEach(flight => {
                const row = document.createElement("tr");

                row.innerHTML = `
                    <td>${flight.callsign || "N/A"}</td>
                    <td>${flight.registration || "Unknown"}</td>
                    <td>${flight.type || "Unknown"}</td>
                    <td>${flight.altitude_ft ?? "N/A"}</td>
                    <td>${flight.gs ?? "N/A"}</td>
                    <td>${flight.lat ?? "N/A"}</td>
                    <td>${flight.lon ?? "N/A"}</td>
                `;

                // When clicked, show full metadata
                row.addEventListener("click", () => showFlightDetails(flight));

                flightsTable.appendChild(row);
            });
        } catch (error) {
            console.error("Error fetching flights:", error);
        }
    }

    // Show a popup with full metadata
    function showFlightDetails(flight) {
        const prettyData = JSON.stringify(flight, null, 2);
        const popup = window.open("", "_blank", "width=500,height=700,scrollbars=yes");
        popup.document.write(`
            <html>
                <head>
                    <title>Flight Details</title>
                    <style>
                        body { font-family: monospace; padding: 10px; background: #f4f4f4; }
                        pre { white-space: pre-wrap; word-wrap: break-word; }
                    </style>
                </head>
                <body>
                    <h2>Flight Metadata</h2>
                    <pre>${prettyData}</pre>
                </body>
            </html>
        `);
    }

    // Refresh button click
    refreshButton.addEventListener("click", fetchFlights);

    // Initial fetch
    fetchFlights();
});