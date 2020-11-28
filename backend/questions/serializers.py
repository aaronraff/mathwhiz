from rest_framework import serializers


class QuestionSerializer(serializers.Serializer):
    prompt = serializers.CharField(max_length=30)
    answer = serializers.IntegerField()

    # Since sqlite3 doesn't support arrays, this will be a serialized array
    choices = serializers.CharField(max_length=512)

    def to_representation(self, obj):
        data = super().to_representation(obj)

        # Create array from choices, since it's currently a string
        # "[1, 2, 3, 4]" -> a Python list
        choices = data["choices"]
        choices = choices.replace(" ", "")
        choices = choices[1 : len(choices) - 1]  # Cut off the brackets
        choices = choices.split(",")
        data["choices"] = [int(c) for c in choices]
        return data
