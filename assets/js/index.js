$(document).ready(
    function generatePoem() {
        var poemID = Math.floor(Math.random() * 12529)
        var request = new XMLHttpRequest();
        request.open("GET", "assets/collection/" + poemID + ".json", false);
        request.send(null)
        var my_JSON_object = JSON.parse(request.responseText);
        $('#poemTitle').html(my_JSON_object.title);
        $('#poemAuthor').html(my_JSON_object.author);
        for (i = 0; i < my_JSON_object.text.length; i ++) {
            $('#poemText').append('<p>' + my_JSON_object.text[i] + '</p>');
        }
});


