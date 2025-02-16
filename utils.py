from datetime import datetime
from mongoUtils import getDataByCurrentDate


async def generateText():
    data = await getDataByCurrentDate()
    if data != None and 'announced_at' in data.keys():
        content = data['format']
        content = content.replace('[batch_name]', data['batch_name'])
        for x in data['assignments']:
            deadline = datetime.strptime(
                x['deadline'], "%Y-%m-%d").strftime('%A, %d %B %Y')
            content = content.replace('[deadline]', deadline, 1)
            content = content.replace('[link]', x['link'], 1)

        return content
            
    return None


# print(generateText())
