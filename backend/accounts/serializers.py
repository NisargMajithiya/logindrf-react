from rest_framework import serializers
# from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','phone_number','password','user_profileimage']
        extra_kwargs = {
            'password': {'write_only': True},
            'user_profileimage': {'allow_null':True}
            }

    def validate_password(self,value):

        try:
            validate_password(value)
        except Exception as e:
            raise serializers.ValidationError(list(e.messages))
            

        return value
        
    def create(self,validated_data):

        # remove the password for the python dic
        password = validated_data.pop('password',None)


        #create a user instacne with validate_data 
        user = User(**validated_data)

        
        #hash the password and then add it to the user instance with set_passwrod()fucntion
        if password is not None:
            user.set_password(password)
        else:
            raise serializers.ValidationError({"password": "Password is required."})
        
        #save to db
        user.save()
            
        return user
        

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError("both username and password are required")
        
        user = authenticate(username=username,password= password)

        if not user:
            raise serializers.ValidationError("invalid credentials")
        
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")
        
        attrs['user'] = user
        return attrs
    
    
class User_serializer(serializers.Serializer):
    class meta:
        model = User
        fields = '__all__'



