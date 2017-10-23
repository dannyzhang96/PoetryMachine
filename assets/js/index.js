var fs = require('fs');
var files = fs.readdirSync('/assets/collection/');
console.log(files[0])