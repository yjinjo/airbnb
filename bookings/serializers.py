from django.utils import timezone
from rest_framework import serializers
from .models import Booking
from users.serializers import ManageBookingTinyUserSerializer
from rooms.serializers import TinyRoomSerializer


class CreateRoomBookingSerializer(serializers.ModelSerializer):

    check_in = serializers.DateField()
    check_out = serializers.DateField()

    class Meta:
        model = Booking
        fields = (
            "check_in",
            "check_out",
            "guests",
        )

    def validate_check_in(self, value):
        now = timezone.localdate(timezone.now())
        if now > value:
            raise serializers.ValidationError("Can't book in the past!")
        return value

    def validate_check_out(self, value):
        now = timezone.localdate(timezone.now())
        if now >= value:
            raise serializers.ValidationError("Can't book in the past")
        return value

    def validate(self, data):
        room = self.context.get("room")
        if data["check_out"] <= data["check_in"]:
            raise serializers.ValidationError(
                "Check in should be smaller than check out."
            )
        if Booking.objects.filter(
            room=room,
            check_in__lte=data["check_out"],
            check_out__gte=data["check_in"],
        ).exists():
            raise serializers.ValidationError(
                "Those (or some) of those dates are already taken."
            )
        return data


class CreateExperienceBookingSerializer(serializers.ModelSerializer):

    experience_time = serializers.DateTimeField()

    class Meta:
        model = Booking
        fields = (
            "experience_time",
            "guests",
        )

    def validate_experience_time(self, value):
        now = timezone.localdate(timezone.now())
        if now > value.date():
            raise serializers.ValidationError("Can't book in the past!")
        return value


class PublicBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = (
            "pk",
            "check_in",
            "check_out",
            "experience_time",
            "guests",
        )


class CheckMyBookingSerializer(serializers.ModelSerializer):

    room = TinyRoomSerializer()

    class Meta:
        model = Booking
        fields = (
            "id",
            "room",
            "kind",
            "check_in",
            "check_out",
            "guests",
            "not_canceled",
        )


class ManageBookingsSerializer(serializers.ModelSerializer):

    room = TinyRoomSerializer()

    user = ManageBookingTinyUserSerializer()

    class Meta:
        model = Booking
        fields = (
            "id",
            "room",
            "check_in",
            "check_out",
            "guests",
            "not_canceled",
            "user",
        )
