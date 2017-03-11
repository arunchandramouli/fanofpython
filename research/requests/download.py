


import requests


URL = "http://www.iea.org/statistics/monthlystatistics/monthlyelectricitystatistics/"

links = ["http://www.iea.org/media/statistics/surveys/electricity/MES201609.XLS","http://www.iea.org/media/statistics/surveys/electricity/MES201606.XLS",
"http://www.iea.org/media/statistics/surveys/electricity/MES201607.XLS"]




for urls in links:

	files = requests.get(urls)
	file_name = urls.split('/')[-1]
	print 'File name %s '%file_name
	with open(file_name,'wb') as writer:

		 writer.write(files.content)