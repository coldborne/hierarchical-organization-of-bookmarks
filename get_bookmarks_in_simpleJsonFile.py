import json


def extract_bookmarks(bookmarks_file_path, output_file_path):
    with open(bookmarks_file_path, 'r', encoding='utf-8') as file:
        bookmarks_data = json.load(file)

        def dfs(nodes):
            for node in nodes:
                if node['type'] == 'url':
                    extracted_bookmarks.append({'name': node.get('name'), 'url': node.get('url')})
                elif node['type'] == 'folder' and 'children' in node:
                    dfs(node['children'])

        extracted_bookmarks = []

        for root_key, root_value in bookmarks_data['roots'].items():
            if root_key == 'bookmark_bar':
                if 'children' in root_value:
                    dfs(root_value['children'])

        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(extracted_bookmarks, file, indent=4, ensure_ascii=False)


bookmarks_file_path = 'path_to_your_BookmarksFile'
output_file_path = 'simple_bookmarks.json'

extract_bookmarks(bookmarks_file_path, output_file_path)
