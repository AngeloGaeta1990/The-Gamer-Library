$(document).ready(function () {
    $('.platform-button').each(function () {
        let boxColor = $(this).data('boxcolor');
        let fontColor = $(this).data('fontcolor')
        $(this).css('background-color', boxColor);
        $(this).css('color', fontColor);

         // Add click event handler for each platform button
        $(this).on('click', function () {
            // Toggle the visibility of the corresponding game menu
            let dropdownMenu = $(this).next('.dropdown-menu');
            dropdownMenu.toggle();
        });
    });

});