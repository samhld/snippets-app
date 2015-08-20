import logging, argparse, sys, psycopg2


#set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect("dbname='snippets'")
logging.debug("Database connection established.")

def put(name, snippet):
    """
    Store a snippet with an associate name
    Returns the name and the snippet
    """

    logging.info("Storing snippet {!r}: {!r}".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    # cursor.execute(command, (name, snippet))
    try:
        command = "insert into snippets values (%s, %s)"
        cursor.execute(command, (name, snippet))
    except psycopg2.IntegrityError as e:
        connection.rollback()
        command = "update snippets set message=%s where keyword=%s"
        cursor.execute(command, (snippet, name))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet    
    
def get(name):
    """
    Retrieve the snippet with a given name
    If there is no such snippet...error will be reported to snippets.log and no snippet will be returned
    Returns the snippet
    """
    
    logging.info("Retrieving snippet {!r}".format(name))
    with connection, connection.cursor() as cursor:
        cursor.execute("select message from snippets where keyword=%s", (name,))
        row = cursor.fetchone()
    logging.debug("Snippet retrieved successfully.")
    
    # if not snippet:
    #     logging.debug("There is no snippet under that keyword")
        
    return snippet

def cat():
    logging.info("Retrieving keywords")
    cursor = connection.cursor()
    cursor.execute("select keyword from snippets")
    keywords = cursor.fetchall()
    connection.commit()
    
def strContained(strInput):
    logging.info("Retrieving snippets")
    cursor = connection.cursor()
    cursor.execute("select keyword from snippets where message like '%%s%'", (strInput,))
    messages = cursor.fetchall()
    
def remove(name, snippet):
    
    
    logging.error("FIXME: Unimplemented - remove({!r})".format(name))
    

# python snippets.py put list "A sequence of things - created using []"

action ="put"
form = "list"
snippet = "A sequence of things - created using []"


def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve information to and from 'snippets' table")

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")
    
    logging.debug("Constructing get subparsr")
    get_parser = subparsers.add_parser("get", help="Retrieve a snippet")
    get_parser.add_argument("name", help="The name of the snippet")
    
    logging.debug("Constructing catalog subparser")
    cat_parser = subparsers.add_parser("cat", help="Retrieve list of all keywords")
    
    logging.debug("Constructing string finder subparser")
    str_parser = subparsers.add_parser("contstr", help="Finds string stored within a snippet")
    
    
    arguments = parser.parse_args(sys.argv[1:])
    
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))

if __name__ == "__main__":
    main()