import json


class Bookmark:
    def __init__(self, name, url):
        self.name = name
        self.url = url


class Folder:
    def __init__(self, name):
        self.name = name
        self.children = []


def process_bookmarks(node):
    if node['type'] == 'url':
        return Bookmark(node.get('name'), node.get('url'))
    elif node['type'] == 'folder':
        folder = Folder(node.get('name'))

        for child in node.get('children', []):
            folder.children.append(process_bookmarks(child))

        return folder


def serialize_structure(node):
    if isinstance(node, Bookmark):
        return {'type': 'url', 'name': node.name, 'url': node.url}
    elif isinstance(node, Folder):
        children = [serialize_structure(child) for child in node.children]
        return {'type': 'folder', 'name': node.name, 'children': children}


def extract_and_reorganize_bookmarks(bookmarks_file_path, output_file_path):
    with open(bookmarks_file_path, 'r', encoding='utf-8') as file:
        bookmarks_data = json.load(file)

    root = bookmarks_data['roots']['bookmark_bar']
    processed_root = process_bookmarks({'type': 'folder', 'name': 'Root', 'children': root['children']})

    reorganized_data = serialize_structure(processed_root)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(reorganized_data, file, indent=4, ensure_ascii=False)


bookmarks_file_path = 'path_to_your_BookmarksFile'
output_file_path = 'bookmarks.json'

extract_and_reorganize_bookmarks(bookmarks_file_path, output_file_path)
