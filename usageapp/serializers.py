
from rest_framework import serializers
from . import models as pm

class test(serializers.ModelSerializer) :
    class Meta:
        model = pm.Usage
        fields = (
            "mon_avg",
            "tus_avg",
            "wed_avg",
            "thr_avg",
            "fri_avg",
            "sat_avg",
            "sun_avg",
            "ja",
            "fe",
            "mar",
            "apr",
            "may",
            "jun",
            "jul",
            "aug",
            "sep",
            "oct",
            "nov",
            "dec",
        )