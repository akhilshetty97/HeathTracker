from openai import OpenAI
from disease_tracker.models import Disease
import environ
from django.conf import settings

env = environ.Env()
environ.Env.read_env()

OPENAI_API_KEY = env("OPENAI_API_KEY")

class DiseaseAnalyzer:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def get_disease_analysis(self, disease_title):
        """Get detailed analysis for a specific disease"""
        prompt = f"""
        Analyze this disease: {disease_title}
        
        Provide a comprehensive analysis in the following format:
        
        1. Disease Overview:
           - Brief description
           - Common symptoms
           - Typical incubation period
           - Transmission methods
        
        2. Risk Assessment:
           - Severity level
           - Most vulnerable populations
           - Environmental factors affecting spread
        
        3. Prevention Guidelines:
           - Personal protection measures
           - Community-level precautions
           - Vaccination information (if applicable)
        
        4. Treatment Approach:
           - First response steps
           - When to seek medical attention
           - Common treatment methods
        
        Present the information in a clear, factual manner suitable for public health awareness.
        """
        return self._get_completion(prompt)

    def analyze_regional_impact(self, region):
        """Analyze disease impact for a specific region"""
        diseases = Disease.objects.filter(location=region)
        
        prompt = f"""
        Analyze the disease situation in {region} with these active outbreaks:
        {[d.title for d in diseases]}
        
        Provide analysis in this structure:

        1. Current Situation:
           - Most concerning outbreaks
           - Population segments at highest risk
           - Current spread patterns
        
        2. Regional Factors:
           - Local healthcare capacity
           - Environmental/seasonal influences
           - Social/cultural factors affecting spread
        
        3. Action Plan:
           - Immediate precautions needed
           - Long-term preventive measures
           - Community preparation recommendations
        
        4. Travel Advisory:
           - Current risk level for travelers
           - Specific precautions for visitors
           - Required/recommended vaccinations
        """
        return self._get_completion(prompt)

    def get_global_health_assessment(self):
        """Global assessment of all tracked diseases"""
        diseases = Disease.objects.all()
        usa_outbreaks = [d.title for d in diseases if d.is_usa]
        global_outbreaks = [f"{d.title} in {d.location}" for d in diseases if not d.is_usa]
        
        prompt = f"""
        Analyze current global disease patterns:
        USA Outbreaks: {usa_outbreaks}
        Global Outbreaks: {global_outbreaks}
        
        Provide a comprehensive global health assessment:

        1. Pattern Analysis:
           - Major outbreak clusters
           - Cross-border transmission patterns
           - Emerging disease trends
        
        2. Global Impact Assessment:
           - Most affected regions
           - Economic/social implications
           - Healthcare system impacts
        
        3. International Response:
           - Current containment effectiveness
           - Global coordination needs
           - Resource allocation priorities
        
        4. Future Outlook:
           - Short-term predictions
           - Long-term implications
           - Recommended global preparations
        """
        return self._get_completion(prompt)

    def _get_completion(self, prompt):
        """Helper method for OpenAI API calls"""
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content