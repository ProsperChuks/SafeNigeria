from core.models import CITIES, State

for ele_one, ele_two in CITIES:
    State.objects.create(name=ele_one)