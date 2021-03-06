# config.py
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    PORT = os.getenv('PORT')
    DATA_SERVICE_HOST = os.getenv('DATA_SERVICE_HOST')
    DATA_SERVICE_PORT = os.getenv('DATA_SERVICE_PORT')
    TOTAL_AND_ANNUALIZED_OPP_AMOUNT_URL = f"{DATA_SERVICE_HOST}/api/v1/review/total-opp-amount"
    PERFORMANCE_CHART_DATA_URL = f"{DATA_SERVICE_HOST}/api/v1/review/performance-chart-data"
    OPPORTUNITIES_BOOKED_URL = f"{DATA_SERVICE_HOST}/api/v1/review/booked-opps"

appConfig = Config()
