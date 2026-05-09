from rest_framework.views import APIView 
from rest_framework.exceptions import PermissionDenied 
from core.services import AuthService 

class PermissionAPIView(APIView): 
    permissions = None 
    
    def check_permissions(self, request): 
        super().check_permissions(request)

        if not self.permissions:
            return 
            
        allowed = AuthService.user_has_any_permission(request.user, self.permissions) 
            
        if not allowed: 
            raise PermissionDenied("You do not have permission to perform this action.")