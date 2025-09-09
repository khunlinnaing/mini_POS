from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from dashboard.models import UserProfile, Company

class LoginSerializer(serializers.Serializer):
    username_or_email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username_or_email = attrs.get('username_or_email')
        password = attrs.get('password')

        user = self._authenticate(username_or_email, password)

        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        attrs['user'] = user
        return attrs

    def _authenticate(self, username_or_email, password):
        # Try username
        user = authenticate(username=username_or_email, password=password)
        if user:
            return user

        # Try email
        try:
            user_obj = User.objects.get(email=username_or_email)
            user = authenticate(username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        return user



class RegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)
    
    # Profile fields:
    phone = serializers.CharField(required=False, allow_blank=True)
    profile = serializers.ImageField(required=False, allow_null=True)
    staff_level = serializers.ChoiceField(choices=UserProfile.STAFF_LEVEL_CHOICES, default=0)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name',
                  'phone', 'profile', 'staff_level', 'company']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        validate_password(attrs['password'])
        return attrs

    def create(self, validated_data):
        phone = validated_data.pop('phone', '')
        profile_image = validated_data.pop('profile', None)
        staff_level = validated_data.pop('staff_level', 0)
        company = validated_data.pop('company')

        validated_data.pop('confirm_password')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )

        UserProfile.objects.create(
            user=user,
            phone=phone,
            profile=profile_image,
            staff_level=staff_level,
            company=company
        )

        return user

