from django.contrib import admin



from .models import Exercise , WorkOut, WorkOut_Exercise , MuscleGroup

admin.site.register(Exercise)
admin.site.register(WorkOut)
admin.site.register(MuscleGroup)
admin.site.register(WorkOut_Exercise)