  
import hoshino
import re
from datetime import timedelta
from hoshino import Service, priv
from hoshino.typing import CQEvent

from nonebot import on_command

@on_command('起床', aliases=('回来', '回来啦', '醒醒'), only_to_me=True)  #不属于service
async def back(session):
    ctx = session.ctx
    group_id = ctx['group_id']
    if hoshino.priv.check_block_group(group_id) == True :
        hoshino.priv.remove_block_group(group_id)
        await session.send(f"我回来啦！", at_sender=True)
    else :
        await session.send(f"我明明一直都在！", at_sender=True)

sv = Service('_switch_', visible=False)


@sv.on_prefix('休息', only_to_me=True)
async def leave(bot, ev: CQEvent):
    if not priv.check_priv(ev, priv.ADMIN):
        await bot.finish(ev, '我还有工作要做，不能去休息呢~', at_sender=True)
    kw = '5分钟'
    time = { '小时': 8, '分钟': 0, '天': 0 }
    group_id = ev.group_id
    for msg in ev.message:
        if msg.type == 'text':
            kw = msg.data['text'].replace(' ', '')
            t_match = re.search(r'(?P<num>[0-9]+)(?P<tp>小时|天|分|分钟)', kw)
            if t_match and int(t_match.group('num')) > 0:
                time = { '小时': 0, '分钟': 0, '天': 0 }
                t = t_match.group('tp')
                t = t if t != '分' else '分钟'
                time[t] = int(t_match.group('num'))
            break
    uid = int(group_id)
    hoshino.priv.set_block_group(uid,timedelta(days=time['天'],minutes=time['分钟'],hours=time['小时']))
    await bot.send(ev, f"那么我就去休息{kw}啦，Zzz~")
    return