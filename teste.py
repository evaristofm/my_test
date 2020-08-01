import json


with open('source_file_2 .json') as f:
    data = json.load(f)

priority = {}
managers = {}
watchers = {}

for d in data:
    priority[f"{d['name']}"] = d['priority']

    for manager in d['managers']:

        if not f"{manager}" in managers:
            managers[f"{manager}"] = []

        managers[f"{manager}"].append(d['name'])

    for watcher in d['watchers']:

        if not f"{watcher}" in watchers:
            watchers[f"{watcher}"] = []

        watchers[f"{watcher}"].append(d['name'])


def sortproj(x):
    return priority[x]

for manager in managers:
    managers[manager].sort(key=sortproj)

for watcher in watchers:
    watchers[watcher].sort(key=sortproj)


managers_json = json.dumps(managers, indent=True)
watchers_json = json.dumps(watchers, indent=True)


with open('manager.json', 'w+') as file:
    file.write(managers_json)
    file.close()

with open('watchers.json', 'w+') as file:
    file.write(watchers_json)
    file.close()
