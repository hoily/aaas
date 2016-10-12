from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class ImageAPIView(GenericAPIView):
    def get(self, request, width, height):
        return Response({
            'width': width,
            'height': height
        })
