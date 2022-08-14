from serpapi import GoogleSearch


def search(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": "**********************************************" # enter serpapi key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    organic_results = results["organic_results"]

    return organic_results


