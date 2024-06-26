from .permission import IsStaffEditorPermission, IsMemberPermission
from rest_framework import permissions

class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
class MemberPermissionMixin():
    permission_classes = [permissions.IsAuthenticated, IsMemberPermission]
    
class UserQuerySetMixin():
    user_field = 'user'
    allow_staff_view = False
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        lookup_data = {}
        lookup_data[self.user_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        if self.allow_staff_view and user.is_staff or user.is_superuser:
            return qs
        return qs.filter(**lookup_data)
        
        
