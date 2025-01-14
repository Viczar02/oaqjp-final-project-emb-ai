let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value.trim();
    const systemResponseDiv = document.getElementById("system_response");

    // Limpiar la respuesta previa
    systemResponseDiv.innerHTML = "";

    // Manejar entrada vacía
    if (!textToAnalyze) {
        systemResponseDiv.innerHTML = `<p style="color: red;">¡Texto inválido! ¡Por favor, inténtalo de nuevo!</p>`;
        return;
    }

    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                systemResponseDiv.innerHTML = `<p style="color: green;">${xhttp.responseText}</p>`;
            } else if (this.status == 400) {
                systemResponseDiv.innerHTML = `<p style="color: red;">¡Texto inválido! ¡Por favor, inténtalo de nuevo!</p>`;
            } else {
                systemResponseDiv.innerHTML = `<p style="color: red;">Ocurrió un error inesperado. Inténtalo de nuevo.</p>`;
            }
        }
    };

    xhttp.open("GET", `emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`, true);
    xhttp.send();
};

