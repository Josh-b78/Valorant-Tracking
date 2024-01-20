from bs4 import BeautifulSoup
import requests


url = "https://books.toscrape.com/"

page_to_scrape = requests.get(url)
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

books = soup.find_all("aritcle", class_= "product-pod")
price = soup.find_all("p", class_ = "price_color")




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