'''
..\google-cloud-sdk\bin\gcloud init

Fazer o Deploy dentro da pasta onde está a função
..\..\google-cloud-sdk\bin\gcloud functions deploy [function_name] --runtime python37 --trigger-http

'''
def hello_world(request):
    request_args = request.args
    request_json = request.get_json(silent=True)
    if request_args and 'name' in request_args:
        name = request_args['name']
        lastname = request_args['lastnam']
    elif request_json and 'name' in request_json and 'lastname' in request_json:
        name = request_json['name']
        lastname = request_json['lastname']
    else:
        name = 'World'
        lastname = ''
    # name = 'Hello'
    return f'Hello {name} {lastname}'