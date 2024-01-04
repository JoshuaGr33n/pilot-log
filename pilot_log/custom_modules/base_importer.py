# base_importer.py
import json
from datetime import timedelta
import re

class BaseImporter:
    model = None
    serializer_class = None

    def __init__(self, file_path):
        self.file_path = file_path

    def read_data_from_file(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def import_data_for_model(self, model_data, serializer_class):
        for entry_data in model_data:
            serializer = serializer_class(data=entry_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
    def parse_duration(self, duration_str):
        match = re.match(r'PT(\d+)H(\d+)M', duration_str)
        if match:
            hours, minutes = map(int, match.groups())
            return timedelta(hours=hours, minutes=minutes)
        else:
            return timedelta()         
