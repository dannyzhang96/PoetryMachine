$(document).ready(
    function generatePoem() {
        var poemID = Math.floor(Math.random() * 12529)
        var request = new XMLHttpRequest();
        request.open("GET", "assets/collection/" + poemID + ".json", false);
        request.send(null)
        var my_JSON_object = JSON.parse(request.responseText);
        $('#poemTitle').html(my_JSON_object.title);
        $('#poemAuthor').html("by " + my_JSON_object.author);
        var poemText = ''
        for (i = 0; i < my_JSON_object.text.length; i ++) {
            poemText += my_JSON_object.text[i] + "<br/>"
        }
        $('#poemText').html(poemText);
});


