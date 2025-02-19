import requests
import lxml.html

html = requests.get('https://store.steampowered.com/explore/new')
doc = lxml.html.fromstring(html.content)
new_releases = doc.xpath('//div[@id="tab_newreleases_content"]')[0]

titles = new_releases.xpath('.//div[@class="tab_item_name"]/text()')
prices = new_releases.xpath('.//div[@class="discount_final_price"]/text()')

tags = []
for tag in new_releases.xpath('.//div[@class="tab_top_item_tags"]'):
    tags.apppend(tag.text_content())

