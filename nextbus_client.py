import requests

class NextBusClient(object):
    def __init__(self, route=None):
        self.base_url = 'http://webservices.nextbus.com/service/publicJSONFeed?command='
        self.agency = 'actransit'
        self.route = route

    def get_prediction(self):
        if not self.route:
            return
        url = u'{}predictions'.format(self.base_url)
        payload = {'a': '{}'.format(self.agency), 'r': self.route, 's': 1006860}
        return requests.get(url, params=payload)



def get_prediction_times(nb_client):
    request = nb_client.get_prediction()
    payload = request.json()
    direction_title = payload['predictions']['direction']['title']
    predictions_times = []
    for pt in payload['predictions']['direction']['prediction']:
        predictions_times.append(pt['minutes'])
    return ''.join(['%s min ' % pt for pt in predictions_times])
