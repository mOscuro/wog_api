from django.conf.urls import url, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_nested import routers

from account.views import AccountViewSet
from workout.views import WorkoutViewSet, StepNestedInWorkoutViewSet, WorkoutTreeViewSet
from exercise.views import ExerciseViewSet


router = routers.DefaultRouter()
router.register(r'users', AccountViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'exercises', ExerciseViewSet)


workouts_router = routers.NestedSimpleRouter(router, r'workouts', lookup='workout')
workouts_router.register(r'steps',
                          StepNestedInWorkoutViewSet,
                          base_name='workout-steps')
workouts_router.register(r'tree',
                         WorkoutTreeViewSet,
                         base_name='workout-tree')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(workouts_router.urls)),
    url(r'^obtain-auth-token/$', obtain_auth_token),
]