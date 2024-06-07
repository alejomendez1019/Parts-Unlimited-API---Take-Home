import re
from collections import Counter
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Part
from .serializers import PartSerializer
from django.db import DatabaseError


class PartViewSet(viewsets.ModelViewSet):
    """
    ModelViewset provides the standard CRUD actions
    """
    queryset = Part.objects.all()
    serializer_class = PartSerializer


@api_view(['GET'])
def common_words(request):
    """
    Return the 5 most common words in part descriptions
    """
    # Stop words to exclude from the analysis; useless words for the sales team
    stop_words = set([
        'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from',
        'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the',
        'to', 'was', 'were', 'will', 'with'
    ])

    try:
        descriptions = Part.objects.values_list('description', flat=True)

        if not descriptions:
            return Response({'message': 'No descriptions found'},
                            status=status.HTTP_204_NO_CONTENT)

        # Convert all descriptions to a single string
        all_words = ' '.join(descriptions).lower()
        # Find all words
        words = re.findall(r'\b\w+\b', all_words)
        if not words:
            return Response({'message': 'No words found in descriptions'},
                            status=status.HTTP_204_NO_CONTENT)

        # Remove stop words
        filtered_words = [word for word in words if word not in stop_words]

        # Get the 5 most common words
        common_words = Counter(filtered_words).most_common(5)

        response_data = {
            'common_words': dict(common_words)
        }

        return Response(response_data, status=status.HTTP_200_OK)

    except DatabaseError:
        # Handle database errors
        return Response({'error': 'Database error occurred'}, status=status.
                        HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        # Handle other exceptions
        return Response({'error': str(e)}, status=status.
                        HTTP_500_INTERNAL_SERVER_ERROR)
