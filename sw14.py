list1 = [{'year':1996, 'month':12},
         {'year':1997, 'month':12},
         {'year':2006, 'month':11},
         {'year':2006, 'month':11},]
common = [ ]
def popularbirthdays(birthdays):
    for i in list1:
        if 'month' in i:
            common.append(i['month'])
   
    popular = {}
    x = set(common)
    for i in x:
        popular.update({i : common.count(i)})   
     
    maxvalue = max(popular.values())
    maxkeys = []
    for key,value in popular.items():
         if value==maxvalue:
             maxkeys.append(key)

    months = ["January", "Feburary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    output = ""
    for i in maxkeys:
        output += str(months[i-1])+", "

    return output[:-2]    

# print(popularbirthdays(list1))

products = ["eggs", "butter", "cheese"]
productPrices = [2.89, 5.00, 3.25]
productsSold = ["eggs", "eggs", "cheese", "butter"]
soldPrice = [2.79, 2.89, 3.25, 5.00 ]
def priceCheck(products, productPrices, productsSold, soldPrice):
    main1 = dict(zip(products, productPrices))
    main2 = dict(zip(productsSold, soldPrice))
    print(main1)
    print(main2)


# print(priceCheck(products, productPrices, productsSold, soldPrice))   


def priceCheck(products, productPrices, productsSold, soldPrice):
    errorCount = 0

    # Create a dictionary to store the prices of products
    priceDict = dict(zip(products, productPrices))

    # Iterate over the sold products and compare their prices
    for i in range(len(productsSold)):
        product = productsSold[i]
        actualPrice = priceDict.get(product)
        if actualPrice != soldPrice[i]:
            errorCount += 1

    print(errorCount)

# Example usage
products = ['apple', 'banana', 'orange']
productPrices = [0.5, 0.25, 0.75]
productsSold = ['apple', 'banana', 'orange', 'apple']
soldPrice = [0.5, 0.3, 0.75, 0.5]

# priceCheck(products, productPrices, productsSold, soldPrice)

l1 = [[104,97],[105,105], [106,115],[97,104],[98,97]]
s = "hijab"
def wordMorph(mapping, s):
    dic = {}
    for i in mapping:
        dic.update({chr(i[0]): chr(i[1])})
    out = ""
    for i in s:
        if i in dic:
            out += dic[i]

    return out
print(wordMorph(l1,s))     



def mapping(a, b):
    d = {}
    for i in range(len(a)):
        if a[i] in d:
            if d[a[i]] != b[i]:
                return False
        else:
            d[a[i]] = b[i]
    return True