from datetime import datetime
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CDCScraper:
    def __init__(self):
        # Base URL of the CDC outbreaks page
        self.base_url = 'https://www.cdc.gov/outbreaks'

        # Setup Chrome options for Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode (no UI)

        # Initialize the Chrome WebDriver with the specified options
        self.driver = webdriver.Chrome(options=options)
        
    def fetch_outbreaks(self):
        try:
            # Navigate to the CDC outbreaks page
            self.driver.get(f'{self.base_url}/index.html')
            
            # Wait for the feed container to load
            wait = WebDriverWait(self.driver, 10)
            
            # First find the "U.S. Outbreaks" heading
            us_outbreaks_heading = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'U.S. Outbreaks')]"))
            )
            
            # Find the parent container of the heading
            section_container = us_outbreaks_heading.find_element(By.XPATH, "./following-sibling::div[contains(@class, 'dfe-section__feed-items')]")
            
            # Find all feed items within this specific section
            feed_items = section_container.find_elements(By.CLASS_NAME, "dfe-block-feed-item")
            
            outbreaks = []
            for item in feed_items:
                try:
                    # Find the link element within each feed item
                    link_element = item.find_element(By.CLASS_NAME, "dfe-block-feed-item__link").find_element(By.TAG_NAME, "a")
                    
                    # Extract the URL and title
                    outbreak_url = link_element.get_attribute('href')
                    outbreak_title = link_element.text
                    
                    outbreak_info = {
                        'title': outbreak_title,
                        'url': outbreak_url
                    }
                    outbreaks.append(outbreak_info)
                    print(f"Found US outbreak: {outbreak_title}")  # Debug print
                    
                except Exception as e:
                    print(f"Error processing feed item: {e}")
                    continue
            
            return outbreaks
            
        except Exception as e:
            print(f"Error scraping CDC: {e}")
            return []
        
        finally:
            # Don't close the driver here if you plan to use it for subsequent requests
            pass