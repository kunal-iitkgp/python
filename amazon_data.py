import sys 
import requests 
import lxml.html 

#sudo pip install requests==1.2.3 lxml==3.2.1


def getProduct(id): 
	
	hxs = lxml.html.document_fromstring(requests.get("http://www.amazon.in/gp/product/"+id).content)
	movie = {}
	
	try:
		movie['Product Name'] = hxs.xpath('//*[@id="productTitle"]/text()')[0].strip()
	except IndexError:
		movie['Product Name'] = ""
	
	hxs_1 = lxml.html.document_fromstring(requests.get("http://www.amazon.in/gp/offer-listing/"+id+"/ref=dp_olp_new_mbc?ie=UTF8&condition=new").content)
	try:
		movie['sellers'] = hxs_1.xpath('//*[@id="olpTabContent"]//h3/a/img/@alt')
	except IndexError:
		movie['sellers'] = []

	try:
		movie['positive_ratings%'] = hxs_1.xpath('//*[@id="olpTabContent"]//a/b/text()')
	except IndexError:
		movie['positive_ratings%'] = []

	try:
		movie['sellers_link_as_provided_by_amazon'] = hxs_1.xpath('//*[@id="olpTabContent"]/div/div[2]/div//h3//@href')
	except IndexError:
		movie['sellers_link_as_provided_by_amazon']=[]

 
	try:
		movie['star_ratings'] = hxs_1.xpath('//*[@id="olpTabContent"]/div/div/div/div[3]/p/i/@class')
	except IndexError:	
		movie['star_ratings']=[]
		

	
	return movie

if __name__ == "__main__":

	details =  getProduct("9352030613")
	product_id="9352030613"
	for i in details:
		print i," = ",details[i],"\n"
	list_p=[]	

	for i in details['sellers_link_as_provided_by_amazon']:
		if i[0]== 'h':
			seller_id = i[27:]
			print seller_id
			hxs_2 = lxml.html.document_fromstring(requests.get("http://www.amazon.in/gp/aag/main?ie=UTF8&asin="+product_id+"&isAmazonFulfilled=0&seller="+seller_id).content)
			try:
				list_p.append(hxs_2.xpath('//*[@id="feedbackList"]/li//li/text()'))

			except IndexError:
				pass
		else:
			hxs_2 = lxml.html.document_fromstring(requests.get("http://www.amazon.in"+i).content)
			try:
				list_p.append(hxs_2.xpath('//*[@id="feedbackList"]/li//li/text()'))
			except IndexError:
				pass
details['star_p']=list_p
print details


#	'//*[@id="fk-mainbody-id"]/div/div[7]/div/div[3]/div/div/div[1]/h1/text()'
#//*[@id="fk-mainbody-id"]/div/div[7]/div/div[3]/div/div/div[1]/h1

#//*[@id="fk-mainbody-id"]/div/div[8]/div/div/div/div[3]/div[1]/table/tbody/tr/td[1]/div/div/a
#id('olpTabContent')/x:div/x:div[2]/x:div/x:div/x:h3//x:a/