from django.contrib.auth import get_user_model

from rest_framework import serializers

from allauth.account.models import EmailAddress


class UserDetailsSerializer(serializers.ModelSerializer):

    email_verified = serializers.SerializerMethodField()

    def get_email_verified(self, user):
        verified_email_exists = user.emailaddress_set.filter(
            verified=1
        ).exists()

        return verified_email_exists

    class Meta:
        model = get_user_model()
        fields = (
            'pk',
            'username',
            'email',
            'first_name',
            'last_name',
            'email_verified'
        )

    def update(self, instance, validated_data):
        new_email = validated_data.pop('email', None)
        user = super().update(instance, validated_data)

        # http://stackoverflow.com/questions/19755102/django-allauth-change-user-email-with-without-verification
        if new_email:
            request = self.context.get("request")
            if request:
                EmailAddress.objects.add_email(
                    request,
                    user,
                    new_email,
                    confirm=True
                )

        return user
