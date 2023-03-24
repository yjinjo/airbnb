import requests
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound, PermissionDenied
from .models import Photo

from dotenv import load_dotenv
import os

load_dotenv()


class PhotoDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Photo.objects.get(pk=pk)
        except Photo.DoesNotExist:
            raise NotFound

    def delete(self, request, pk):
        photo = self.get_object(pk=pk)

        if (photo.room and photo.room.owner != request.user) or (
            photo.experience and photo.experience.host != request.user
        ):
            raise PermissionDenied

        photo.delete()
        return Response(status=HTTP_200_OK)


class GetUploadURL(APIView):
    def post(self, request):
        url = f"https://api.cloudflare.com/client/v4/accounts/{os.environ.get('CLOUDFLARE_ID')}/images/v2/direct_upload"
        one_time_url = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {os.environ.get('CLOUDFLARE_TOKEN')}",
            },
        )
        one_time_url = one_time_url.json()
        result = one_time_url.get("result")
        return Response({"uploadURL": result.get("uploadURL")})
