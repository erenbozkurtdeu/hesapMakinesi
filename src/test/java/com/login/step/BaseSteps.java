package com.login.step;

import com.login.base.BaseTest;
import com.login.model.ElementInfo;
import com.thoughtworks.gauge.Step;
import org.openqa.selenium.*;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

public class BaseSteps extends BaseTest {

    public BaseSteps() {
        initMap(getFileList());
    }

    WebElement findElement(String key) {
        By infoParam = getElementInfoToBy(findElementInfoByKey(key));
        WebDriverWait webDriverWait = new WebDriverWait(driver, Duration.ofSeconds(5));
        WebElement webElement = webDriverWait
                .until(ExpectedConditions.presenceOfElementLocated(infoParam));
        ((JavascriptExecutor) driver).executeScript(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})",
                webElement);
        return webElement;
    }

    public By getElementInfoToBy(ElementInfo elementInfo) {
        By by = null;
        if (elementInfo.getType().equals("css")) {
            by = By.cssSelector(elementInfo.getValue());
        } else if (elementInfo.getType().equals("id")) {
            by = By.id(elementInfo.getValue());
        } else if (elementInfo.getType().equals("xpath")) {
            by = By.xpath(elementInfo.getValue());
        }
        return by;
    }

    private void clickElement(WebElement element) {
        element.click();
    }

    @Step("<int> saniye bekle")
    public void waitBySeconds(int seconds) {
        try {
            logger.info(seconds + " saniye bekleniyor.");
            Thread.sleep(seconds * 1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    @Step("Elementine tıkla <key>")
    public void clickElement(String key) {
        if (!key.isEmpty()) {
            clickElement(findElement(key));
            logger.info(key + " elementine tıklandı.");
        }
    }

    @Step("<text> textini <key> elemente yaz")
    public void sendKeys(String text, String key) {
        if (!key.equals("")) {
            findElement(key).sendKeys(text);
            logger.info(key + " elementine " + text + " texti yazıldı.");
        }
    }

    @Step({"<key> elementi <text> değerini içeriyor mu kontrol et"})
    public void checkElementContainsText(String key, String text) {
        System.out.print(findElement(key).getText());
        Boolean containsText = findElement(key).getText().contains(text);
        System.out.print(containsText);
        logger.info("Alınan text değeri" + containsText);
        assertTrue(containsText, "Expected text is not contained");
        logger.info(key + " elementi " + text + " değerini içeriyor.");
    }

    @Step({"<key> elementi <text> değerine eşit mi kontrol et"})
    public void checkElementEqualText(String key, String text) {
        System.out.print(findElement(key).getText());
        Boolean containsText = findElement(key).getText().equals(text);
        System.out.print(containsText);
        logger.info("Alınan text değeri" + containsText);
        assertTrue(containsText, "Expected text is not contained");
        logger.info(key + " elementi " + text + " değerini içeriyor.");
    }
}