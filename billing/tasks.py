from __future__ import absolute_import, unicode_literals
import random
import datetime

from celery import shared_task, task
from kombu.utils import json

from billing.models import BillingItem
from rest_framework import serializers


@shared_task(name="sum_two_numbers")
def add(x, y):
    return x + y


class BillingItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = BillingItem
        fields = "__all__"

@shared_task(name='multiply_two_number')
def mul(x, y):
    number_1 = x
    number_2 = x * (y * random.randint(3, 100))
    total = number_1 * number_2
    new_obj = BillingItem.objects.create(
        item_name='some item',
        number_1=number_1,
        number_2=number_2,
        total=total,
        timestamp=datetime.datetime.now
    )
    return BillingItemSerializer(new_obj).data


@shared_task(name="sum_list_numbers")
def xsum(numbers):
    return sum(numbers)