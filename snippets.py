import logging
import argparse
import sys

#set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
    """
    Store a snippet with an associate name
    Returns the name and the snippet
    """
    
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    return name, snippet
    
def get(name):
    """
    Retrieve the snippet with a given name
    If there is no such snippet...error will be reported to snippets.log and no snippet will be returned
    Returns the snippet
    """
    
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
def remove(name, snippet):
    
    
    logging.error("FIXME: Unimplemented - remove({!r})".format(name))
    

# python snippets.py put list "A sequence of things - created using []"

action ="put"
form = "list"
snippet = "A sequence of things - created using []"


def main():
    """main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
    arguments = parser.parse_args(sys.argv[1:])

if __name__ == "__main__":
    main()