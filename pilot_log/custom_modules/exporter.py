# exporter.py
from .base_exporter import BaseExporter
from ..models import Flight
from ..serializers import FlightSerializer


class YourModelExporter(BaseExporter):
    model = Flight  
    serializer_class = FlightSerializer 

    def get_csv_data(self, data):
        headers = ['id', 'pilot_name', 'date', 'duration', 'created_at', 'updated_at']
        rows = [
            [str(getattr(instance, header)) if header != 'pilot_name' else str(getattr(instance.pilot, 'name')) for header in headers]
            for instance in data
        ]
        return headers, rows
