from yapsy.IPlugin import IPlugin


class Calendar(IPlugin):
    def can_perform(self, friday, request):
        return 'action' in request['result'] and 'calendar' in request['result']['action']

    def perform(self, friday, request):
        return "Thingy"

    def activate(self):
        print("Calendar activated")

    def deactivate(self):
        print("Calendar activated")
