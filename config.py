# config.py
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    PORT = os.getenv('PORT')
    DATA_SERVICE_HOST = os.getenv('DATA_SERVICE_HOST')
    DATA_SERVICE_PORT = os.getenv('DATA_SERVICE_PORT')
    TOTAL_AND_ANNUALIZED_OPP_AMOUNT_URL = f"{DATA_SERVICE_HOST}:{DATA_SERVICE_PORT}/api/v1/review/total-opp-amount"
    PERFORMANCE_CHART_DATA_URL = f"{DATA_SERVICE_HOST}:{DATA_SERVICE_PORT}/api/v1/review/performance-chart-data"
    OPPORTUNITIES_BOOKED_URL = f"{DATA_SERVICE_HOST}:{DATA_SERVICE_PORT}/api/v1/review/booked-opps"

appConfig = Config()
