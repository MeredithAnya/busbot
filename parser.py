COMMAND_MAP = {
    'sched': 'schedule',
    'times': 'predictions'
}
def parse_text_body(body):
    route, command = body.split()
    return route, COMMAND_MAP[command]

def format_times_message(route, times):
    return "Bus times for {} line:\n{}".format(route, times)
