from rest_framework import viewsets, routers, serializers
from polls import models

# the serializer specifies how the records are serialized in the list or detail-views
class PollSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Poll
		fields = ('id', 'url', 'question', 'pub_date', )

# the viewset defines urls and views for list and detail-viwes
class PollViewSet(viewsets.ModelViewSet):
	model = models.Poll
	serializer_class = PollSerializer

# register viewsets for the rest-api
def register(restrouter):
	restrouter.register(r'polls', PollViewSet)