from django import template
from activity.views import ALL_ACTIVITIES
register = template.Library()

@register.filter(is_safe=True)
def mapactivity(value: str, arg:int):
    print(value, arg)
    model = ALL_ACTIVITIES.get(value.lower()).get('model')
    print(ALL_ACTIVITIES.get(value.lower()))
    queryset = model.objects.filter(created_by_id = arg)
    print("klsdjf", queryset)
    return queryset