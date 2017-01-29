
'''
	This file is for Configuration related items alone
'''


total_jobs = ".//*[@id='job-search-results']//*[contains(@class,'row job-search-paging') and not(contains(@class,'block-margin-bot'))]//*[contains(@class,'text-center')]/b[3]/text()"

job_url = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td//a[contains(@class,'js-job-link')]/@href"

job_desg = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td//a[contains(@class,'js-job-link')]/b/text()"

job_dept = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td[@class='col-md-3']/text()"

job_loc = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td[@class='col-md-2']/text()"

job_date_posted = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td[contains(@class,'col-md-2') and contains(@class,'hidden')]/text()"

next_button = ".//*[@id='job-search-results']//div[contains(@class,'job-search-paging') and contains(@class, 'margin-bot')]//div[contains(@class,'text-right')]/a[contains(text(),'Next')]"

wait_xpath = "//*[@id='job-search-results']//table//*"

wait_xpath_search = "//*[@id='job-search-results']"

quit_xpath = "//*[@id='job-search-results']//*[contains(@class,'warn')]"