
'''
	This file is for Configuration related items alone
'''


total_jobs = ".//*[@id='job-search-results']//*[contains(@class,'job-search-paging')]//*[contains(@class,'text-center')]/b[3]"

job_url = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td//a[contains(@class,'anchorLink') and contains(@class,'js-job-link')]/@href"

job_desg = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td//a[contains(@class,'anchorLink') and contains(@class,'js-job-link')]/b"

job_dept = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td[@class='col-md-3']"

job_loc = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td[@class='col-md-2']"

job_date_posted = "//*[@id='job-search-results']//table[contains(@class,'table-striped')]//tr//td[contains(@class,'col-md-2') and contains(@class,'hidden')]"

next_button = ".//*[@id='job-search-results']//div[contains(@class,'job-search-paging') and contains(@class, 'margin-bot')]//div[contains(@class,'text-right')]/a[contains(text(),'Next')]"

