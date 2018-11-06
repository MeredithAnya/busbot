COMMAND_MAP = {
    'sched': 'schedule',
    'times': 'predictions',
    'config': 'routeConfig',
}

def parse_text_body(body):
    """
    eg. 'B times :stopId', '12 sched'

    """
    words = body.split()
    route, command = words[:2]
    try:
        stop_id = words[2]
    except IndexError:
        stop_id = None

    return {
        'route': route,
        'command': COMMAND_MAP[command],
        'stop_id': stop_id,
    }

def format_times_message(route, times):
    return "Bus times for {} line:\n{}".format(route, times)

def format_stops_message(route, stops):
    message = u"Bus stops for {} line:\n".format(route)
    for stop in stops:
        message += u"{}: {}\n".format(stop['title'], stop['id'])

    return message
