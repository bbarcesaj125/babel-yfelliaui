import requests
from requests.exceptions import HTTPError
import json
from bs4 import BeautifulSoup

""" This is a program that takes in a list of urls and then tries to extract information (e.g. Page's title) from them
using BeautifulSoup. """


F_URL = "url"
F_STATUS = "status_code"
F_META = "metadata"
F_CONTENT = "content"
dic_list = []
dic_nested_bs = []


def get_urls(arglist, is_verbose=False):
    for url in arglist:
        try:
            res = get(url)
        except HTTPError as http_err:
            print(f"Other error occured: {http_err}")
            print(str(http_err))
            res = None
        except Exception as err:
            print(f"Other error occurred: {err}")

        else:
            print("Success!")

            display_url(res, is_verbose=False)
            dic_list_new = write_to_dic(res, is_verbose=False)
            write_to_file(dic_list_new)


def get(url):
    user_agent_text = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    header_dict = {"user-agent": user_agent_text}
    res = requests.get(url, headers=header_dict)
    # print(res.headers)
    res.raise_for_status()
    return res


def write_to_dic(res, is_verbose):
    """ This function calls search_meta_bs4() to extract the metadata and then places them in a dictionary. """

    meta_data = search_meta_bs4(res.text)

    dic = {
        F_URL: res.url,
        F_STATUS: res.status_code,
        F_META: meta_data,
        F_CONTENT: res.text[:45],
    }

    dic_list.append(dic)
    return dic_list


def search_meta_bs4(res):
    """ This function extracts the metadata of an HTML page using BeautifulSoup. """

    soup = BeautifulSoup(res, "lxml")
    title = soup.find("meta", property="og:title")
    description = soup.find("meta", property="og:description")
    image = soup.find("meta", property="og:image")

    title_final = title["content"] if title else "No meta title given!"
    description_final = (
        description["content"] if description else "No meta description given!"
    )
    image_final = image["content"] if image else "No meta image given!"

    dic = {
        "title": title_final,
        "description": description_final,
        "image": image_final,
    }

    return dic


def search_title(text):
    """ ***OBSOLETE*** This is a function extracts the title of an HTML page. """

    retbuffer = begin = 0
    end = None
    begin = text.find("<title>")
    if begin != -1:
        begin += len("<title>")
        end = text[begin:].find("</title>")
        if end != -1:
            end += begin
            retbuffer = text[begin:end]
    print(f"Test search_title : {begin}, {end}, {retbuffer}")
    return retbuffer


def write_to_file(list_data):
    with open("json_file.json", "w") as output_file:
        json.dump(list_data, output_file)


def display_url(res, is_verbose=False):

    if res:
        print(f"--> There are {len(res.text)} Bytes in {res.url}")
        if is_verbose:
            print("Status :", res.status_code)
            # print("Headers :", res.headers)
            # print("Text :", res.text)
            for key, value in res.headers.items():
                print(f"{key} : {value}")
            print("_" * 30)
            print(res.text[:1000])

        else:
            print("Status :", res.status_code)
            print("Url :", res.url)
    else:
        print("Response is Null!")


if __name__ == "__main__":
    url_list = [
        "https://www.crummy.com/software/BeautifulSoup/bs4/doc/",
        "https://api.github.com/invalid",
        "https://www.whatismybrowser.com/detect/what-is-my-user-agent",
        "https://www.reddit.com/",
        "https://stackoverflow.com/",
    ]

    get_urls(url_list)
