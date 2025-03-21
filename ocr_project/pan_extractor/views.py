from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .utils import extract_details
import numpy as np
from PIL import Image
import io

class PanOCRView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({"error": "No file uploaded"}, status=400)

        file = request.FILES['file']
        image = np.array(Image.open(io.BytesIO(file.read())))  # Convert to NumPy array

        results = extract_details(image)

        return Response({"filename": file.name, "data": results})
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .utils import extract_details
import numpy as np
from PIL import Image
import io

class PanOCRView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({"error": "No file uploaded"}, status=400)

        file = request.FILES['file']
        image = np.array(Image.open(io.BytesIO(file.read())))  # Convert to NumPy array

        results = extract_details(image)

        return Response({"filename": file.name, "data": results})
