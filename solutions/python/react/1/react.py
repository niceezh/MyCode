from typing import Any

class InputCell:
    def __init__(self, initial_value):
        self._value = initial_value
        self.dependents = []

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if self._value == new_value:
            return
        self._value = new_value

        queue = [self]
        changed_cells = []
        while queue:
            cell = queue.pop(0)
            if isinstance(cell, InputCell):
                for dependent in cell.dependents:
                    if dependent not in queue:
                        queue.append(dependent)
            elif isinstance(cell, ComputeCell):
                cell: Any
                if cell.recompute():
                    changed_cells.append(cell)
                    for dependent in cell.dependents:
                        if dependent not in queue:
                            queue.append(dependent)
        for cell in changed_cells:
            for callback in cell.callbacks:
                callback(cell._value)

    def add_dependent(self, dependent):
        self.dependents.append(dependent)


class ComputeCell:
    def __init__(self, inputs, compute_function):
        self.inputs = inputs
        self.compute_function = compute_function
        self.callbacks = []
        self.dependents = []
        self._value = compute_function([input_cell.value for input_cell in inputs])

        for input_cell in inputs:
            input_cell.add_dependent(self)

    @property
    def value(self):
        return self._value

    def add_dependent(self, dependent):
        self.dependents.append(dependent)

    def recompute(self):
        new_value = self.compute_function([input_cell.value for input_cell in self.inputs])
        if self._value == new_value:
            return False
        self._value = new_value
        return True

    def add_callback(self, callback):
        if callback not in self.callbacks:
            self.callbacks.append(callback)

    def remove_callback(self, callback):
        if callback in self.callbacks:
            self.callbacks.remove(callback)
