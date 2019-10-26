class MyMiddlewareOPTIONS:
    def __init__(self, options_response):
        self.options_response = options_response

    def __call__(self, request):
        response = self.options_response(request)
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Methods'] = "*"
        response['Access-Control-Allow-Headers'] = "*"
        return response
    
   

class MyMiddlewareGET:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = "*"
        response['Access-Control-Allow-Methods'] = "*"
        response['Access-Control-Allow-Headers'] = "*"
        return response