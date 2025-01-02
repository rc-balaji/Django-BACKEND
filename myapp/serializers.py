from rest_framework import serializers
from .models import (
    User,
    Topic,
    UserTopic,
    SubTopic,
    LearningMaterial,
    Practice,
    Test,
    PracticeQuestion,
    TestQuestion,
    PracticeOption,
    TestOption,
    TestHistory,
    Report,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class UserTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTopic
        fields = "__all__"


class SubTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTopic
        fields = "__all__"


class LearningMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = LearningMaterial
        fields = "__all__"


class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class PracticeQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeQuestion
        fields = "__all__"


class TestQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = "__all__"


class PracticeOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeOption
        fields = "__all__"


class TestOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestOption
        fields = "__all__"


class TestHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TestHistory
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
