load("init.js");
load("pages/homepage.js");

// testOnAllDevices("homepage test", "/", function (driver, device) {
//     new Homepage(driver).waitForIt();
//     checkLayout(driver, "qa/visual/specs/homepage.gspec", device.tags);
// });
//
//
// testOnDevice($galen.devices.desktop, "Pretend we need to write this to be a device specific CTA test", "/", function (driver, device) {
//     var homepage = new Homepage(driver).waitForIt();
//     logged("Checking color for cta button", function () {
//         checkLayout(driver, "qa/visual/specs/cta_buttons.gspec", ["usual"]);
//     })
//
//     logged("Checking color for highlighted cta button", function () {
//         homepage.hoverCTA();
//         checkLayout(driver, "qa/visual/specs/cta_buttons.gspec", ["hovered"]);
//     });
// });

// testOnAllDevices("homepage test using " + $galen.config.browser +" browser", "/", function (driver, device) {
//     new Homepage(driver).waitForIt();
//     checkLayout(driver, "qa/visual/specs/homepage.gspec", device.tags);
// });
//


// An example of http://galenframework.com/docs/reference-javascript-tests-guide/#Multilevelparameterization with browser
// forAll($galen.devices, function () {
//     forAll($galen.browsers, function () {
//         test("Test on ${deviceName} for ${browserName}", function (device, browser) {
//             System.out.println("Testing on  "+ device.deviceName);
//             System.out.println("with a size of " + device.size + ". How to debug on command line should be in JS docs");
//             var driver = createDriver($galen.settings.website + "", device.size, browser.browserName);
//             // var driver = device.initDriver($galen.settings.website + "");
//             new Homepage(driver).waitForIt();
//             checkLayout(driver, "qa/visual/specs/homepage.gspec", browser.browserName);
//             driver.quit()
//         });
//     });
// });

// Switches browser using DRIVER=browsername
forAll($galen.devices, function (device) {
    test("Homepage on ${deviceName} device in " + $galen.settings.current_browser + " browser", function (device) {
        var driver = createDriver($galen.settings.website + "", device.size, $galen.settings.current_browser);
        new Homepage(driver).waitForIt();
        checkLayout(driver, "qa/visual/specs/homepage.gspec", [device.deviceName, $galen.settings.current_browser]);
        driver.quit()
    });
});