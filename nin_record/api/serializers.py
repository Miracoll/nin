from rest_framework import serializers

from nin_record.models import Guardian, NINProfile, NextOfKin, Parent, SupportingDocument

class NINProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NINProfile
        fields = '__all__'

class SupportingDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportingDocument
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = '__all__'

class NextOfKinSerializer(serializers.ModelSerializer):
    class Meta:
        model = NextOfKin
        fields = '__all__'