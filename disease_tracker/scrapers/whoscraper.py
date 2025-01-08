from datetime import datetime
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WHOScraper:
    def __init__(self):
        # Base URL of the WHO international outbreaks page
        self.base_url = 'https://www.who.int/emergencies/disease-outbreak-news'

        # Setup Chrome options for Selenium WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run Chrome in headless mode (no UI)

        # Initialize the Chrome WebDriver with the specified options
        self.driver = webdriver.Chrome(options=options)
        
    def fetch_who_diseases(self):
        try:
            # First navigate to the WHO page
            self.driver.get(self.base_url)
            
            # Wait for page to load - let's wait longer and add some debugging
            wait = WebDriverWait(self.driver, 15)  # Increased wait time
            
            print("Waiting for page to load...")
            
            # First check if page loaded at all
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            print("Body tag found")
            
            # Wait for h4 tags to load
            h4_elements = wait.until(
                EC.presence_of_all_elements_located((By.TAG_NAME, "h4"))
            )
            
            # Store unique disease-region pairs
            disease_data = set()
            
            for h4 in h4_elements:
                try:
                    
                    # Check if h4 has the correct class
                    if 'sf-list-vertical__title' in h4.get_attribute('class'):
                        # Find span with class 'trimmed' inside h4
                        span = h4.find_element(By.CLASS_NAME, 'trimmed')
                        text = span.text.strip()
                        
                        if ' - ' in text:
                            parts = text.split(' - ', 1)
                            disease_name = parts[0].strip()
                            region = parts[1].strip()
                            disease_data.add((disease_name, region))
                            print(f"Found: {disease_name} in {region}")
                    
                except Exception as e:
                    print(f"Error processing h4 element: {e}")
                    continue
            
            # Convert to list of dictionaries
            unique_diseases = [
                {
                    'disease': disease,
                    'region': region
                }
                for disease, region in disease_data
            ]
            
            # print(f"Total diseases found: {len(unique_diseases)}")
            return unique_diseases
            
        except Exception as e:
            print(f"Error scraping WHO diseases: {e}")
            return []
        finally:
            # Don't close the driver here if you plan to use it again
            pass
