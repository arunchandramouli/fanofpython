import sys

sys.path.insert(0,"\\Code\\holy\\python\\presentation\\fanofpython\\tests\\code\\turing\\orders\\")

import dev.main

'''
	Code Execution
'''		

if __name__ == "__main__":

	data_set = ["order_number","order_type","order_date","order_sub_total","order_sales_tax","order_total","payment_amount","payment_type","product_name",
	"barcode","sku","cost","product_price","category","sub_category","gross_item_price","total_sales_price","total_product_tax",
	"product_quantity","order_year","order_month","weekpart","daypart","order_week","hourpart"]

	for each_data in data_set:
		dev.main.Processor.initiate(user_input=each_data)

