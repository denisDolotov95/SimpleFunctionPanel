function showPass(pass_id, eye_id) {
    let input = $(`#${pass_id}`);
    if (input.attr("type") === "password") {
        input.attr("type", "text");
        $(`#${eye_id}`).html('<span class="glyphicon glyphicon-eye-open"></span>');
    } else {
        input.attr("type", "password");
        $(`#${eye_id}`).html('<span class="glyphicon glyphicon-eye-close"></span>');
    }
}
