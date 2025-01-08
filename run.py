import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from disease_tracker.scrapers.cdcscraper import CDCScraper
from disease_tracker.scrapers.whoscraper import WHOScraper
from disease_tracker.models import Disease

def scrape_data():
    # Create scraper instances
    cdc_scraper = CDCScraper()
    who_scraper = WHOScraper()

    try:
        # Get data from CDC
        print("Scraping CDC data...")
        usa_diseases = cdc_scraper.fetch_outbreaks()
        for disease in usa_diseases:
            Disease.objects.update_or_create(
                title=disease['title'],
                defaults={
                    'location': 'USA',
                    'is_usa': True
                }
            )
        print(f"Found {len(usa_diseases)} USA diseases")

        # Get data from WHO
        print("\nScraping WHO data...")
        global_diseases = who_scraper.fetch_who_diseases()
        for disease in global_diseases:
            Disease.objects.update_or_create(
                title=disease['disease'],
                defaults={
                    'location': disease.get('region', 'Global'),
                    'is_usa': False
                }
            )
        print(f"Found {len(global_diseases)} global diseases")

    finally:
        cdc_scraper.driver.quit()
        who_scraper.driver.quit()

def view_data():
    print("\nCurrent diseases in database:")
    diseases = Disease.objects.all()
    for disease in diseases:
        print(f"- {disease.title} ({disease.location})")

if __name__ == "__main__":
    while True:
        print("\nDisease Tracker Menu:")
        print("1. Scrape new data")
        print("2. View current data")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            scrape_data()
        elif choice == '2':
            view_data()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")