document.addEventListener("DOMContentLoaded", function() {
    var h5Element = document.querySelector(".card-title");

    h5Element.addEventListener("mouseenter", function() {
        var linkElement = h5Element.querySelector("a");
        linkElement.style.color = "blue"; // Altera a cor do link para azul
    });

    h5Element.addEventListener("mouseleave", function() {
        var linkElement = h5Element.querySelector("a");
        linkElement.style.color = "black"; // Altera a cor do link de volta para preto
    });
});
