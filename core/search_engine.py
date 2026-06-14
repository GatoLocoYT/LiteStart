from core.app_indexer import get_installed_apps

APPS_CACHE = get_installed_apps()


def calculate_score(query, item_name):

    query = query.lower().strip()

    item_name = item_name.lower()

    if item_name == query:
        return 100

    if item_name.startswith(query):
        return 80

    if query in item_name:
        return 50

    return 0


def search(query):

    query = query.strip()

    if not query:
        return []

    scored_results = []

    for app in APPS_CACHE:

        score = calculate_score(
            query,
            app["name"]
        )

        if score > 0:

            scored_results.append(
                (
                    score,
                    app["name"]
                )
            )

    scored_results.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return [
        name
        for score, name in scored_results
    ]