class ToDo:
    def _init_(self, todo, done, created, importance, _id = None):
        self.todo = todo
        self.done = done
        self.created = created
        self.importance = importance
        if (_id is not None):
            self._id = _id