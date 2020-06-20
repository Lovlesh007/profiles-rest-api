from rest_framework.views import APIView   
#import APIview Class from the rest framework
from rest_framework.response import Response

class HelloApiView(APIView):
    """Testing of the API view"""
    """the working is that whenever we do any request on the url
    then the url passes that request to the APIView Functions and
    as we inherit the ApiView Function we catch the request and then
    we define our http function like get, post, put etc.. according
    to out requirements. Please note that the end of the process we have to
    return the response object."""

    def get(self,request,format=None):
        """Returns a list of API view Features"""
        
        #create a list for features for printing.
        an_apiview =[
            'Uses HTTP method as functions(get,post,patch,put,delete',
            'Is similiar to a traditional Django view',
            'Gives you the most control over the application logic',
            'Is mapped manually to urls',

        ]

        """It is verrry necessary to response back to api , so this api as you see is for return the API
        Features which are written on List 'an_apiview' then we return back to it  """
        return Response({'message':'Hey My self Lovlesh Bhatt', 'an_apiview': an_apiview})



