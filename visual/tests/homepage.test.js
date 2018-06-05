load("init.js");
load("pages/homepage.js");

testOnAllDevices("homepage test", "/", function (driver, device) {
    new Homepage(driver).waitForIt();
    checkLayout(driver, "qa/visual/specs/homepage.gspec", device.tags);
});


testOnDevice($galen.devices.desktop, "Pretend we need to write this to be a device specific CTA test", "/", function (driver, device) {
    var welcomePage = new WelcomePage(driver).waitForIt();
    logged("Checking color for cta button", function () {
        checkLayout(driver, "qa/visual/specs/cta_buttons.gspec", ["usual"]);
    })

    logged("Checking color for highlighted cta button", function () {
        welcomePage.hoverCTA();
        checkLayout(driver, "qa/visual/specs/cta_buttons.gspec", ["hovered"]);
    });
});


// testOnAllDevices("homepage test using " + $galen.config.browser +" browser", "/", function (driver, device) {
//     new Homepage(driver).waitForIt();
//     checkLayout(driver, "qa/visual/specs/homepage.gspec", device.tags);
// });
//
//
// var devices = {
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
//
// var browsers = {
//   firefox: {
//     browserName: "Firefox"
//   },
//   chrome: {
//     browserName: "Chrome"
//   }
// };
//
// forAll(devices, function () {
//     forAll(browsers, function () {
//         test("Test on ", function (device, browser) {
//             new Homepage(driver).waitForIt();
//             checkLayout(driver, "qa/visual/specs/homepage.gspec", device.tags);
//         });
//     });
// });
//
//
//
