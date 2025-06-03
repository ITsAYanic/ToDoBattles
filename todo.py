from datetime import date, datetime
class ToDo:
    def __init__(self, todo: str, done: bool = False, created_at: date = None, importance: str = "normal", _id = None):
        if(_id is not None):
            self._id = _id
        self.todo = todo
        self.done = done
        if(created_at is None):
            self.created_at = datetime.now()
        else:
            self.created = created_at
        self.importance = importance

    def changeStatus(self):
        if(self.done == True):
            self.done = False
        else:
            self.done = True
