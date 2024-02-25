$(document).ready(function () {
    // Apply platform color to body
    if ($('.pd-container').length > 0) {
        let platformColor = $('.pd-container').data('platformcolor');
        let platformFontColor = $('.pd-container').data('platformfontcolor');
        $('body').css({
            'background-color': platformColor,
            'color': platformFontColor
        });
    }

    $('.platform-button').each(function () {
        let boxColor = $(this).data('boxcolor');
        let fontColor = $(this).data('fontcolor');
        $(this).css({
            'background-color': boxColor,
            'color': fontColor
        });
    });

    // Delete buttons on the library/index.html page
    if ($("#deleteModal").length > 0) {
        const deleteModal = new bootstrap.Modal($("#deleteModal")[0]);
        const deleteButtons = $(".btn-delete");
        deleteButtons.on("click", function () {
            deleteModal.show();
        });
    }

    // Delete button for game delete
    if ($("#deleteGameModal").length > 0) {
        const deleteGameModal = new bootstrap.Modal($("#deleteGameModal")[0]);
        const deleteGameButton = $("#deleteGameButton");
        deleteGameButton.on("click", function () {
            deleteGameModal.show();
        });
    }

    // Delete button for wishlist game delete
    if ($("#deleteWishListGameModal").length > 0) {
        const deleteWishListGameModal = new bootstrap.Modal($("#deleteWishListGameModal")[0]);
        const deleteWishListGameButton = $("#deleteWishListGameButton");
        deleteWishListGameButton.on("click", function () {
            deleteWishListGameModal.show();
        });
    }
});
