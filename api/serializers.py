from rest_framework import serializers
from django.contrib.auth.models import User
from dashboard.models import *

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'company_name','company_address', 'company_logo']

class UserProfileSerializer(serializers.ModelSerializer):
    company = CompanySerializer()

    class Meta:
        model = UserProfile
        fields = ['id', 'phone', 'profile', 'staff_level', 'company']


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','profile']

    def get_profile(self, obj):
        try:
            profile = obj.profile
            return UserProfileSerializer(profile).data
        except UserProfile.DoesNotExist:
            return None