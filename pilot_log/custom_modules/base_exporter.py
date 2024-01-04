# base_exporter.py
import csv
from io import StringIO

class BaseExporter:
    model = None
    serializer_class = None

    def export_data_to_csv(self):
        data = self.get_data()
        csv_data = self.serialize_to_csv(data)
        return csv_data

    def get_data(self):
        return self.model.objects.all()

    def serialize_to_csv(self, data):
        headers, rows = self.get_csv_data(data)
        output = StringIO()
        csv_writer = csv.writer(output)
        csv_writer.writerow(headers)
        csv_writer.writerows(rows)
        return output.getvalue()

    def get_csv_data(self, data):
        raise NotImplementedError("Method get_csv_data must be implemented in subclasses.")
