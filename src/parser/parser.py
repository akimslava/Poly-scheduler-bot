import asyncio
import datetime
import json

import pytz

from config import *
from tools import getData


async def parse_subject(subject: json) -> str:
    result = f"""{subject['time_start']} - {subject['time_end']} {subject['subject']}
              {subject['typeObj']['name']}
"""
    teachers = subject['teachers']
    if teachers is not None:
        for i, teacher in enumerate(teachers):
            result += ' ' * 14 + teacher['full_name'] + '\n'
    audiences = subject['auditories']
    if audiences is not None:
        for i, auditory in enumerate(audiences):
            result += ' ' * 14 + f"{auditory['name']}, {auditory['building']['name']}\n"
    return result


async def parse_day(day: json) -> str:
    result = ""
    for subject in day['lessons']:
        result += await parse_subject(subject) + '\n'
    return result


async def get(action: str, group_id: int) -> str:
    today = datetime.datetime.now(pytz.timezone('Europe/Moscow'))
    transform_action = {
        'на сегодня': today,
        'на завтра': today + datetime.timedelta(days=1),
        'на неделю': today if today.isoweekday() < 4 else today + datetime.timedelta(days=7),
    }
    try:
        date: datetime = transform_action[action]
    except:
        return "Во время запроса произошла ошибка"

    schedule = await getData(SCHEDULE_URL.format(group_id) + date.strftime('%Y-%m-%d'))

    week: list = schedule['days']

    msg_text = ""
    if action == 'на сегодня' or action == 'на завтра':
        for day in week:
            is_today = day['weekday'] == today.isoweekday() and action == 'на сегодня'
            is_tomorrow = (day['weekday'] == today.isoweekday() + 1) % 7 and action == 'на завтра'
            if is_today or is_tomorrow:
                msg_text = await parse_day(day)
    else:
        transform_day_number = {
            1: 'Понедельник',
            2: 'Вторник',
            3: 'Среда',
            4: 'Четверг',
            5: 'Пятница',
            6: 'Суббота',
            7: 'Воскресенье',
        }
        for day in week:
            msg_text += f"{transform_day_number[day['weekday']]} ({day['date']})\n"
            msg_text += await parse_day(day) + '\n'

    return msg_text


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        text = loop.run_until_complete(asyncio.gather(get("на неделю", 38736)))[0]
        print(text)
    finally:
        pass
