load("galen-bootstrap/galen-bootstrap.js");

// Java ENV variables to work with runner
var domain = System.getenv("BASE_URL") || "http://testapp.galenframework.com";
// var domain = "http://testapp.galenframework.com";

var TEST_USER = {
    username: "testuser@example.com",
    password: "test123"
};

$galen.settings.website = domain;
//$galen.settings.website = "http://localhost:8080";

$galen.registerDevice("mobile", inSingleBrowser("mobile emulation", "400x1080", ["mobile"]));
$galen.registerDevice("tablet", inSingleBrowser("tablet emulation", "640x1080", ["tablet"]));
$galen.registerDevice("desktop", inSingleBrowser("desktop emulation", "1024x1080", ["desktop"]));
$galen.registerDevice("large_desktop", inSingleBrowser("large desktop emulation", "1024x1080", ["large_desktop"]));

// this.browsers = {
//   firefox: {
//     browserName: "Firefox"
//   },
//   chrome: {
//     browserName: "Chrome"
//   }
// };
// this.devices = {
//   mobile: {
//     deviceName: "mobile",
//     size: "400x700"
//   },
//   tablet: {
//     deviceName: "tablet",
//     size: "600x800"
//   },
//   desktop: {
//     deviceName: "desktop",
//     size: "1024x768"
//   }
// };


(function (export) {
    export.TEST_USER = TEST_USER;
})(this);
