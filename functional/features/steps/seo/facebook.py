import bs4
import json
import re


def content_not_empty(el):
    print('running')
    if re.search(r'content=\"(.*?)\"', el):
        meta_content = re.search(r'content=\"(.*?)\"', el)
        assert meta_content.group(1) != '', 'content section was empty'
    else:
        assert False, 'did not find content on the mata tag'



def find_all_og_elements(content):
    soup = bs4.BeautifulSoup(content, features="html.parser")
    open_graph_meta = soup.findAll('meta', attrs={'property': re.compile('^og:')})
    return open_graph_meta


def get_facebook_og_title(content):
    open_graph_meta = find_all_og_elements(content)
    for element in open_graph_meta:
        element = str(element)
        print(element)
        if re.search(u'property="og:title"', element):
            content_not_empty(element)
            break
        else:
            assert False, 'did not find an og:title element'

def get_facebook_og_description(content):
    open_graph_meta = find_all_og_elements(content)
    for element in open_graph_meta:
        element = str(element)
        if re.search(u'property="og:description"', element):
            content_not_empty(element)
            continue
        else:
            assert False, 'did not find an og:title element'

def get_facebook_og_image(content):
    open_graph_meta = find_all_og_elements(content)
    for element in open_graph_meta:
        element = str(element)
        if re.search(u'property="og:image"', element):
            content_not_empty(element)
            continue
        else:
            assert False, 'did not find an og:title element'


def get_facebook_og_url(content):
    open_graph_meta = find_all_og_elements(content)
    for element in open_graph_meta:
        element = str(element)
        if re.search(u'property="og:url"', element):
            content_not_empty(element)
            continue
        else:
            assert False, 'did not find an og:title element'



# import bs4
# import json
# import re
# from qa.settings import log
#
# def check_content_not_empty(el):
#     if re.search(r'content=\"(.*?)\"', el):
#         meta_content = re.search(r'content=\"(.*?)\"', el)
#         assert meta_content.group(1) != '', 'content section was empty'
#     else:
#         assert False, 'did not find content on the mata tag'
#
#
# def find_all_og_elements(content):
#     soup = bs4.BeautifulSoup(content, features="html.parser")
#     open_graph_meta = soup.findAll('meta', attrs={'property': re.compile('^og:')})
#     return open_graph_meta


# def get_facebook_og_title(content):
#     open_graph_meta = find_all_og_elements(content)
#     for element in open_graph_meta:
#         element = str(element)
#         print(element)
#         if re.search(u'property=\"og:title\"', element):
#             check_content_not_empty(element)
#             continue
#         else:
#             assert False, 'did not find an og:title element'
#
# def get_facebook_og_description(content):
#     open_graph_meta = find_all_og_elements(content)
#     for element in open_graph_meta:
#         if re.search(u'property=\"og:description\"', element):
#             content_not_empty(element)
#         else:
#             assert False, 'did not find an og:description element'
#
# def get_facebook_og_image(content):
#     open_graph_meta = find_all_og_elements(content)
#     for element in open_graph_meta:
#         if re.search(u'property=\"og:image\"', element):
#             content_not_empty(element)
#             continue
#         else:
#             assert False, 'did not find an og:image element'
#
#
# def get_facebook_og_url(content):
#     open_graph_meta = find_all_og_elements(content)
#     for element in open_graph_meta:
#         if re.search(u'property=\"og:url\"', element):
#             content_not_empty(element)
#             continue
#         else:
#             assert False, 'did not find an og:url element'
