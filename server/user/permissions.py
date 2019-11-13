from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
	message = '권한이 없습니다.'

	def has_object_permission(self, request, view, obj):
		# 읽기 권한은 모두에게 허용
		if request.method in SAFE_METHODS:
			return True
		# 쓰기 권한은 admin 권한이 있는 사용자나 그 글을 작성한 사람만 가능
		return obj.id == request.user.id or request.user.is_admin


# https://www.django-rest-framework.org/api-guide/permissions/