# views.py
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .custom_modules.importer import YourModelImporter
from .custom_modules.exporter import YourModelExporter
import os

class YourModelViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        file_uploaded = request.data.get('file', None)
        if file_uploaded:
            # Save the uploaded file to a temporary location
            with open('temp_file.json', 'wb+') as temp_file:
                for chunk in file_uploaded.chunks():
                    temp_file.write(chunk)

            # Use the file path for importing
            importer = YourModelImporter('temp_file.json')
            importer.import_data()

            # Clean up: remove the temporary file
            os.remove('temp_file.json')

            return Response({"message": "Import successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "File not provided"}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        exporter = YourModelExporter()
        csv_data = exporter.export_data_to_csv()
        return Response({"message": "Export successful", "data": csv_data}, status=status.HTTP_200_OK)
