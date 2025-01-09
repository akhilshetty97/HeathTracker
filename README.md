# Disease Outbreak Monitor - Real-time Disease Surveillance Platform

A sophisticated web application that automatically tracks and analyzes global disease outbreaks using data from CDC and WHO. The system employs web scraping, RESTful APIs, and AI-powered analysis to provide real-time health risk assessments.

## Features

- **Automated Data Collection**
  - Real-time web scraping of disease outbreak data from CDC and WHO
  - Automated data update system with scheduled scraping jobs
  - Efficient data storage and management using PostgreSQL

- **RESTful API Endpoints**
  - Comprehensive disease outbreak information
  - Region-specific analysis and statistics
  - Global health assessments and risk analysis
  - USA-specific outbreak tracking

- **AI-Powered Analysis**
  - GPT-4 integration for automated health risk assessments
  - Pattern recognition in disease outbreak data
  - Generation of actionable health advisories

- **Interactive Dashboard**
  - Real-time visualization of outbreak data
  - Regional and global statistics
  - Trend analysis and historical data

## Tech Stack

- **Backend**: Django REST Framework
- **Database**: PostgreSQL
- **Frontend**: React
- **AI Integration**: GPT-4
- **Web Scraping**: Selenium
- **Additional Tools**: Redis (caching)

## API Endpoints

```python
GET /api/diseases/ - List all diseases
GET /api/diseases/usa/ - Get USA-specific outbreaks
GET /api/diseases/global/ - Get global outbreaks
GET /api/diseases/{id}/ - Get specific disease details
GET /api/diseases/{id}/analysis/ - Get AI analysis for specific disease
GET /api/diseases/region/{region}/ - Get regional impact analysis
GET /api/diseases/global_assessment/ - Get global health assessment
POST /api/diseases/update_data/ - Trigger data update
GET /api/diseases/statistics/ - Get outbreak statistics
