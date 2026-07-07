document.getElementById('telemetry-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    // Gather inputs from the webpage form fields
    const planetPayload = {
        distance: document.getElementById('distance').value,
        mass: document.getElementById('mass').value,
        luminosity: document.getElementById('luminosity').value,
        greenhouse: document.getElementById('greenhouse').value
    };

    try {
        // Send a POST request containing JSON data back to our Flask app
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(planetPayload)
        });

        const result = await response.json();

        if (response.ok) {
            // Unhide presentation view layers
            document.getElementById('welcome-message').classList.add('hidden');
            document.getElementById('results-display').classList.remove('hidden');

            // Manage the text status configuration
            const badge = document.getElementById('status-badge');
            badge.innerText = result.status;
            
            // Alter visual styling metrics based on the specific classification index
            if (result.class === 1) {
                badge.className = "badge habitable";
            } else {
                badge.className = "badge hostile";
            }

            // Update progress bar width animation and percentage text dynamically
            document.getElementById('probability-bar').style.width = `${result.probability}%`;
            document.getElementById('probability-text').innerText = `${result.probability.toFixed(2)}%`;
        } else {
            alert("Error running inference: " + result.error);
        }
    } catch (err) {
        console.error("Transmission breakdown: ", err);
    }
});