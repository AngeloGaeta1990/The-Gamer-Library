$(document).ready(function () {
    // Check if we are on the platform_detail.html page
    if ($('.pd-container').length > 0) {
        // Get platform color attributes
        let platformColor = $('.pd-container').data('platformcolor');
        let platformFontColor = $('.pd-container').data('platformfontcolor');

        // Apply platform color to body
        $('body').css('background-color', platformColor);
        $('body').css('color', platformFontColor);
        // Apply styles to other elements as needed
        // ...
    }

    // Expand buttons on the library/index.html page
    
    // Apply styles to platform buttons on the library/index.html page
    $('.platform-button').each(function () {
        let boxColor = $(this).data('boxcolor');
        let fontColor = $(this).data('fontcolor');
        $(this).css('background-color', boxColor);
        $(this).css('color', fontColor);
    });

    // Delete buttons on the library/index.html page
    const deleteModal = new bootstrap.Modal($("#deleteModal")[0]);
    const deleteButtons = $(".btn-delete");
    const deleteConfirm = $("#deleteConfirm");

    deleteButtons.on("click", function (e) {
        console.log("Button clicked");
        let platformId = $(this).data("platformid");
        console.log("Platform:Id", platformId);
        deleteConfirm.attr("href", `delete_platform/${platformId}`);
        deleteModal.show();
    });

    // // Toggle visibility of game details box
    // $('.btn-primary').on('click', function () {
    //     var collapse = $(this).siblings('.collapse');
    //     collapse.collapse('toggle');
    // });
});
