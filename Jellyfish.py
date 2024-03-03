# Created by jin_rh

class Jellyfish:
    """
    Custom class take a collection object and iterate
    """

    def __init__(self, items):
        """
        parameter items: a collection object
        """
        self._index = 0
        self._items = items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return self.JellyfishIterator(self)

    # Nested iterator
    class JellyfishIterator:
        """
        Customised iterator class generating iterator for Jellyfish class

        """

        def __init__(self, obj):
            self._index = 0
            self._obj = obj

        def __iter__(self):
            # iterator
            return self

        def __next__(self):
            """
            Returns the next item from the collection
            for sequence and stop iterating when it reaches the limit

            """
            if self._index >= len(self._obj):
                # When it reaches the end of iteration, throw exception
                raise StopIteration

            else:
                # Return a next item, otherwise
                result = self._obj._items[self._index]
                self._index += 1
                return result

