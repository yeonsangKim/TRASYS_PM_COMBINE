
from rest_framework import serializers
from . import models as pm

class pm_combine(serializers.ModelSerializer) :
    class Meta:
        model = pm.Parking
        fields = (
            "latitude",
            "longitude",
            "photo",
            "gcooter",
            "deer",
            "beam",
            "talang",
            "address",
        )