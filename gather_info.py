from lxml import html
import requests


user_input = "alter-self"
page = requests.get("http://www.orcpub.com/dungeons-and-dragons/5th-edition/spells/{}".format(user_input))
tree = html.fromstring(page.content)

spell_card = tree.xpath('//*[@id="app"]/div/div[3]')
spell_name = tree.xpath('//*[@id="app"]/div/div[3]/h1/span/text()')[0]
school_lvl = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[1]/em/text()')[0]
cast_time_title = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[2]/strong/text()')[0]
cast_time = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[2]/span/text()')[0]
range_title = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[3]/strong/text()')[0]
spell_range = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[3]/span/text()')[0]
comp_title = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[4]/strong/text()')[0]
components = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[4]/span/text()')[0]
dur_title = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[5]/strong/text()')[0]
duration = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[5]/span/text()')[0]
description = tree.xpath('//*[@id="app"]/div/div[3]/div/div[1]/div/div/div[6]/p/text()')


print_me = [spell_card, spell_name, school_lvl, cast_time_title, cast_time, range_title,
            spell_range, comp_title, components, dur_title, duration]

for item in print_me:
    print item

for paragraph in description:
    print paragraph
