import os
import time
import random
import undetected_chromedriver as uc

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def load_search_terms(filename="search_terms.txt"):
    """
    Load search terms (one per line) from a text file, ignoring blank lines.
    Returns a list of lowercase terms.
    """
    terms = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                term = line.strip().lower()
                if term:
                    terms.append(term)
    return terms


def build_poke_back_xpath(search_terms):
    """
    Dynamically build an XPath that checks for any occurrence of the
    given terms in a case-insensitive manner within the @aria-label attribute.
    """
    xpath_clauses = []
    for term in search_terms:
        clause = (
            "contains(translate(@aria-label, "
            "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), "
            f"'{term}')"
        )
        xpath_clauses.append(clause)
    joined_clauses = " or ".join(xpath_clauses)
    return f"//div[{joined_clauses}]"


def click_random_position(driver, element):
    """
    Click a random position within the given element's bounding box
    via a small JavaScript snippet.
    """
    driver.execute_script(
        """
        const rect = arguments[0].getBoundingClientRect();
        const randomX = Math.floor(Math.random() * rect.width) + rect.left;
        const randomY = Math.floor(Math.random() * rect.height) + rect.top;
        const el = document.elementFromPoint(randomX, randomY);
        if (el) el.click();
        """,
        element
    )


def main():
    # Step 1: Load search terms from file
    search_terms = load_search_terms("search_terms.txt")
    if not search_terms:
        print("[!] No search terms found in 'search_terms.txt'.")
        print("    Please add terms (e.g. 'poke', 'vissza', 'bök') to that file.")
        return

    # Build dynamic XPath from those terms
    poke_back_xpath = build_poke_back_xpath(search_terms)

    # Step 2: Initialize undetected Chrome (no headless mode)
    options = uc.ChromeOptions()
    # Make sure we're not adding --headless anywhere
    # options.add_argument("--headless")  # Not used by request

    driver = uc.Chrome(options=options, use_subprocess=True)
    wait = WebDriverWait(driver, 10)

    try:
        # Step 3: Navigate to Facebook and wait for login
        print("[+] Opening Facebook login page...")
        driver.get("https://www.facebook.com")
        input("    Please log in manually, then press ENTER to continue... ")

        # Step 4: Navigate to Facebook Pokes page
        print("[+] Navigating to the Facebook Pokes page...")
        driver.get("https://www.facebook.com/pokes")
        time.sleep(random.uniform(3, 6))

        print("[+] Starting continuous poke-back process. Press Ctrl + C to stop.")
        while True:
            # Scroll randomly to mimic human browsing
            for _ in range(random.randint(1, 3)):
                scroll_distance = random.randint(-800, 800)
                driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
                time.sleep(random.uniform(0.5, 1.5))

            # Attempt to find "Poke Back" elements via the dynamic XPath
            print(f"[?] Searching for elements matching:\n    {poke_back_xpath}")

            try:
                wait.until(EC.presence_of_element_located((By.XPATH, poke_back_xpath)))
            except:
                print("[!] No matching elements found right now. Checking again soon.")
                time.sleep(random.randint(30, 60))
                continue

            all_elements = driver.find_elements(By.XPATH, poke_back_xpath)
            
            # Filter out elements that may not truly match or aren't clickable
            poke_elements = []
            for elem in all_elements:
                # Check if element is visible and enabled
                if not elem.is_displayed():
                    continue
                if not elem.is_enabled():
                    continue

                # Double-check the aria-label matches any of the search terms
                aria_label = (elem.get_attribute("aria-label") or "").lower()
                if any(term in aria_label for term in search_terms):
                    poke_elements.append(elem)

            print(f"[+] Found {len(poke_elements)} matching elements after filtering.")

            # Scroll to each element, wait, then do a random click
            for element in poke_elements:
                try:
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                    time.sleep(random.uniform(0.5, 1.0))

                    wait.until(EC.element_to_be_clickable(element))
                    click_random_position(driver, element)
                    time.sleep(random.uniform(1.0, 2.0))
                except Exception as exc:
                    print(f"[!] Error clicking element: {exc}")

            # Wait a random time before next iteration
            wait_time = random.randint(60, 120)
            print(f"[+] Cycle complete. Waiting {wait_time} seconds before next check...")
            time.sleep(wait_time)

    except KeyboardInterrupt:
        print("\n[!] Process interrupted by user.")
    finally:
        print("[+] Closing the browser...")
        driver.quit()
        print("[+] Browser closed.")


if __name__ == "__main__":
    main()
