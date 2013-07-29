"""
Copyright (c) 2013 John Vrbanac

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
from types import FunctionType


class EventManager(object):

    def __init__(self):
        super(EventManager, self).__init__()
        self.listeners = []

    def add_listener(self, evt_type, callback):
        self.listeners.append(Listener(evt_type, callback))

    def has_listener(self, evt_type, callback):
        return Listener(evt_type, callback) in self.listeners

    def remove_listener(self, evt_type, callback):
        if self.has_listener(evt_type, callback):
            self.listeners.remove(Listener(evt_type, callback))

    def dispatch(self, event):
        to_call = [l for l in self.listeners if l.type is event.type]
        for listener in to_call:
            if type(listener.callback) is FunctionType:
                listener.callback(event)


class Listener(object):

    def __init__(self, evt_type, callback):
        super(Listener, self).__init__()
        self.type = evt_type
        self.callback = callback

    def __eq__(self, other):
        result = False
        if type(other) is Listener:
            result = self.type == other.type and self.callback == other.type
        return result

    def __ne__(self, other):
        return self is not other


class Event(object):

    def __init__(self, event_type, payload=None):
        super(Event, self).__init__()
        self.event_type = event_type
        self.payload = payload
