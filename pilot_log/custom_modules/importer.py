# importer.py
from .base_importer import BaseImporter
from ..serializers import PilotSerializer, FlightSerializer
from ..models import Pilot, Flight

class ModelImporter(BaseImporter):
    def import_pilots(self, pilots_data):
        for pilot_data in pilots_data:
            pilot, created = Pilot.objects.get_or_create(
                id=pilot_data.get('id'),
                defaults={
                    'name': pilot_data.get('name'),
                    'created_at': pilot_data.get('created_at'),
                    'updated_at': pilot_data.get('updated_at')
                }
            )

    def import_flights(self, flights_data):
        for flight_data in flights_data:
            pilot_id = flight_data.get('pilot')
            pilot = Pilot.objects.get(id=pilot_id) if pilot_id else None
            Flight.objects.create(
                id=flight_data.get('id'),
                pilot=pilot,
                date=flight_data.get('date'),
                duration= self.parse_duration(flight_data.get('duration')),
                created_at=flight_data.get('created_at'),
                updated_at=flight_data.get('updated_at')
            )
    
    def import_data(self):
        data = self.read_data_from_file()

        if 'pilots' in data:
            self.import_data_for_model(data['pilots'], PilotSerializer)
            # self.import_pilots(data['pilots'])
            
            
        if 'flights' in data:
            self.import_data_for_model(data['flights'], FlightSerializer) 
            # self.import_flights(data['flights'])
                   
