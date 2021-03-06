from db_interface import QueryHandler


class AbstractItem:
    def __init__(self):
        self.id = int()
        self.name = str()
        self.description = str()
        self.order = int()
        self._elements_list = list()
        self._members = list()
        self.model_class = None

    def __contains__(self, element):
        return element in self._elements_list

    def __eq__(self, other):
        return self.id == other.id

    def _add_element(self, element):
        self._elements_list.append(element)
        return self._elements_list

    def _remove_element(self, element):
        try:
            self._elements_list.remove(element)
        except ValueError:  # if element doesnt exist in elements_list
            return None
        return self._elements_list

    def _reorder_elements(self, element, index: int):
        pass

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_order(self, order):
        self.order = order

    def get_order(self):
        return self.order

    def add_member(self, member):
        self._members.append(member)

    def remove_member(self, member):
        try:
            self._members.remove(member)
        except ValueError:  # if element doesnt exist in members
            return None
        return self._members

    def _get_elements_list(self):
        return self._elements_list


