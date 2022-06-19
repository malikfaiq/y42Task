from rest_framework.exceptions import ValidationError
from rest_framework import serializers
from .models import Record
from .utils import upload_file


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"

    def create(self, validated_data):
        file = self.context["request"].FILES.get("file", None)
        file_format = validated_data.get("file_format", None)
        if file and file_format:
            response = upload_file(file, file_format)
            if response:
                validated_data["file_path"] = response
                record = Record.objects.create(**validated_data)
                return record
        else:
            raise ValidationError({"error": "File or file format is missing!"})

    def update(self, instance, validated_data):
        file = self.context["request"].FILES.get("file", None)
        file_format = validated_data.get("file_format", None)
        [setattr(instance, k, v) for k, v in validated_data.items()]
        instance.save()
        if file and file_format:
            response = upload_file(file, file_format)
            if response:
                instance.file_path = response
                instance.save()
        return instance
