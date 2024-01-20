from bs4 import BeautifulSoup
import requests


url = "https://books.toscrape.com/"
valorant_page = "https://tracker.gg/valorant/profile/riot/Otto%230tto/matches"


page = requests.get(valorant_page)
soup = BeautifulSoup(page.text, "html.parser")

test = soup.find("div", class_ = "trn-gamereport-list trn-gamereport-list--compact")
print(test)


#test = soup.find("data-v-63b27203", class_ = "trn-match-row__text-value")
#test = soup.find_all("div", class_= "trn-match-row__text-value")
#print(test)
#books = soup.find_all("aritcle", class_= "product-pod")
#price = soup.find_all("p", class_ = "price_color")




#I think this is the path to the data element I want to extract
'''
> div.trn-wrapper 
> div.trn-container 
> div 
> main 
> div.content.no-card-margin 
> div.site-container.trn-grid.trn-grid--vertical.trn-grid--small 
> div.trn-grid__sidebar-left 
> div:nth-child(2) 
> div 
> div.trn-gamereport-list.trn-gamereport-list--compact 
> div:nth-child(1) 
> div.trn-gamereport-list__group-entries 
> div.vmr.trn-match-row.trn-match-row--outcome-loss.cursor-pointer 
> div.vmr-stats.trn-match-row__section.trn-match-row__section--right.gap-4 
> div.trn-match-row__block.min-w-24 
> div.trn-match-row__text-value
'''