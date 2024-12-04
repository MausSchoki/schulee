document.addEventListener("DOMContentLoaded", () => {
    const apiUrl = "http://127.0.0.1:5000/api/schueler";
    const container = document.querySelector(".container");

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const schuelerList = document.createElement("ul");
            data.forEach(schueler => {
                const item = document.createElement("li");
                item.textContent = `${schueler.name} (${schueler.klasse})`;
                schuelerList.appendChild(item);
            });
            container.appendChild(schuelerList);
        })
        .catch(error => console.error("Fehler beim Laden der Schülerdaten:", error));
});
