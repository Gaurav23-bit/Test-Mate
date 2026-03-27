import requests

def execute_request(method, url, headers=None, body=None, params=None):
    try:
        req_headers = {}
        if headers:
            for line in headers.split('\n'):
                if ':' in line:
                    key, val = line.split(':', 1)
                    req_headers[key.strip()] = val.strip()
        
        req_body = body.encode('utf-8') if body else None
        
        response = requests.request(
            method=method,
            url=url,
            headers=req_headers,
            data=req_body,
            params=params,
            timeout=10
        )
        return response, None
    except requests.exceptions.RequestException as e:
        return None, str(e)