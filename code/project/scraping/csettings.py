
'''
	This file is for configuration related purpose only
'''

'''
	Base URL for the Product
'''


'''
	DEFINE THE csettings.baseurl
'''
baseurl = "https://sites.google.com/site/gamedatalibrary/software-by-year/"



'''
	FULL PATH OF THE OUTPUT FILE - *.CSV
'''

file_create_op = "records.csv"



'''
	Xpath required for fetching game related info
'''

inner_iframe_awesome_table_rows_pag_next = "//*[@id='middleContainer']//*[@id='count']//*[@id='pagination']//*[contains(@class,'goog-inline')]//*[@class='google-visualization-table-page-next']"

inner_iframe_awesome_table_rows_count_3 = "//*[@id='middleContainer']//*[@id='count']//*[@class='numberOfResultsShown']/b[3]"

inner_iframe_awesome_table_rows_count_2 = "//*[@id='middleContainer']//*[@id='count']//*[@class='numberOfResultsShown']/b[2]"

inner_iframe_awesome_table_rows_count_1 = "//*[@id='middleContainer']//*[@id='count']//*[@class='numberOfResultsShown']/b[1]"

inner_iframe_awesome_table_headers = "//*[@id='middleContainer']//*[@id='parentChart1']//*[@class='google-visualization-table']//table//thead/tr/th[contains(@class,'google-visualization-table')]"

inner_iframe_awesome_table_rows_curr_td = "//*[@id='middleContainer']//*[@id='parentChart1']//*[@class='google-visualization-table']//table//tbody/tr[contains(@class,'google-visualization-table')][%s]/td"


inner_iframe_awesome_table_rows = "//*[@id='middleContainer']//*[@id='parentChart1']//*[@class='google-visualization-table']//table//tbody/tr[contains(@class,'google-visualization-table')]"

inner_iframe_awesome_table_middle_container = "//*[@id='middleContainer']//table//tr//td"

inner_iframe_awesome_table = "//*[@dir='ltr']//*[contains(@class,'tabcontent')]/iframe"

iframe_body = "//*[@dir='ltr']//*"

iframe_game_data = "//*[@id='body']//*[contains(@id,'canvas') and contains(@id,'sites') and @role='main']//table//div[@dir='ltr']//*[contains(@class,'sites-embed-content')]/iframe"

page_load_games_full_content = "//*[@id='body']//*[contains(@id,'canvas') and contains(@id,'sites') and @role='main']//table//div[@dir='ltr']/div/a[1]"


page_load = "//*[@id='body']//*"

