import pandas

excel_data_df = pandas.read_excel('wine.xlsx')

print(excel_data_df)

wine_name = excel_data_df['Название'].tolist()
wine_variety = excel_data_df['Сорт'].tolist()
wine_price = excel_data_df['Цена'].tolist()
wine_picture = excel_data_df['Картинка'].tolist()

#print(wine_name, wine_variety, wine_price, wine_picture)

wine_data = []
for i in range(len(excel_data_df)):
    wine_data.append({
        'name': wine_name[i],
        'variety': wine_variety[i],
        'price': wine_price[i],
        'picture': wine_picture[i]
    })

print(wine_data)