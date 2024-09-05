class scraper:
    from bs4 import BeautifulSoup as btfs
    from article import Article
    import requests, re
    from analyzeSentiment import polarity_scores
    import csv


    html = requests.get("https://news.yahoo.com/").text
    soup = btfs(html,"html.parser")


    headlines = soup.find_all("h3")
    headlines = headlines[12:len(headlines)-3]

    images = soup.find_all("img")
    images = images[8:58]

    descriptions = soup.find_all("p")
    descriptions = descriptions[2:52]

    sources = soup.find_all("span", attrs={"class":"Ell"})

    article = [Article] 
    headline_titles = []
    headline_image = []
    headline_description = []
    headline_source =[]
    headline_sentiment = []


    #Image scraper
    for image in images:
        image = str(image)
        match = re.search(r'src="([^"]+)"', image)
        extracted_image = match.group(1)
        headline_image.append(extracted_image)

    for image in headline_image:
        print(image)

    #Headliner scraper
    for headline in headlines:
        headline = str(headline)
        match = re.search(r'>([^<]+)<', headline)
        extracted_headline = match.group(1)
        headline_titles.append(extracted_headline)
        sentiment_Dict = polarity_scores(extracted_headline)
        if (sentiment_Dict["neg"] > sentiment_Dict["pos"]):
            headline_sentiment.append("-"+str(sentiment_Dict["neg"]))
        else:
            headline_sentiment.append(sentiment_Dict["pos"])

    for headline in headline_titles:
        print(headline)
    print("\n")

    # Description scraper
    for description in descriptions:
        description = str(description)
        match = re.search(r'>(.*?)<', description)
        extracted_description = match.group(1)
        headline_description.append(extracted_description)
    for description in headline_description:
        print(description)

    # Source scraper
    print(sources[0])
    for source in sources:
        source = str(source)
        match = re.search(r'>(.*?)<', source)
        extracted_source = match.group(1)
        headline_source.append(extracted_source)
    for source in headline_source:
        print(source)
    for sentiment in headline_sentiment:
        print(sentiment)

    # Writes to CSV
    file = open("scraped_quotes.csv","w")
    writer = csv.writer(file)
    writer.writerow(["TITLE", "SENTIMENT", "SOURCE", "DESCRIPTION", "IMAGE"])
    
    for i in range(50):
        writer.writerow([headline_titles[i], headline_sentiment[i], headline_source[i], headline_description[i], headline_image[i]])
    file.close()

