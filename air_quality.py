import requests
from datetime import datetime

class AirQualityAnalyzer:
    def __init__(self):
        self.api_key = 'your_air_quality_api_key'
        self.base_url = 'https://api.airquality.com/v1/'
        
    async def get_air_quality(self, location):
        current_data = await self.fetch_current_data(location)
        forecast = await self.fetch_forecast(location)
        
        return {
            'current_aqi': current_data['aqi'],
            'pollutants': current_data['pollutants'],
            'forecast': forecast,
            'health_impact': self.assess_health_impact(current_data)
        }