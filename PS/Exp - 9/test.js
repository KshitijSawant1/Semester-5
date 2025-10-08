const { Builder, By, until } = require("selenium-webdriver");
const chrome = require("selenium-webdriver/chrome");
const assert = require("node:assert/strict");
const path = require("node:path");

// Choose ONE mode below:

// A) Headless (modern; recommended for CI)
const options = new chrome.Options().addArguments(
  "--headless=new",
  "--disable-gpu",
  "--no-sandbox",
  "--disable-dev-shm-usage"
);

// B) Visible browser (for debugging)
// const options = new chrome.Options();

async function openApp(driver) {
  const fileUrl = "file://" + path.resolve("index.html");
  await driver.get(fileUrl);
  await driver.wait(
    until.elementLocated(By.css('[data-testid="title"]')),
    2000
  );
}

async function testGreeting(driver, name, expected, expectError = false) {
  const nameInput = await driver.findElement(
    By.css('[data-testid="name-input"]')
  );
  const button = await driver.findElement(
    By.css('[data-testid="greet-button"]')
  );
  const greeting = await driver.findElement(By.css('[data-testid="greeting"]'));
  const error = await driver.findElement(By.css('[data-testid="error"]'));

  await nameInput.clear();
  if (name !== null) await nameInput.sendKeys(name);
  await button.click();

  // Wait until either greeting or error has text
  await driver.wait(async () => {
    const [g, e] = await Promise.all([greeting.getText(), error.getText()]);
    return g.length > 0 || e.length > 0;
  }, 2000);

  const greetingText = await greeting.getText();
  const errorText = await error.getText();

  if (expectError) {
    assert.ok(
      errorText.includes("Please enter your name."),
      `Expected validation error, got: "${errorText}"`
    );
    assert.equal(
      greetingText,
      "",
      "Greeting should be empty on validation error"
    );
  } else {
    assert.equal(
      greetingText,
      expected,
      `Greeting mismatch. Got: "${greetingText}"`
    );
    assert.equal(errorText, "", "Error should be empty on success");
  }
}

(async function run() {
  const driver = await new Builder()
    .forBrowser("chrome")
    .setChromeOptions(options)
    .build();

  try {
    await openApp(driver);

    await testGreeting(driver, "Alice", "Hello, Alice!");
    await testGreeting(driver, "  Bob  ", "Hello, Bob!"); // trims whitespace
    await testGreeting(driver, "", "", true); // empty -> validation
    await testGreeting(driver, "नमस्ते", "Hello, नमस्ते!"); // Unicode

    console.log("✅ All tests passed!");
  } catch (err) {
    console.error("❌ Test run failed:", err);
    process.exitCode = 1;
  } finally {
    await driver.quit();
  }
})();
