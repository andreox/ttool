from rest_framework import serializers
from tickets.models import Tickets

#class TicketsSerializer(serializers.Serializer):
#    id = serializers.IntegerField(required=True)
#    head = serializers.CharField(required=False,allow_blank=True,max_length=100)
#    body = serializers.CharField(required=False,allow_blank=True,max_length=300)
#    ticket_class = serializers.CharField(required=False,allow_blank=True,max_length=50)

#    def create(self, validated_data):
#
#        return Tickets.objects.create(**validated_data)
#
#    def update(self, instance, validated_data):
#
#        instance.id = validated_data.get('id',instance.id)
#        instance.head = validated_data.get('head',instance.head)
#        instance.body = validated_data.get('body',instance.body)
#        instance.ticket_class = validated_data.get('ticket_class',instance.ticket_class)
#        instance.save()
#        return instance

class TicketsSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Tickets
        fields = ['id','head','body','ticket_class']



