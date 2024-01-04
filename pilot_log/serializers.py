# serializers.py
from rest_framework import serializers
from .models import Pilot, Flight

class BaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = None 
        fields = '__all__'

    def validate_unique_field(self, field_name, field_value):
        # Check if the specified field value is unique
        if field_name and field_value:
            query_params = {field_name: field_value}
            if self.Meta.model.objects.filter(**query_params).exists():
                raise serializers.ValidationError(f"{field_name.capitalize()} must be unique.")

class PilotSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Pilot
        fields = ['id', 'name', 'created_at', 'updated_at']

    def create(self, validated_data):
        self.validate_unique_field('name', validated_data.get('name'))
        return super().create(validated_data)

class FlightSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Flight
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)
