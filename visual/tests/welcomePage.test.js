load("init.js");
load("pages/WelcomePage.js");

testOnAllDevices("Welcome page", "/", function (driver, device) {
    new WelcomePage(driver).waitForIt();
    checkLayout(driver, "qa/visual/specs/welcomePage.gspec", device.tags);
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
