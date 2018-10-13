importClass(org.openqa.selenium.interactions.Actions);
importClass(org.openqa.selenium.support.ui.Wait);
importClass(org.openqa.selenium.support.ui.ExpectedConditions);
importClass(org.openqa.selenium.By);
importClass(org.openqa.selenium.WebElement);
importClass(org.openqa.selenium.NoSuchElementException);
importClass(org.openqa.selenium.support.ui.FluentWait);


this.News = $page("News page", {
    pageRoot: "div.news-layout",
}, {
    // Declaring secondary fields so they are not used in 'waitForIt' function
    clickTwoColumnButton: loggedFunction("Click Two Column Button", function () {
        var actions = new Actions(this.driver);
        actions.moveToElement(this.findChild('xpath: (//button[contains(@class, "view-mode")])[2]')).click().perform();
        var wait = new Wait(this.driver, 10)
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath('(//div[contains(@class, "news-page-column__list")])[2]')))
    }),

    clickThreeColumnButton: loggedFunction("Click Three Column Button", function () {
        var actions = new Actions(this.driver);
        actions.moveToElement(this.findChild('xpath: (//button[contains(@class, "view-mode")])[3]')).click().perform();
        var wait = new Wait(this.driver, 10)
        wait.until(ExpectedConditions.visibilityOfElementLocated(By.xpath('(//div[contains(@class, "news-page-column__list")])[3]')))
    })

});
