import requests
from parser import format_stops_message, format_times_message

class NextBusClient(object):
    def __init__(self, route, command, stop_id=None):
        self.base_url = 'http://webservices.nextbus.com/service/publicJSONFeed?command='
        self.agency = 'actransit'
        self.route = route
        self.command = command
        self.stop_id = stop_id

    def _get_url(self):
        if not self.route or not self.command:
            return
        return u'{}{}'.format(self.base_url, self.command)

    def _get_params(self):
        payload = {
            'a': '{}'.format(self.agency),
            'r': self.route,
        }
        if self.command in ['schedule', 'predictions']:
            payload['stopId'] = self.stop_id

        return payload

    def _get_request(self):
        url = self._get_url()
        params = self._get_params()
        return requests.get(url, params=params)

    def get_prediction_times(self):
        r = self._get_request().json()
        direction_title = r['predictions']['direction']['title']
        predictions_times = []
        for pt in r['predictions']['direction']['prediction']:
            predictions_times.append(pt['minutes'])
        return ''.join(['%s min ' % pt for pt in predictions_times])

    def get_route_config(self):
        r = self._get_request().json()
        stops =  []
        # todo: handle more than 20 stops
        for s in r['route']['stop'][:20]:
            if s.get('stopId'):
                stops.append({'title': s['title'], 'id': s['stopId']})
        return stops

    def get_message(self):
        if self.command == 'routeConfig':
            stops = self.get_route_config()
            return format_stops_message(self.route, stops)
        if self.command == 'predictions':
            times = self.get_prediction_times()
            return format_times_message(self.route, times)
