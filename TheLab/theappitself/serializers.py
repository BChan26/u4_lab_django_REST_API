from rest_framework import serializers
from .models import Team, Player

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    playername=serializers.HyperlinkedRelatedField(
        view_name = 'player_detail',
        many = True,
        read_only = True
    )
    class Meta:
        model = Team
        fields = ('id', 'name', 'location', 'division', 'wins', 'losses', 'playername')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    team = serializers.HyperlinkedRelatedField(
        view_name = 'team_detail',
        read_only = True
    )
    class Meta:
        model = Player
        fields = ('id', 'playername', 'position', 'age', 'injured', 'team')