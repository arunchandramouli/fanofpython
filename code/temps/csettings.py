
'''
	This file is for configuration related purpose only
'''

'''
	Base URL for the Product
'''


'''
	DEFINE THE csettings.baseurl
'''
baseurl_equipment = "https://www.sunbeltrentals.com/equipment/"

baseurl = "https://www.sunbeltrentals.com"



'''
	FULL PATH OF THE OUTPUT FILE - *.CSV
'''

file_create_op = "records_p.csv"



'''
	Xpath required for fetching related info
'''


home_page_load = "//*[@id='desktopSiteContainer']//div//*"
equipment_catalog_home_page = "//*[@id='desktopContent']//*[@id='mainEquipGrid']/span/a/@href"
more_items = "//*[@id='desktopContent']//*[@id='mainEquipItemsGrid']/div/span/a/@href"
equipment_catalog_home_page_cat = "//*[@id='desktopContent']//*[@id='mainEquipGrid']/span/a/@href"
equipment_catalog_home_page_subcat = "//*[@id='desktopContent']//*[@id='mainEquipGrid']/span/a/@href"


zip_code_ip_textbox = "//*[@id='desktopContent']//*[@id='getRates']//*[@id='getRatesSearch']"
getRatesSearchDate = "//*[@id='desktopContent']//*[@id='getRates']//*[@id='getRatesSearchDate']"

getRatesSearchButton = "//*[@id='desktopContent']//*[@id='getRates']//*[@id='getRatesSearchButton']"



ratePopupPage = "//*[contains(@class,'k-window')]//*[@id='ratePopup']"
selectBranch = "//*[contains(@class,'k-window')]//*[@id='ratePopup']//*[@id='locationsResultsBind']//*[@class='resultContainer']//*[@class='SBGreyButton']"

selectBranchDetailsPage = "//*[@id='locationsResultsBind']//*[@class='resultContainer']//*[@class='SBGreyButton']"


branch_location_p1 = "//*[@id='desktopContent']//*[@id='getRates']//*[@id='getRatesSearchResult']/strong/text()"
branch_location_p2 = "//*[@id='desktopContent']//*[@id='getRates']//*[@id='getRatesSearchResult']/text()"

price_details_p1 = ".//*[@id='mainEquipDetail']//*[@class='RentalRatesRow']/td/label/text()"
price_details_p2 = ".//*[@id='mainEquipDetail']//*[@class='RentalRatesRow']/td/text()"

catClass = "//*[@id='mainEquipDetail']//*[contains(@id,'EquipTabs')]//*[@class='GenSpecs']/ul/li/span[@class='Spec']/text()"

equipmentType = "//*[@id='desktopContent']//*[@id='equipDetailLeft']//*[@class='Breadcrumb']/h1/a[2]/text()"
equipmentTypeCat = "//*[@id='desktopContent']//*[@id='equipDetailLeft']//*[@class='Breadcrumb']/h1/a[3]/text()"
equipmentTypeSubCat = "//*[@id='desktopContent']//*[@id='equipDetailLeft']//*[@class='Breadcrumb']/h1/a[4]/text()"
equipmentPRDName = "//*[@id='desktopContent']//*[@id='equipDetailLeft']//*[@class='PageHeader']/h1/text()"


