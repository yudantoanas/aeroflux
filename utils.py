import json
from datetime import datetime


def generateText(sourceFile):
    with open(sourceFile) as sourceFile:
        json_data = json.load(sourceFile)

    for data in json_data:
        if 'announced_at' in data.keys():
            announced_at = datetime.strptime(data['announced_at'], "%Y-%m-%d")
            if announced_at.date() == datetime.now().date():
                content = data['format']
                content = content.replace('[batch_name]', data['batch_name'])
                for x in data['assignments']:
                    deadline = datetime.strptime(
                        x['deadline'], "%Y-%m-%d").strftime('%A, %d %B %Y')
                    content = content.replace('[deadline]', deadline, 1)
                    content = content.replace('[link]', x['link'], 1)

                return content

    return None
