__author__ = 'cmotevasselani'



url_mock = {
    1: [2, 3, 5],
    2: [4, 6, 7],
    3: [1, 2, 5],
    4: [4, 8, 9],
    5: [3, 6, 7],
    6: [1, 5, 9],
    7: [4, 8, 9],
    8: [1, 2, 3],
    9: [4]
}


def mock_follow_urls(url):
    return url_mock[url]

def get_urls_at_level_recursive(root_url, level, urls):
    urls.append(mock_follow_urls(root_url))



    return urls






urls_at_level = get_urls_at_level_recursive(3, [])
print "urls at level 3: " + ''.join([str(x) for x in urls_at_level])
