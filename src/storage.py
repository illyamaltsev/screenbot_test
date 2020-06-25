class ScreenStorage:

    def __init__(self):
        self.storage = {}

    def save_file_path(self, url: str, path: str):
        self.storage[url] = path

    def get_file_path_by_url(self, url: str):
        return self.storage[url] if url in self.storage else None