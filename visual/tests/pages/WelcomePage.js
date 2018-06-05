importClass(org.openqa.selenium.interactions.Actions);

this.WelcomePage = $page("Welcome page", {
    loginButton: "#welcome-page .button-login",

    hoverCTA: loggedFunction ("Hover over Login CTA", function (){
        var actions = new Actions(this.driver);
        actions.moveToElement(this.findChild("xpath: //*[@id='welcome-page']//button")).perform();
    })
});
