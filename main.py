# import requests
#
# from bs4 import BeautifulSoup
#
# with open("index.html", "r", encoding="utf-8") as file:
#      src = file.read()
# print(src)
# soup = BeautifulSoup(src, "lxml")
#
# page_h1 = soup.find("h1")
# print(page_h1.text)
#
# for item in page_all_h1:
#     print(item.text)         не выведется
#
# user_name = soup.find("div", class="user__name")
# print(user__name.text.strip())
#
# user_name = soup.find("div", {"class" : "user_name","id":"dopolnitelnyi"}).find("span")
# print(user__name.text.strip())
#
# find_all_spans_in_user__info = soup.find(
#      class_="user__info").find_all("span")
# print(find_all_spans_in_user__info)
#
# for item in find_all_spans_in_user__info:
#      print(item.text)
#
# social_link = soup.find(class_="social__networks").find("ul").find_all("a")
# print(social_link)
#
# all_a = soup.find_all("a")
# print(all_a)
#
# for item in all_a:
#      item_url = item.text
#      item_url = item.get("href")
#      print(item_url)
#
# next_elemen = soup.find(class_="post__title").next_element\
#      .next_element.text
# print(next_elemen)
#
#
# links = soup.find(class_="some__links").find_all("a")
# print(links)
#
# for link in links:
#      link_href_attr = link.get("href")
#      link_data_attr = link.get("data-attr")
#      print(link_data_attr)
#      print(link_data_attr)
#
# find_by_text = soup.find("a", text="Одежда для взрослых")
# print(find_by_text.text)
#
# find_a_by_text = soup.find("a", text=re.compile("Одежда"))
# print(find_a_by_text)
#
# finnd_compile_registr =  soup.find_all(text=re.compile("([Оо]дежда)"))
# print(finnd_compile_registr)
#1-урок
#
#
#
#
# # # todo: step 2
# with open("all_categories_dict.json",encoding="utf-8") as file:
#  all_categories = json.load(file)
#
# iteration_count = int(len(all_categories)) - 1
# count = 0
# print(f"ВСЕГО ИТЕРАЦИЙ: {iteration_count}")
#
# for category_name, category_href in all_categories.items():
#
#     rep = ["'"",", " ", "-"]
#     for item in rep:
#         if item in category_name:
#             category_name = category_name.replace(item, "_")
#
#     req = requests.get(url=category_href, headers=headers)
#     src = req.text
#
#     with open(f"data4/{count}_{category_name}.html", "w", encoding="utf-8") as file:
#         file.write(src)
#     with open(f"data4/{count}_{category_name}.html", encoding="utf-8") as file:
#         src = file.read()
#
#     soup = BeautifulSoup(src, "lxml")
#
#     allert_block =  soup.find(class_="uk-alert-danger")
#     if allert_block is not None:
#         continue
#     # cобираем заголовки таблицы
#     table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")
#     product = table_head[0].text
#     calories = table_head[1].text
#     proteins = table_head[2].text
#     fats = table_head[3].text
#     carbohydrates = table_head[4].text
#
#     with open(f"data4/{count}_{category_name}.csv", "w", encoding="utf-8") as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             (
#                 product,
#                 calories,
#                 proteins,
#                 fats,
#                 carbohydrates,
#             )
#         )
#     #sobiraem dannye producta
#     products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")
#
#     product_info = []
#     for item in products_data:
#         products_tds = item.find_all("td")
#
#         title = products_tds[0].find("a").text
#         calories = products_tds[1].text
#         proteins = products_tds[2].text
#         fats = products_tds[3].text
#         carbohydrates = products_tds[4].text
#
#         product_info.append(
#             {
#                 "Title": title,
#                 "Calories": calories,
#                 "Proteins": proteins,
#                 "Fats": fats,
#                 "Carbohydrates": carbohydrates,
#             }
#         )
#
#         with open(f"data4/{count}_{category_name}.csv", "a", encoding="utf-8") as file:
#             writer = csv.writer(file)
#             writer.writerow(
#                 (
#                     title,
#                     calories,
#                     proteins,
#                     fats,
#                     carbohydrates,
#                 )
#             )
#
#     with open(f"media9/{count}_{category_name}.json", "a", encoding="utf-8") as  file:
#         json.dump(product_info, file, indent=4, ensure_ascii=False)
#     count += 1
#     print(f"# ИТЕРАЦИЙ {count}. {category_name} ЗАПИСАН...")
#     iteration_count = iteration_count -1
#
#     if iteration_count == 0:
#         print("РАБОТА ЗАВЕРШЕНА!")
#         break
#
#     print(f"ОСТАЛОСЬ ИНТЕРАЦИЙ: {iteration_count}")
#     sleep(randint(0,1)) #2-УРОК
#
#
# import requests
# from bs4 import BeautifulSoup
# import lxml
# import json
# 
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
# 
# }
# count = 1
# 
# fests_urls_list = []
# 
# for i in range(0, 241, 24):
#     url1 = f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=&to_date=&maxprice=500&o={i}&bannertitle=May'
# 
#     req = requests.get(url=url1, headers=headers)
#     json_data = json.loads(req.text)
#     html_response = json_data['html']
# 
#     with open(f"data/index_{i}.html", 'w', encoding='utf-8') as file:
#         file.write(html_response)
# 
#     with open(f"data/index_{i}.html", encoding='utf-8') as file:
#         src = file.read()
# 
#     soup = BeautifulSoup(src, 'lxml')
# 
#     cards = soup.find_all('a', class_='card-details-link')
# 
#     for item in cards:
#         fest_url = 'https://www.skiddle.com' + item.get('href')
#         fests_urls_list.append(fest_url)
# 
# fest_result_list =[]
# 
# for url in fests_urls_list:
#     req = requests.get(url=url, headers=headers)
# 
#     soup = BeautifulSoup(req.text, "lxml")
# 
#     print("__________________________________________________")
#     print(count)
#     print(url)
#     try:
#        
#         fest_info_block = soup.find("div", class_="MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 css-1ik2gjq")
#         fest_info_list = fest_info_block.find_all(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 css-2re0kq")
# 
#  
#         fest_name_block = soup.find("div", class_="MuiContainer-root MuiContainer-maxWidthFalse css-1krljt2")
#         fest_name = fest_name_block.find("h1").text
# 
#  
#         fest_data = fest_info_list[0].find(class_="MuiGrid-root MuiGrid-container css-f3i3nk").find(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol").find_all("span")
#         fest_data[0].append(fest_data[1])
#         # адрес ивента
#         fest_location = fest_info_list[1].find(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol").find("span").text
# 
#           
#         if len(fest_info_list) == 3:
# 
#             fest_price = fest_info_list[2].find(class_="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-11 css-twt0ol").find("span").text
#         elif len(fest_info_list) < 3:
#             fest_price = "No information"
# 
# 
#         fest_result_list.append(
#             {
#                 "Count": count,
#                 "Link": url,
#                 "Fest name": fest_name,
#                 "Fest date": fest_data[0].text,
#                 "Fest location": fest_location,
#                 "Fest price": fest_price,
#             }
#         )
#     except AttributeError:
#         fest_result_list.append({
#             "Count": count,
#             "!": "Error"
#         })
#     count += 1
# 
# with open("fest_result_list.json", "a", encoding="utf-8") as file:
#     json.dump(fest_result_list, file, indent=4, ensure_ascii=False)
#       #3-урок
#
#
#
#
#
#import time
# import json
# import requests
# from bs4 import BeautifulSoup
# import lxml
# import datetime
# import csv
# 
# start_time = time.time()
# 
# def get_data():
#     cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
# 
#     with open(f"labirint_{cur_time}.csv", "w", encoding="utf-8") as file:
#         writer = csv.writer(file)
# 
#         writer.writerow(
#             (
#                 "Название книги",
#                 "Автор",
#                 "Издательство",
#                 "Цена со скидкой",
#                 "Цена без скидки",
#                 "Процент скидки",
#                 "Статус наличия"
#             )
#         )
# 
#     headers = {
#         "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
#     }
# 
#     url = "https://www.labirint.ru/genres/2308/"
# 
#     response = requests.get(url=url, headers=headers)
#     soup = BeautifulSoup(response.text, "lxml")
# 
#     pages_count = int(soup.find("div", class_="pagination-numbers").find_all("a")[-1].text)
# 
#     books_data = []
#     for page in range(1, pages_count + 1):
#         url = f"https://www.labirint.ru/genres/2308/?display=table&page={page}"
# 
#         response = requests.get(url=url, headers=headers)
#         soup = BeautifulSoup(response.text, "lxml")
# 
#         books_items = soup.find("tbody", class_="products-table__body").find_all("tr")
# 
#         for bi in books_items:
#             book_data = bi.find_all("td")
# 
#             try:
#                 book_title = book_data[0].find("a").text.strip()
#             except:
#                 book_title = "Название не указано"
# 
#             try:
#                 book_author = book_data[1].text.strip()
#             except:
#                 book_author = "Автор не указан"
# 
#             try:
#                 # book_publishing = book_data[2].text
#                 book_publishing = book_data[2].find_all("a")
#                 book_publishing = ":".join([bp.text for bp in book_publishing])
#             except:
#                 book_publishing = "Издатель не указан"
# 
#             try:
#                 book_new_price = int(book_data[3].find("div", class_="price").find("span").find("span").text.strip().replace(" ", ""))
#             except:
#                 book_new_price = "Цена со скидко не указана"
# 
#             try:
#                 book_old_price = int(book_data[3].find("span", class_="price-gray").text.strip().replace(" ", ""))
#             except:
#                 book_old_price = "Цена без скидки не указана"
# 
#             try:
#                 book_sale = round(((book_old_price - book_new_price) / book_old_price) * 100)
#             except:
#                 book_sale = "Нет скидки"
# 
#             try:
#                 book_status = book_data[-1].text.strip()
#             except:
#                 book_status = "Статус не указан"
# 
#             # print(book_title)
#             # print(book_author)
#             # print(book_publishing)
#             # print(book_new_price)
#             # print(book_old_price)
#             # print(book_sale)
#             # print(book_status)
#             # print("#" * 10)
# 
#             books_data.append(
#                 {
#                     "Название": book_title,
#                     "Автор": book_author,
#                     "Издательство": book_publishing,
#                     "Цена со скидкой": book_new_price,
#                     "Цена без скидки": book_old_price,
#                     "Процент скидки": book_sale,
#                     "Статус": book_status
#                 }
#             )
# 
#             with open(f"labirint_{cur_time}.csv", "a", encoding="utf-8") as file:
#                 writer = csv.writer(file)
# 
#                 writer.writerow(
#                     (
#                         book_title,
#                         book_author,
#                         book_publishing,
#                         book_new_price,
#                         book_old_price,
#                         book_sale,
#                         book_status
#                     )
#                 )
# 
#         print(f"Обработана {page}/{pages_count}")
#         time.sleep(1)
# 
#     with open(f"labirint_{cur_time}.json", "w", encoding="utf-8") as file:
#         json.dump(books_data, file, indent=4, ensure_ascii=False)
# 
# def main():
#     get_data()
#     finish_time = time.time() - start_time
#     print(f"На работу кода ушло: {finish_time}")
# 
# if __name__ == '__main__':
#     main()
# # 9-урок
#
#
#
#
#
# import datetime
# import json
# import requests
#
#
# headers = {
#         "X-Is-Ajax-Requests": "X-Is-Ajax-Requests",
#         "X-Requested-With": "XMLHttpRequest"
# }
#
#
# def get_data():
#     start_time = datetime.datetime.now()
#     url = "https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1=146"
#     r = requests.get(url=url, headers=headers)
#
#     # with open("index.html", "w", encoding="utf-8") as file:
#     #     file.write(r.text)
#
#     # print(r.json())
#
#     # with open("r.json", "w", encoding="utf-8") as file:
#     #     json.dump(r.json(), file, indent=4, ensure_ascii=False)
#
#     pages_count = r.json()["pagesCount"]
#
#     data_list = []
#     for page in range(1, pages_count + 1):
#         url = f"https://roscarservis.ru/catalog/legkovye/?form_id=catalog_filter_form&filter_mode=params&sort=asc&filter_type=tires&arCatalogFilter_458_1500340406=Y&set_filter=Y&arCatalogFilter_463=668736523&PAGEN_1={pages_count}"
#
#         r = requests.get(url=url, headers=headers)
#         data = r.json()
#         items = data["items"]
#
#         possible_stores = ["discountStores", "fortochkiStores", "commonStores"]
#         for item in items:
#             total_amount = 0
#             item_name = item["name"]
#             item_price = item["price"]
#             item_img = f'https://roscarservis.ru{item["imgSrc"]}'
#             item_url = f'https://roscarservis.ru{item["url"]}'
#
#         stores = []
#         for ps in possible_stores:
#             if ps in item:
#                 if item[ps] is None or len(item[ps]) < 1:
#                     continue
#                 else:
#                     for store in item[ps]:
#                         store_name = store["STORE_NAME"]
#                         store_price = store["PRICE"]
#                         store_amount = store["AMOUNT"]
#                         total_amount += int(store["AMOUNT"])
#
#                         stores.append(
#                             {
#                                 "store_name": store_name,
#                                 "store_price": store_price,
#                                 "store_amount": store_amount,
#                             }
#                         )
#             data_list.append(
#                 {
#                     "name": item_name,
#                     "price": item_price,
#                     "url": item_url,
#                     "img_url": item_img,
#                     "stores": stores,
#                     "total_amount": total_amount,
#
#                 }
#             )
#         print(f"[INFO] обработал {page}/{pages_count}")
#
#     cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
#     with open(f"data_{cur_time}.json", "a", encoding="utf-8") as file:
#         json.dump(data_list, file, indent=4, ensure_ascii=False)
#
#     diff_time = datetime.datetime.now() - start_time
#     print(diff_time)
#
# def main():
#     get_data()
#
# if _name_ == '_main_':
#     main()
# 8- урок
#
#
#
#
#
