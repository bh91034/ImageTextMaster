# Reference :
# - https://blog.katastros.com/a?ID=00650-8d76cc1c-12c6-4ddf-8cc9-7bb4efeefed7
#
# encoding:utf-8 
import re   # Use regular rules to match the desired data 
import requests   # Use requests to get the web page source code 
import pymysql
import urllib
import time
import operator


#Known url download image 
def  getImage (ilt, name) : 
    for g in ilt:
        namestring = 'E://Download/picture3/' + str(name) + '.jpg'   #Storage address + picture name 
        urllib.request.urlretrieve( 'https:' +g[ 3 ], namestring) #Core    download code 
        name = name + 1    #Realize dynamic naming self-increment 
        # print(name)


#Save the data in mysql 
def  data_Import (sql) : 
    conn=pymysql.connect(host = '127.0.0.1' ,user = 'root' ,password = 'rootadmin' ,db = 'test' ,charset = 'utf8' )     
    #Connect to the database conn.query(sql) #Insert data
    conn.commit()
    conn.close()

# Get the link passed by the main function 
def  getHtmlText (url) : 
    try :   # Exception handling 
        # Get the URL link you passed in and set the timeout time of 3 seconds 
        r = requests.get(url, timeout = 3 )
         # Determine its http status code
        r.raise_for_status()
        # Set its encoding encoding is to set its header encoding apparent_encoding is to analyze its encoding format from the returned webpage
        r.encoding = r.apparent_encoding
        # Return to source code 
        return r.text
    except : # If an exception occurs, return empty 
        return  ''

# Parse your web page information 
def  parsePage (ilt, html) : 
    # Exception handling 
    try :
         # Find the price of the schoolbag 
        plt = re.findall( r'\"view_price\"\:\"[\d\.]*\" ' , html)
         # Find the name of the schoolbag 
        tlt = re.findall( r'\"raw_title\"\:\".*?\"' , html)
         # Find the address of the schoolbag 
        # add = re.findall(r'/"item_loc\"\:\".*?\"', html) 
        #nid 
        nid = re.findall( r'\"nid\"\:\"[\d]*\"' , html)
         # find school bag The picture link 
        img = re.findall( r'\"pic_url\"\:\".*?\"' ,
        html) # Sales 
        sales = re.findall( r'\"view_sales\"\:\".*?\"', html)
         # print(sales) 
     # print("https://item.taobao.com/item.htm?id="+nid) 
        # Get this content into the list in the main function 
        for i in range(len( plt)):
            price = eval(plt[i].split( ':' )[ 1 ])
            title = eval(tlt[i].split( ':' )[ 1 ])
            address = eval(nid[i].split( ':' )[ 1 ])
            imgs = eval(img[i].split( ':' )[ 1 ])
            sale = eval(sales[i].split( ':' )[ 1 ])
            ilt.append([price, title, address, imgs, sale])
    except :   # Release an exception and output an empty string 
        print( '' )

# Get the list passed by the main function 
def  printGoodsList (ilt, name, categoryid) : 
    # Use tplt to separate each column 
    tplt = '{:^4}\t{:^8}\t{: ^16}\t{:^16}\t{:^32}\t{:^32}' 
    #Sort by price from small to large^10 
    # ilt.sort() 
    createtime = '2018-04-03' 
    store = 'Taobao/Tmall' 
    for g in ilt:
        sql = """insert into taobao(categoryid,name,price,description,createtime,picture,store,url,monthly_sales) values('%d','%s','%s','%s',' %s','%s','%s','%s','%s')""" % (categoryid, pymysql.escape_string(g[ 1 ]), g[ 0 ], pymysql.escape_string( g[ 1 ]), createtime, 'images/upload/' + str(name) + '.jpg' , store, "https://item.taobao.com/item.htm?id=" +g[ 2 ] , g[ 4 ])
        data_Import(sql)
        # print("Congratulations, successfully written"+str(count)+"data!") 
        name = name + 1   # Picture name plus one

# Define the main function main 
def  main () : 
    # name = int(time.time())-31736 # Get the timestamp of the current time to avoid conflicts 
    name = 1524632649 + 44 
    goods_list = [ 'fashion suit' , 485 , 'leather ' , 486 , 'suit' , 487 , 'T-shirt' , 488 , 'original design' , 489 , 'jacket' , 490 , 'casual pants' , 491 , 'jeans' , 492 , 'windbreaker' , 493 , ' denim jacket',494 , 'baseball uniform' , 495 , 'sports jacket' , 496 , 'POLO shirt' , 497 , 'suit' , 498 , 'wearing guide' , 499 , 'long sleeve pajamas' , 500 , 'coral fleece pajamas' , 501 , 'Padded pajamas' , 502 , 'Stockings' , 503 , 'Underwear suits' , 504 , 'Leggings' , 505 , 'One-piece pajamas' , 506 , 'Night skirt women winter' ,507 ]
    for i in range(len(goods_list)):
         if i% 2 == 0 :
            goods = goods_list[i] # What you want to search for 
            categoryid = goods_list[i+ 1 ]
            print(goods+ ":" +str(categoryid))
            depth = 1   # You want to get a few pages of things 
            start_url = 'https://s.taobao.com/search?q= ' + goods + '&sort=sale-desc'  # Your search URL plus your search Things, sorted by sales 
            infoList = [] # A custom empty list is used to store your data 
            for i in range(depth): # Cycle your pages 
                try : # Exception handling 
                    url = start_url + '&s' + str( 44 * i) # Get your URL 
                    print ('url=', url)
                    #html = getHtmlText(url) # Get the url and pass it into the function you want to get the url 
                    #parsePage(infoList, html) # Get your html source code and put it into the parsed webpage 
                except : # Abnormal skip occurred
                    continue 
            # Put the data in the list into the parsed function
            #printGoodsList(infoList, name, categoryid)
            #getImage(infoList, name)
            time.sleep( 7 )   # sleep for 5 seconds 
            name = name + 44
            print(name)

main() # call the main function