

import heapq
from typing import List
from Generic.time import get_cur_time
from Timer.event import TimeoutEvent


class Timer:

    def __init__(self):
        self.__events: List[TimeoutEvent] = []

    def get_events(self):
        return self.__events

    def add_event(self, event: TimeoutEvent):
        heapq.heappush(self.get_events(), event)

    def pop_event(self) -> TimeoutEvent:
        return heapq.heappop(self.get_events())

    def get_earliest_time(self):
        if self.get_events():
            return int(self.get_events()[0].get_timestamp().get_time() - get_cur_time())
        return float("inf")

    def is_event_can_active(self):
        return abs(self.get_earliest_time()) < 50


class SaveParam:

    def __init__(self, seconds, changes):
        self.seconds = seconds * 1000
        self.changes = changes

