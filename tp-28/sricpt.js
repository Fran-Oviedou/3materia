document.addEventListener("DOMContentLoaded", function() {
    let imagenes = document.querySelectorAll("#imagenes img");
    imagenes.forEach(img => {
        img.addEventListener("click", function() {
            alert("terrible fotarda");
        });
    });
});
