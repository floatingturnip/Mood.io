# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

def getSentiment(entry):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    f = open("journal1.txt", "w")
    f.write(entry)

    path = 'journal1.txt'
    f = open(path)
    text = f.read()

    document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    f = open("sentiments.txt", "a")
    f.write(str(round(sentiment.score, 3)) + "\n")
    f.close()

    f = open("allJournalEntries.txt", "a")
    f.write(text + "\n\n")
    f.close()

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    return sentiment

"""def getMagnitude(entry):
    # Instantiates a client
    client = language.LanguageServiceClient()

    # The text to analyze
    f = open("journal1.txt", "w")
    f.write(entry)

    path = 'journal1.txt'
    f = open(path)
    text = f.read()

    document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)

    # Detects the sentiment of the text
    sentiment = client.analyze_sentiment(document=document).document_sentiment
    f = open("sentiments.txt", "a")
    f.write(str(sentiment.score) + "\n")
    f.close()

    f = open("allJournalEntries.txt", "a")
    f.write(text + "\n\n")
    f.close()

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
    return sentiment.magnitude   """

#this is to analyze the entity sentiment and rank the top ten salience ones.
def sample_analyze_entity_sentiment(text_content):
    """
    Analyzing Entity Sentiment in a String
    Args:
      text_content The text content to analyze
    """

    client = language.LanguageServiceClient()

    # text_content = 'Grapes are good. Bananas are bad.'

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language = "en"
    document = {"content": text_content, "type": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8

    response = client.analyze_entity_sentiment(document, encoding_type=encoding_type)
    
    entList = []
    # Loop through entitites returned from the API
    for entity in response.entities:
        entList.append(entity)
        print(u"Representative name for the entity: {}".format(entity.name))
        # Get entity type, e.g. PERSON, LOCATION, ADDRESS, NUMBER, et al
        print(u"Entity type: {}".format(enums.Entity.Type(entity.type).name))
        # Get the salience score associated with the entity in the [0, 1.0] range
        print(u"Salience score: {}".format(entity.salience))
        # Get the aggregate sentiment expressed for this entity in the provided document.
        sentiment = entity.sentiment
        print(u"Entity sentiment score: {}".format(sentiment.score))
        print(u"Entity sentiment magnitude: {}".format(sentiment.magnitude))
        # Loop over the metadata associated with entity. For many known entities,
        # the metadata is a Wikipedia URL (wikipedia_url) and Knowledge Graph MID (mid).
        # Some entity types may have additional metadata, e.g. ADDRESS entities
        # may have metadata for the address street_name, postal_code, et al.
        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{} = {}".format(metadata_name, metadata_value))

        # Loop over the mentions of this entity in the input document.
        # The API currently supports proper noun mentions.
        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content))
            # Get the mention type, e.g. PROPER for proper noun
            print(
                u"Mention type: {}".format(enums.EntityMention.Type(mention.type).name)
            )

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(u"Language of the text: {}".format(response.language))

    entList.sort(key=lambda x: x.salience, reverse=True)
    f = open("entities.txt", "w")
    count = 1
    for entity in entList:
        print(entity.name)

        f.write(entity.name + " " + str(entity.salience) + "\n")

        count += 1
        if(count == 10):
            break
    
    f.close()
# [END language_entity_sentiment_text]


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--text_content", type=str, default="Grapes are good. Bananas are bad. Journals are interesting. People are exciting. My Computer is crashing. I am very sad"
    )
    args = parser.parse_args()

    sample_analyze_entity_sentiment(args.text_content)


if __name__ == "__main__":
    main()
