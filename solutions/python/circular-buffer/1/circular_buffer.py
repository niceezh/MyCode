class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity < 1:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.read_position = 0
        self.write_position = 0
        self.size = 0

    def read(self):
        if self.is_empty():
            raise BufferEmptyException("Circular buffer is empty")
        value = self.buffer[self.read_position]
        self.buffer[self.read_position] = None
        self.read_position = (self.read_position + 1) % self.capacity
        self.size -= 1
        return value

    def write(self, data):
        if self.is_full():
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.write_position] = data
        self.write_position = (self.write_position + 1) % self.capacity
        self.size += 1

    def overwrite(self, data):
        if self.is_full():
            self.read_position = (self.read_position + 1) % self.capacity
            self.size -= 1
        self.buffer[self.write_position] = data
        self.write_position = (self.write_position + 1) % self.capacity
        self.size += 1

    def clear(self):
        for i in range(self.capacity):
            self.buffer[i] = None
        self.read_position = 0
        self.write_position = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity
