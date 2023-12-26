$(document).ready(function () {
    $('.platform-button').each(function () {
        let boxColor = $(this).data('boxcolor');
        let fontColor = $(this).data('fontcolor')
        $(this).css('background-color', boxColor);
        $(this).css('color', fontColor);
    });

});