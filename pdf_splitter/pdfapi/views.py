import os
import zipfile
from django.http import JsonResponse, HttpResponse
from PyPDF2 import PdfReader, PdfWriter
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from datetime import datetime

OUTPUT_DIR = '/home/buzzadmin/Documents/Desktop/Click_On_This/upload/Project-B/pdf_splitter/output'

@csrf_exempt
def split_pdf(request):
    try:
        if request.method == 'POST':
            if 'file' not in request.FILES:
                return JsonResponse({'error': 'Please upload a file'}, status=400)

            uploaded_file = request.FILES['file']
            if not uploaded_file.name.endswith('.pdf'):
                return JsonResponse({'error': 'File must be a PDF'}, status=400)

            # Create the output directory if it doesn't exist
            if not os.path.exists(OUTPUT_DIR):
                os.makedirs(OUTPUT_DIR)

            # Generate a timestamped folder based on the uploaded file's name
            base_filename = os.path.splitext(uploaded_file.name)[0]
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_folder = os.path.join(OUTPUT_DIR, f"{base_filename}_{timestamp}")
            os.makedirs(output_folder)

            # Save the uploaded file temporarily
            fs = FileSystemStorage(location=output_folder)
            pdf_path = fs.save(uploaded_file.name, uploaded_file)
            pdf_path = fs.path(pdf_path)

            # Create a zip file to store split PDFs
            zip_file_path = os.path.join(output_folder, f'{base_filename}_split_pages.zip')
            with zipfile.ZipFile(zip_file_path, 'w') as zipf:
                reader = PdfReader(pdf_path)
                for i, page in enumerate(reader.pages):
                    writer = PdfWriter()
                    writer.add_page(page)

                    page_pdf_path = os.path.join(output_folder, f'{base_filename}_page_{i + 1}.pdf')
                    with open(page_pdf_path, 'wb') as output_pdf:
                        writer.write(output_pdf)

                    zipf.write(page_pdf_path, os.path.basename(page_pdf_path))

            # Serve the zip file as a response
            with open(zip_file_path, 'rb') as zip_file:
                response = HttpResponse(zip_file.read(), content_type='application/zip')
                response['Content-Disposition'] = f'attachment; filename={base_filename}_split_pages.zip'
            
            return response

        return JsonResponse({'error': 'Invalid request'}, status=400)
    
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {str(e)}'}, status=500)
