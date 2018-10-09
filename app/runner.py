import yaml
from core.collector import Collector

conf = yaml.load(open("conf.yaml"))

collectors = list()

for c_conf in conf.get('collectors'):

    puller_conf = c_conf.get("puller", None)
    parser_conf = c_conf.get("parser", None)
    pusher_conf = c_conf.get("pusher", None)

    c = Collector(freq=c_conf.get("freq"))
    c.add_puller(puller_conf.get("class"), **puller_conf.get("kwargs"))
    c.add_parser(parser_conf.get("class"), **parser_conf.get("kwargs"))
    if pusher_conf.get("kwargs"):
        c.add_pusher(pusher_conf.get("class"), **pusher_conf.get("kwargs"))
    else:
        c.add_pusher(pusher_conf.get("class"))

    collectors.append(c)

repeat = True
while repeat:

    for c in collectors:

        if c.is_ready():
            c.collect()

    repeat = False