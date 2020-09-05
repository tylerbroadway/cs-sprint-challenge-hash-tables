# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    result = []

    for file in files:
        key = file.split("/")[-1]

        if key not in cache:
            cache[key] = []

        cache[key].append(file)

    for query in queries:
        if query in cache:
            result += cache[query]

    return result

if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
