load("init.js");
load("pages/WelcomePage.js");

testOnAllDevices("Welcome page", "/", function (driver, device) {
    new WelcomePage(driver).waitForIt();
    checkLayout(driver, "qa/visual/specs/welcomePage.gspec", device.tags);
});


// 
// testOnDevice($galen.devices.desktop, "Menu Highlight", "/", function (driver, device) {
//     var welcomePage = new WelcomePage(driver).waitForIt();
//     logged("Checking color for menu item", function () {
//         checkLayout(driver, "qa/visual/specs/menuHighlight.gspec", ["usual"]);
//     })
//
//     logged("Checking color for highlighted menu item", function () {
//         welcomePage.hoverFirstMenuItem();
//         checkLayout(driver, "qa/visual/specs/menuHighlight.gspec", ["hovered"]);
//     });
// });
