
import logging

import azure.functions as func
import requests

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    url = req.params.get('url')
    table = url + '/Assets'
    params = {'$select': 'ID,Name,PlanDataSetName, PropID,Scenario,SubType,VersionName'}
    username = 'tim.tong'
    password = 'lx*m1%24lx*m1%24'
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        #response = func.HttpRequest.get_Json(table, params=params ,auth=(username, password), verify = False)
        #print(response)
        #return func.HttpResponse(response) #f"Hello, {name}. This HTTP triggered function executed successfully.")
        #response = req.http_client.get(table, params=params ,auth=(username, password), verify = True)
        #return func.HttpResponse(response.content)
        #response = req.http_client.get(table)
        #return func.HttpResponse(response.content)
        response = requests.get(table, params=params  , auth=auth , verify=True)
        return func.HttpResponse(response.content)
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
