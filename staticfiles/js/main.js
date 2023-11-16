// Contenu de main.js

$(document).ready(function() {
    var table = $('#dataTableExample4').DataTable({
        "order": [],
    });
});

$(document).ready(function () {
    // Clique sur le bouton pour réduire le menu latéral
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#content').toggleClass('active');
    });
    // Clique sur le bouton "Plus" pour afficher le menu de navigation
    $('.more-button,.body-overlay').on('click', function () {
        $('#sidebar,.body-overlay').toggleClass('show-nav');
    });
});

