import xml.etree.ElementTree as ET


class Config:
    def __init__(self, file_path):
        self.file_path = file_path
        self.params = {}
        self.groups = {}
        self.load()

    def get(self, name: str, group: str = None, default: str = None) -> str:
        """
        :param name:    Name of parameter (str)
        :param group:   Name of group (optional str)
        :param default: Default value (optional)
        :return: value (str)
        """
        if group is None:
            if name in self.params:
                return self.params[name]
            else:
                return default
        else:
            if group in self.groups:
                if name in self.groups[group]:
                    return self.groups[group][name]
                else:
                    return default

    def set(self, name: str, value: str, group: str = None):
        """
        :param name:    Name of parameter (str)
        :param value:   Value of parameter (str)
        :param group:   Name of group (optional str)
        """
        if group is None:
            self.params[name] = value
        else:
            if group not in self.groups:
                self.groups[group] = {}
            self.groups[group][name] = value
        self.save()

    def save(self):
        root = ET.Element("config")
        for name, value in self.params.items():
            param_elem = ET.SubElement(root, "param", name=name)
            param_elem.text = str(value)
        for group_name, group_dict in self.groups.items():
            group_elem = ET.SubElement(root, "group", name=group_name)
            for name, value in group_dict.items():
                param_elem = ET.SubElement(group_elem, "param", name=name)
                param_elem.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def load(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            self.save()
            self.load()
            return
        root = tree.getroot()
        for param_elem in root.findall("param"):
            name = param_elem.get("name")
            value = param_elem.text
            self.set(name, value)
        for group_elem in root.findall("group"):
            group_name = group_elem.get("name")
            for param_elem in group_elem.findall("param"):
                name = param_elem.get("name")
                value = param_elem.text
                self.set(name, value, group_name)

    def get_params(self):
        return list(self.params.keys())

    def get_groups(self):
        return list(self.groups.keys())

    def list_group(self, group: str):
        return list(self.groups[group].keys())


def test():
    c = Config('test.xml')
    c.set('test', 'test')
    c.set('test2', 'test2')
    c.set('test',  'test in group', group='test_group')
    print(c.get_params())
    print(c.get_groups())
    print(c.list_group('test_group'))


def test_load():
    c = Config('test.xml')
    print(c.get_params())
    print(c.get_groups())
    print(c.list_group('test_group'))


if __name__ == "__main__":
    test_load()
