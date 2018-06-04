load("galen-bootstrap/galen-bootstrap.js");


var TEST_USER = {
    username: "testuser@example.com",
    password: "test123"
};

$galen.settings.website = "http://testapp.galenframework.com";
//$galen.settings.website = "http://localhost:8080";

$galen.registerDevice("mobile", inSingleBrowser("mobile emulation", "400x1080", ["mobile"]));
$galen.registerDevice("tablet", inSingleBrowser("tablet emulation", "640x1080", ["tablet"]));
$galen.registerDevice("desktop", inSingleBrowser("desktop emulation", "1024x1080", ["desktop"]));
$galen.registerDevice("large_desktop", inSingleBrowser("large desktop emulation", "1024x1080", ["large_desktop"]));

(function (export) {
    export.TEST_USER = TEST_USER;
})(this);
