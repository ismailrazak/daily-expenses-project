from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import  models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id","username","first_name","last_name","email","mobile_number"]

    def validate_mobile_number(self,value):
        try:
            int(value)
            return value
        except:
            raise serializers.ValidationError("Info: Please enter a valid mobile_number.")


class OwnedBySerializer(serializers.ModelSerializer):
    class ExpenseField(serializers.ReadOnlyField):
        def to_representation(self, value):
            return value.name

    expense = ExpenseField()
    username = serializers.SlugRelatedField(slug_field="username",queryset=get_user_model().objects.all())
    class Meta:
        model = models.OwnedBy
        fields=["expense","username","owes"]

class ExpenseSerializer(serializers.ModelSerializer):
    owned_by = OwnedBySerializer(many=True)
    class Meta:
        model = models.Expense
        fields = ["id","name","total_bill","billing_method","owned_by"]

#used to create nested relationship.
    def create(self, validated_data):
        nested_data = validated_data.pop('owned_by')
        expense = models.Expense.objects.create(**validated_data)
        for owned_by in nested_data:
            models.OwnedBy.objects.create(expense=expense,**owned_by)
        return expense

#validating all the splitting methods.
    def validate_owned_by(self, data):
        billing_method = self.initial_data['billing_method']
        total_bill = float(self.initial_data['total_bill'])

        if billing_method == "EX":
            # exact amount splitting
            total = sum(self._parse_amount(owned_by['owes']) for owned_by in data)
            if total != total_bill:
                raise serializers.ValidationError("Total amount split does not equal the total_bill.")
            return data

        elif billing_method == "EQ":
            # equal splitting
            each_person_bill = total_bill / len(data)
            for owned_by in data:
                money = self._parse_amount(owned_by['owes'])
                if money != each_person_bill:
                    raise serializers.ValidationError(
                        f"Bill split should have been {each_person_bill:.2f} each, not {money}.")
            return data

        elif billing_method == "PE":
            # percentage splitting
            total_percentage = 0
            for owned_by in data:
                money = owned_by['owes']
                if not money.endswith('%'):
                    raise serializers.ValidationError(
                        "Please append a percentage at the end of the amount and try again.")

                percentage = self._parse_percentage(money[:-1])
                total_percentage += percentage

            if total_percentage != 100:
                raise serializers.ValidationError(f"Total percentage should have been 100%, not {total_percentage}%.")
            return data

    def _parse_amount(self, money):
        #helper function for validation.
        try:
            return float(money)
        except ValueError:
            raise serializers.ValidationError("Please enter a valid amount and try again.")

    def _parse_percentage(self, percentage):
        # helper function for validation.
        try:
            return float(percentage)
        except ValueError:
            raise serializers.ValidationError("Please enter a valid percentage and try again.")

