const notificationSwall= (titleText, text, icon, confirmButtonText) => {
    Swal.fire({
        titleText: titleText,
        text: text,
        icon: icon, //waring, success, error, info
        confirmButtonText: confirmButtonText
    });
}