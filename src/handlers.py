import sys
import traceback
import asyncio
import logging

import asyncio_redis


logger = logging.getLogger(__name__)


@asyncio.coroutine
def redis(callback, host='localhost', port=6379, db=0, channel='channel'):
    connection = yield from asyncio_redis.Connection.create(host=host, port=port, db=db)
    subscriber = yield from connection.start_subscribe()
    yield from subscriber.subscribe([channel])
    while True:
        try:
            pub = yield from subscriber.next_published()
            yield from callback(pub.value)
        except Exception as exc:
            logger.error('\n'.join(traceback.format_tb(sys.exc_info()[2])))

