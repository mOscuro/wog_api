#===============================================================================
# Created on 30 nov. 2016
# @author: Matthieu
#===============================================================================

from rest_framework import permissions
from rest_framework.permissions import DjangoObjectPermissions

#===============================================================================
# CUSTOM HOMEMADE PERMISSIONS
#===============================================================================

class IsCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creators of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permission are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permission are only allowed to the creator of the Workout.
        return obj.creator == request.user
    
class IsWorkoutCreatorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow creators of an object to edit it.
    (specific use to Step update permission)
    """

    def has_object_permission(self, request, view, obj):
        # Write permission are only allowed to the creator of the Workout.
        #pdb.set_trace()
        return obj.workout.creator == request.user

#===============================================================================
# PERMISSIONS MAPPING FOR WORKOUT REQUESTS
#===============================================================================

class WorkoutObjectPermissions(DjangoObjectPermissions):
    perms_map = {
        'GET': ['wog_workout.view_project'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['wog_workout.add_workout'],
        'PUT': ['wog_workout.change_workout'],
        'PATCH': ['wog_workout.change_workout'],
        'DELETE': ['wog_workout.delete_workout'],
    }
