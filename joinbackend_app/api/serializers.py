from rest_framework import serializers
from joinbackend_app.models import Contact, User, Task, Subtask


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_to_data = validated_data.pop('assigned_to', [])

        # Update task fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Clear existing subtasks
        instance.subtasks.all().delete()
        instance.assigned_to.all().delete()

        # Add new subtasks correctly
        for subtask_data in subtasks_data:
            instance.subtasks.create(**subtask_data)  # Use related manager

        # Add new contacts correctly
        for assigned in assigned_to_data:
            instance.assigned_to.create(**assigned)  # Use related manager

        return instance

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_to_data = validated_data.pop('assigned_to', [])

        # Create the task first
        task = Task.objects.create(**validated_data)

        task.assigned_to.set(assigned_to_data)

        # Create the related subtasks
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)

        return task
