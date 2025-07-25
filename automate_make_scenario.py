from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ======= CONFIG =======
EMAIL = "burnerac1236@gmail.com"     # <== Change this
PASSWORD = "Mmcc@1212"           # <== Change this
driver_path = "msedgedriver.exe"     # Make sure it's in your folder

# ======= EDGE SETUP =======
options = Options()
options.use_chromium = True
options.add_argument("start-maximized")

service = Service(r"C:\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=service, options=options)

try:
    # 1. Open Make.com home
    driver.get("https://www.make.com/en")
    time.sleep(5)

    wait = WebDriverWait(driver, 20)

    # 2. Accept Cookies if shown
    try:
        accept_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Understood')]")))
        accept_btn.click()
        print("✅ Accepted cookies")
        # Wait for the cookie popup to disappear
        wait.until(EC.invisibility_of_element_located((By.XPATH, "//button[contains(text(), 'Understood')]")))
    except Exception as e:
        print("⚠️ No cookie popup found or error:", e)

    # 3. Go directly to login page
    driver.get("https://www.make.com/en/login")
    print("✅ Navigated directly to login page")
    time.sleep(3)

    # 4. Enter login details and sign in (robust, custom element aware)
    # Email field
    email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "imt-input-email input[name='email']")))
    email_input.click()
    email_input.send_keys(EMAIL)
    print("✅ Email entered")
    time.sleep(0.5)

    # Password field
    password_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "imt-input-password input[name='password']")))
    password_input.click()
    password_input.send_keys(PASSWORD)
    print("✅ Password entered")
    time.sleep(0.5)

    # Click the Sign in button
    sign_in_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Sign in')]")))
    sign_in_btn.click()
    print("✅ Clicked Sign in button")

    # Wait for login to complete (URL change)
    wait.until(lambda d: "login" not in d.current_url)
    print("✅ Login attempt complete, current URL:", driver.current_url)
    time.sleep(5)

    # After login, go to the scenarios page
    driver.get("https://eu2.make.com/2247680/scenarios?folder=all&tab=all&type=scenario")
    print("✅ Navigated to scenarios page")
    time.sleep(5)

    # Print the page source for debugging
    print(driver.page_source)

    wait = WebDriverWait(driver, 60)  # Increase timeout

    # Wait for skeletons to disappear
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".dmo-animate-skeleton")))
    print("✅ Loading skeletons gone, waiting for scenario list...")

    # Now wait for a scenario title to appear
    wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'scenarios-list-item__title')]")))
    print("✅ Scenario list loaded")

    # Use JavaScript to get scenario titles and ON/OFF states from shadow DOM
    scenarios_info = driver.execute_script("""
        let results = [];
        // Find all shadow roots in the document
        function findAllShadowRoots(node) {
            let roots = [];
            if (node.shadowRoot) roots.push(node.shadowRoot);
            for (let child of node.children) {
                roots = roots.concat(findAllShadowRoots(child));
            }
            return roots;
        }
        let roots = [document];
        roots = roots.concat(findAllShadowRoots(document));
        for (let root of roots) {
            let items = root.querySelectorAll('div.scenarios-list-item');
            for (let item of items) {
                let title = item.querySelector('.scenarios-list-item__title')?.innerText || '';
                let state = '';
                let switches = item.querySelectorAll('div');
                for (let sw of switches) {
                    if (sw.innerText === 'ON' || sw.innerText === 'OFF') state = sw.innerText;
                }
                results.push({title, state});
            }
        }
        return results;
    """)
    print("Scenarios found via JS:", scenarios_info)

    # Print all iframes and their src attributes for debugging
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"Found {len(iframes)} iframes.")
    for i, iframe in enumerate(iframes):
        print(f"{i}: src={iframe.get_attribute('src')}")

    # Print all scenario titles and their ON/OFF state for debugging
    scenarios = driver.find_elements(By.XPATH, "//div[contains(@class, 'scenarios-list-item')]")
    print(f"Found {len(scenarios)} scenario rows.")
    for i, row in enumerate(scenarios):
        try:
            title = row.find_element(By.XPATH, ".//div[contains(@class, 'scenarios-list-item__title')]").text
        except Exception:
            title = "N/A"
        try:
            state = row.find_element(By.XPATH, ".//div[text()='ON' or text()='OFF']").text
        except Exception:
            state = "N/A"
        print(f"{i}: Title='{title}', State='{state}'")

    # Click the title of the scenario that is ON
    scenario_on_title = wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//div[contains(@class, 'scenarios-list-item')][.//div[text()='ON']]//div[contains(@class, 'scenarios-list-item__title')]"
    )))
    scenario_on_title.click()
    print("✅ Clicked the ON scenario title")
    time.sleep(5)

    # 9. Click Edit button
    edit_button = driver.find_element(By.XPATH, "//button[@title='Edit']")
    edit_button.click()
    print("✅ Clicked Edit")
    time.sleep(5)

    # 10. Click Run Once button
    run_once = driver.find_element(By.XPATH, "//button[@title='Run once']")
    run_once.click()
    print("✅ Triggered Run Once")

    time.sleep(10)

except Exception as e:
    print("❌ Error:", str(e))

finally:
    input("Press Enter to exit...")
    driver.quit()
