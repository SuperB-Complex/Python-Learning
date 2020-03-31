import json

OPENFILE, CUSTOMIZEDFILE = "open.json", "customised.json"

class Dispatcher:
    @classmethod
    def dispatcher(cls, filenaem):
        with open(filenaem, 'r') as r:
            for row in r.readlines():
                data = dict(json.loads(row))
                f = str(data['year']) + '_' + filenaem
                with open(f, 'a') as w:
                    w.write(row)
                    w.write('\n')
        return 
        
Dispatcher.dispatcher(OPENFILE)
Dispatcher.dispatcher(CUSTOMIZEDFILE)