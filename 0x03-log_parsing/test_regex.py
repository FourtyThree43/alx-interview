import re

def parse_line(line):
    pattern = (
    r'(?P<ip>\d+\.\d+\.\d+\.\d+\s+)s+',
    r'-s+\[(?P<date>.*?)\]s+',
    r'"(?P<method>GET) (?P<resource>./projects/260) HTTP/1.1" (?P<status_code>\d{3}) (?P<file_size>\d+)'
    )
    match = re.fullmatch(pattern, line.strip())
    if match:
        return match.groupdict()
    else:
        return None

line = '80.10.166.113 - [2023-10-21 12:10:19.711191] "GET /projects/260 HTTP/1.1" 200 990'
line2 = 'Hello'
print(parse_line(line))
print(parse_line(line2))

