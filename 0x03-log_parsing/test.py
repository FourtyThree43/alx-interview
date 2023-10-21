import re
from collections import defaultdict


def parse_logs(log_lines):
    fp = (r'\s*(?P<ip>\S+)\s*',
          r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',
          r'\s*"(?P<method>\S+)\s*(?P<resource>\S+)\s*(?P<protocol>[^"]*)"\s*',
          r'\s*(?P<status_code>\S+)', r'\s*(?P<file_size>\d+)')

    log_fmt = '{}\\-{}{}{}{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])

    stats = {
        'total_file_size': 0,
        'requests_by_method': defaultdict(int),
        'requests_by_protocol': defaultdict(int),
        'requests_by_status_code': defaultdict(int),
        'top_10_ips': defaultdict(int),
        'top_10_resources': defaultdict(int),
    }

    for line in log_lines:
        resp_match = re.fullmatch(log_fmt, line)
        if resp_match is not None:
            method = resp_match.group('method')
            resource = resp_match.group('resource')
            protocol = resp_match.group('protocol')
            status_code = int(resp_match.group('status_code'))
            file_size = int(resp_match.group('file_size'))
            ip = resp_match.group('ip')

            stats['total_file_size'] += file_size
            stats['requests_by_method'][method] += 1
            stats['requests_by_protocol'][protocol] += 1
            stats['top_10_resources'][resource] += 1
            stats['requests_by_status_code'][status_code] += 1
            stats['top_10_ips'][ip] += 1

    stats['top_10_resources'] = dict(
        sorted(stats['top_10_resources'].items(),
               key=lambda item: item[1],
               reverse=True)[:10])
    stats['top_10_ips'] = dict(
        sorted({
            k: v
            for k, v in stats['top_10_ips'].items() if v >= 2
        }.items(),
               key=lambda item: item[1],
               reverse=True)[:10])

    return stats


if __name__ == '__main__':
    with open("logs.txt", "r") as f:
        input_logs = f.readlines()

    print(parse_logs(input_logs), end="\n")
