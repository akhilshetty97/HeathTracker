from disease_tracker.scrapers.cdcscraper import CDCScraper
from disease_tracker.scrapers.whoscraper import WHOScraper
from disease_tracker.models import Disease

def collect_disease_data():
    # Create scraper instances
    cdc_scraper = CDCScraper()
    who_scraper = WHOScraper()

    try:
        # Get data from CDC
        usa_diseases = cdc_scraper.fetch_outbreaks()
        for disease in usa_diseases:
            Disease.objects.update_or_create(
                title=disease['title'],
                defaults={
                    'location': 'USA',
                    'is_usa': True
                }
            )

        # Get data from WHO
        global_diseases = who_scraper.fetch_who_diseases()
        for disease in global_diseases:
            Disease.objects.update_or_create(
                title=disease['title'],
                defaults={
                    'location': disease.get('region', 'Global'),
                    'is_usa': False
                }
            )

    finally:
        cdc_scraper.driver.quit()
        who_scraper.driver.quit()