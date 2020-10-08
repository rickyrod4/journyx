# Please write code that takes a chat message string as input and returns a JSON
# formatted string containing information about its contents. 
# You should look for at least the following features:...

 
#" 1) @mentions - This is a way to mention another user
#     They always start with '@' and end when hitting a non-word character
# 
# 2) Links - Any URLs that are contained in the message, plus the page's current
#    HTML title up to 200 characters max. You can assume that all URLs start with http.
#
# 3) Emoticons - for this exercise, you can assume that emoticons are defined as any
#    alphanumeric string, no longer than 15 characters with no whitespace, contained in parentheses.
# 
# 3) An integer word cound of the remaining words, not counting any 
#    @mentions, links or emoticons 
# "


def jounyx_string():
    from urllib.request import urlopen
    from html.parser import HTMLParser
    import urllib
    #"""'
    # Get the input messaage from the user
    # go thru the string imported
    # Classify which case is going on basaed on the input
    # convert to JSON formatted string
    # return the JSON String"

    json_string = {}

    # Get the input messaage from the user
    message = input("Please enter your message: ")
    message_object = message.split(" ")

    #pre-set JSON formatted list
    word_count = 0
    #mentions
    mentions_list = []
    #links
    links_list = []
    links_content = {}
    #emoticons
    emoticons_list = []


    # go thru the string imported
    # Classify which case is going on basaed on the input
    for word in message_object:
        #Link if/else statement
        if(word.find('http',0,5) != -1):
        #open page
        #rerieve url title
            url = word
            def error_callback(*_, **__):
                pass

            def is_string(data):
                return isinstance(data, str)

            def is_bytes(data):
                return isinstance(data, bytes)

            def to_ascii(data):
                if is_string(data):
                    data = data.encode('ascii', errors='ignore')
                elif is_bytes(data):
                    data = data.decode('ascii', errors='ignore')
                else:
                    data = str(data).encode('ascii', errors='ignore')
                return data


            class Parser(HTMLParser):
                def __init__(self, url):
                    self.title = None
                    self.rec = False
                    HTMLParser.__init__(self)
                    try:
                        self.feed(to_ascii(urlopen(url).read()))
                    except urllib.error.HTTPError:
                        return
                    except urllib.error.URLError:
                        return
                    except ValueError:
                        return

                    self.rec = False
                    self.error = error_callback

                def handle_starttag(self, tag, attrs):
                    if tag == 'title':
                        self.rec = True

                def handle_data(self, data):
                    if self.rec:
                        self.title = data

                def handle_endtag(self, tag):
                    if tag == 'title':
                        self.rec = False

            def get_title(url):
                return Parser(url).title

            links_content["url"] =  word
            links_content["title"] = get_title(url)
            links_list.append(links_content)
            

        # @Mention if/else statement
        elif(word.find('@',0,1)!= -1):
            word = word.replace('@','')
            mentions_list.append(word)
            
        # Emoticon if/else statement
        elif('(' in word and len(word)<=17 and ')' in word):
            word = word.replace('(','')
            word = word.replace(')','')
            emoticons_list.append(word)
            
        #establish the number of words that arent in the previous 3 cases
        else:
            word_count += 1
            json_string["words"] = word_count


    #formating JSON String
    if(mentions_list):
        json_string["mentions"] = mentions_list
    if(links_list):
        json_string["links"] = links_list
    if(emoticons_list):
        json_string["emoticons"] = emoticons_list

    #json format print and return the result
    import json
    result = json.dumps(json_string, indent=2, sort_keys=True)
    print(result)
    return result


jounyx_string()