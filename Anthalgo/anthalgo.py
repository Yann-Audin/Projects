def fetch_data(url: str) -> pd.DataFrame:
    """
    Loop on the pages and fetch the data from the endpoint.

    Args:
        url (str): The basic url of the page
    Returns:
        df (pd.DataFrame): The data of the pages
    """
    
    heads = ["id", "book", "fragment", "text_grc", "text_fra", "text_eng", "author", "keywords"]
    
    i = 1
    # loop through all pages
    while True:
        # If we've reached the end of the endpoint, break
        if i > 83:
            break
        # Get the next page
        url = url + str(i)
        i += 1
        # Get the page
        try:
            response = requests.get(url)
            break
        except Exception as e:
            print("Error:", e)
            break
        # Get the json data from the page
        page_text = response.text
        page_json = json.loads(page_text)
        # Loop through the json data of the page
        for item in page_json:
            # Loop through each item in the json data
            for key in heads:
                # If the key is in the json data
                if key in item.keys():
                    # Add the value to the csv file
                    csv_writer.writerow([item[key]])
        # Pause for 1 second
        time.sleep(1)
        
        