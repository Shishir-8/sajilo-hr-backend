from rest_framework import serializers
from accounts.models import User
from .models import Employee


class EmployeeCreateSerializer(serializers.ModelSerializer):

    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, required=False)

    role = serializers.ChoiceField(
        choices=['admin', 'hr', 'employee'],
        default='employee',
        write_only=True
    )


    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'email', 'username', 'password',
            'department', 'position', 'salary', 'role',
            'phone', 'address'
        ]

    def create(self, validated_data):

        # USER DATA
        username = validated_data.pop('username')
        email = validated_data.pop('email')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        password = validated_data.pop('password', '123456')
        role = validated_data.pop('role', 'employee')

        # CREATE USER AUTOMATICALLY
        user = User.objects.create_user(
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role=role
        )

        # CREATE EMPLOYEE LINKED TO USER
        employee = Employee.objects.create(
            user=user,
            **validated_data
        )

        return employee
    
class EmployeeReadSerializer(serializers.ModelSerializer):

    employee_name = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def get_employee_name(self, obj):
        return obj.user.get_full_name() or obj.user.username