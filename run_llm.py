import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings') 
django.setup()


from disease_tracker.services.llm_service import DiseaseAnalyzer

# Use DiseaseAnalyzer
analyzer = DiseaseAnalyzer()
result = analyzer.get_disease_analysis("Cucumbers - Salmonella Outbreak")
print(result)
