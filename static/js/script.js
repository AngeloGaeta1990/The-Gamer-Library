$(document).ready(function () {
    // Check if we are on the platform_detail.html page
    if ($('.pd-container').length > 0) {
        // Get platform color attributes
        let platformColor = $('.pd-container').data('platformcolor');
        let platformFontColor = $('.pd-container').data('platformfontcolor');

        // Apply platform color to body
        $('body').css('background-color', platformColor);
        $('body').css('color', platformFontColor);
    }
        // Apply styles to other elements as needed
        // ...

    $('.platform-button').each(function () {
        let boxColor = $(this).data('boxcolor');
        let fontColor = $(this).data('fontcolor');
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

$(document).ready(function () {
    const submitButton = $("#submitButton");
    const deleteModal = new bootstrap.Modal($("#deleteModal")[0]);
    const deleteButtons = $(".btn-delete");
    const deleteConfirm = $("#deleteConfirm");

    deleteButtons.on("click", function (e) {
        console.log("Button clicked")
        let platformId = $(this).data("platformid");
        console.log("Platform:Id", platformId)
        deleteConfirm.attr("href", `delete_platform/${platformId}`);
        deleteModal.show();
    });
});