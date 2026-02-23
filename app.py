from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder="web")

@app.route("/")
def home():
    try:
        # Skúsime stiahnuť dáta z internetu
        r = requests.get(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?={letter}", timeout=5)
        r.raise_for_status() # Skontroluje, či je link funkčný
        data = r.json()
        drinks = data.get("data", [])
    except Exception as e:
        print(f"Chyba: {e}")
        # Ak internet nejde, toto sa zobrazí ako záloha:
        drinks = [
    {
        "name": "Margarita",
        "ingredients": ["Tequila", "Triple sec", "Limetka"],
        "imageUrl": "https://mixthatdrink.com/wp-content/uploads/2023/03/classic-margarita-cocktail-735x1105.jpg"
    },
    {
        "name": "Mojito",
        "ingredients": ["Rum", "mäta", "Limetka", "Soda"],
        "imageUrl": "https://www.liquor.com/thmb/MJRVqf-itJGY90nwUOYGXnyG-HA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/mojito-720x720-primary-6a57f80e200c412e9a77a1687f312ff7.jpg"
    },
    {
        "name": "Gin Tonic",
        "ingredients": ["Gin", "Tonic", "citrón"],
        "imageUrl": "https://www.thespruceeats.com/thmb/0noKFvArOC2N2Eg4pA7uwc0bC30=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/gin-and-tonic-recipe-759300-hero-01-aa12e6504f944c54b8b9c589cc1d0ac6.jpg"
    },
    {
        "name": "Cosmopolitan",
        "ingredients": ["Vodka", "brusnicový džús", "citrón"],
        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnP_Vt_FYdJqp81mpDiMAuBDmUcQUVNAgD7w&s"
    },
    {
        "name": "Aperol Spritz",
        "ingredients": ["Aperol", "Prosecco", "1 plátok pomaranč"],
        "imageUrl": "https://www.alkoholium.cz/wp-content/uploads/2019/01/namichany-aperol-sprizt-199x300.jpg"
    },
    {
        "name": "Cuba Libre",
        "ingredients": ["Rum", "Cola", "Limetka"],
        "imageUrl": "https://www.senzaalcoolshop.it/media/catalog/product/cache/fd2f998da3b103353dc59ebf37e66336/v/o/vogelfrei-libre-800x600.png"
    },
    {
        "name": "Whiskey Sour",
        "ingredients": ["Whisky", "citrón", "cukor", "vajce biele"],
        "imageUrl": "https://cdn.loveandlemons.com/wp-content/uploads/2025/10/whiskey-sour.jpg"
    },
    {
        "name": "Piña Colada",
        "ingredients": ["Rum", "Kokosový krém", "Anásová šťava"],
        "imageUrl": "https://assets.tmecosys.com/image/upload/t_web_rdp_recipe_584x480/img/recipe/ras/Assets/A9467000-4182-4A69-802E-6A36234604C1/Derivates/9cca3d9b-727b-4d23-b633-71dcd23125da.jpg"
    },
    {
        "name": "Bloody Mary",
        "ingredients": ["Vodka", "Paradajková šťava", "Worcestrová omáčka", "citrón"],
        "imageUrl": "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/bloody-mary-a2983ba.jpg"
    },
    {
        "name": "Long Island Iced Tea",
        "ingredients": ["Vodka", "Rum", "Tequila", "Gin", "Triple sec", "Cola", "citrón"],
        "imageUrl": "https://www.thermomixdivarecipes.com/wp-content/uploads/2021/09/Thermomix-Long-Island-Iced-Tea_1200px_sqr.jpg"
    },
    {
        "name": "Sex on the Beach",
        "ingredients": ["Vodka", "broskyňový likér", "pomarančový džús", "brusnicový džús"],
        "imageUrl": "https://images.ctfassets.net/6zncp07wiqyq/4O5j94cP91zRNdFyijtfcH/bfc737a1882434262387d46affa95ec6/media_n04jissn_sex-on-the-beach.jpg"
    },
    {
        "name": "Manhattan",
        "ingredients": ["Whisky", "vermút", "bitter", "ľad"],
        "imageUrl": "https://www.liquor.com/thmb/DR2UAsRlu-YCVn9r_iLJCmOvzlg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/manhattan-4000x4000-primary-ig-9c3d894510284e9d8fbd9c518d00790b.jpg"
    },
    {
        "name": "Moscow Mule",
        "ingredients": ["Vodka", "Ginger Beer", "Lime"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/3pylqc1504370988.jpg"
    },
    {
        "name": "Tequila Sunrise",
        "ingredients": ["Tequila", "Orange juice", "Grenadine"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/quqyqp1480879103.jpg"
    },
    {
        "name": "Screwdriver",
        "ingredients": ["Vodka", "Orange juice"],
        "imageUrl": "https://barrellingtidedistillery.com/cdn/shop/articles/Screwdriver_2.0_-_Cocktail_Recipe_-_Barrelling_Tide_Distillery.png?v=1696533440"
    },
    {
        "name": "Irish Coffee",
        "ingredients": ["Irish whiskey", "Coffee", "Sugar", "Cream"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/sywsqw1439906999.jpg"
    },
    {
        "name": "Mai Tai",
        "ingredients": ["Rum", "Orgeat", "Orange Curacao", "Lime"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/twyrrp1439907470.jpg"
    },
    {
        "name": "Paloma",
        "ingredients": ["Tequila", "Grapefruit soda", "Lime"],
        "imageUrl": "https://www.liquor.com/thmb/biENZidPDFfUSudTwK6XXnSWVc8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__liquor__2017__05__24151232__vida-paloma-720x720-recipe-59093f2d7fcd47dcb8c053960c38fac7.jpg"
    },
    {
        "name": "Hurricane",
        "ingredients": ["Rum", "Passion fruit juice", "Lime juice", "Simple syrup", "Grenadine"],
        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdEGla4nJc9ydJdVh9tKBiuqEMgUfvNtHQpQ&s"
    },
    {
        "name": "Clover Club",
        "ingredients": ["Gin", "Lemon juice", "Raspberry syrup", "Egg white"],
        "imageUrl": "https://mixthatdrink.com/wp-content/uploads/2013/09/royal-clover-club-735x1101.jpg"
    },
    {
        "name": "Gin Fizz",
        "ingredients": ["Gin", "Lemon juice", "Sugar", "Soda water"],
        "imageUrl": "https://utopihenfarms.com/wp-content/uploads/2021/05/Classic-Gin-Fizz-Cocktail.jpg"
    },
    {
        "name": "Caipirinha",
        "ingredients": ["Cachaça", "Sugar", "Lime"],
        "imageUrl": "https://www.allrecipes.com/thmb/Xv7FI7O3UL7oE__5077haA9fYWs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/20210-caipirinha-PICS-Beauty-4x3-d4a5aed5d6534d579225b81de111b53a.jpg"
    },
    {
        "name": "White Russian",
        "ingredients": ["Vodka", "Coffee liqueur", "Cream"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/vsrupw1472405732.jpg"
    },
    {
        "name": "Black Russian",
        "ingredients": ["Vodka", "Coffee liqueur"],
        "imageUrl": "https://www.kitchengeekery.com/_next/image?url=https%3A%2F%2Fsite.kitchengeekery.com%2Fwp-content%2Fuploads%2F2021%2F01%2Fblack-russian-cocktail.jpg&w=828&q=75"
    },
    {
        "name": "Rum Punch",
        "ingredients": ["Rum", "Orange juice", "Pineapple juice", "Grenadine"],
        "imageUrl": "https://www.tasteofhome.com/wp-content/uploads/2024/05/Sweet-Rum-Punch_EXPS_FT24_273648_EC_050224_4.jpg"
    },
    {
        "name": "Blue Lagoon",
        "ingredients": ["Vodka", "Blue Curacao", "Lemonade"],
        "imageUrl": "https://www.liquor.com/thmb/-Ednp4bA2pQ79BY4Mf-2vdLegJI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__liquor__2019__07__12152657__blue-lagoon-720x720-recipe-647fb82bc3214de68e0eed9aed5afbfa.jpg"
    },
    {
        "name": "Tequila Mojito",
        "ingredients": ["Tequila", "Lime", "Mint", "Sugar", "Soda"],
        "imageUrl": "https://mycocktailrecipes.com/_next/image?url=%2Fapi%2Fmedia%2Ffile%2Ftequila_mojito_cocktail-400x400.webp&w=828&q=70"
    },
    {
        "name": "Pegu Club",
        "ingredients": ["Gin", "Lime juice", "Orange bitters", "Cointreau"],
        "imageUrl": "https://www.puredrinkology.com/recipes/pegu-club/images/cover_huea14c79269db3153ff5eaf879241deb9_225238_1000x0_resize_q75_box.jpeg"
    },
    {
        "name": "Rusty Nail",
        "ingredients": ["Scotch", "Drambuie"],
        "imageUrl": "https://punchdrink.com/wp-content/uploads/2014/01/Social-Bobby-heugel-Rusty-Nail-Scotch-Cocktail-Recipe.jpg"
    },
    {
        "name": "B52",
        "ingredients": ["Kahlua", "Baileys", "Grand Marnier"],
        "imageUrl": "https://www.alkohol-shop.cz/user/articles/images/b52.jpg"
    },
    {
        "name": "Golden Dream",
        "ingredients": ["Galliano", "Orange juice", "Triple sec", "Cream"],
        "imageUrl": "https://www.shakedrinkrepeat.com/wp-content/uploads/2022/01/Golden-Dream-4.jpg"
    },
    {
        "name": "Vesper",
        "ingredients": ["Gin", "Vodka", "Lillet Blanc"],
        "imageUrl": "https://www.simplyrecipes.com/thmb/L-08Ye1YjiPnO7cM5YIO-OcAzBo=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Vesper-Cocktail-LEAD-05-df942c449a124fb291a3c76e071729e7.jpg"
    },
    {
        "name": "Sazerac",
        "ingredients": ["Rye whiskey", "Absinthe", "Sugar", "Bitters"],
        "imageUrl": "https://www.liquor.com/thmb/Ob_GjDCNJE0a8rHE7YfUK8txAmg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/sazerac-1500x1500-hero-62326d995cdb4a79a6a0a3bd4a98cef9.jpg"
    },
    {
        "name": "Mint Julep",
        "ingredients": ["Bourbon", "Mint", "Sugar", "Water"],
        "imageUrl": "https://cdn.diffords.com/contrib/encyclopedia/2018/12/5c0fcbc2b0b9d.jpg"
    },
    {
        "name": "Mai Tai (Variation)",
        "ingredients": ["Rum", "Orgeat syrup", "Orange Curacao", "Lime juice"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/twyrrp1439907470.jpg"
    },
    {
        "name": "Zombie",
        "ingredients": ["Light rum", "Dark rum", "Apricot brandy", "Pineapple juice", "Papaya juice", "Lime juice", "Grenadine"],
        "imageUrl": "https://www.foodandwine.com/thmb/0PaWcq-nvWBsquRjtt_V332G2Wg=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/zombie-FT-RECIPE1025-02-854e970e5a754e93823edabe7093ba58.jpg"
    },
    {
        "name": "Bahama Mama",
        "ingredients": ["Dark rum", "Coconut rum", "Pineapple juice", "Orange juice", "Grenadine"],
        "imageUrl": "https://images.immediate.co.uk/production/volatile/sites/30/2024/06/Bahama-mama-fb944d2.jpg"
    },
    {
        "name": "Planter’s Punch",
        "ingredients": ["Dark rum", "Lime juice", "Pineapple juice", "Grenadine"],
        "imageUrl": "https://images.squarespace-cdn.com/content/v1/5bcccf8b9b7d15579477a125/af5183a9-7613-46f6-aa1e-c9c47b4a7167/Planter%27s+Punch.jpg"
    },
    {
        "name": "French 75",
        "ingredients": ["Gin", "Champagne", "Lemon juice", "Sugar"],
        "imageUrl": "https://www.tastingtable.com/img/gallery/french-75-cocktail-recipe-upgrade/french-75-cocktail-recipe-upgrade-1666629351.jpg"
    },
    {
        "name": "Sidecar",
        "ingredients": ["Cognac", "Triple sec", "Lemon juice"],
        "imageUrl": "https://upload.wikimedia.org/wikipedia/commons/9/94/Sidecar-cocktail.jpg"
    },
    {
        "name": "Americano",
        "ingredients": ["Campari", "Sweet Vermouth", "Soda water"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/xxsxqy1472668106.jpg"
    },
    {
        "name": "Aviation",
        "ingredients": ["Gin", "Maraschino liqueur", "Lemon juice", "Crème de violette"],
        "imageUrl": "https://www.liquor.com/thmb/VpgoyRklZ9Z-iXty4CJF6dHWR1w=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/aviation-720x720-primary-52e461a1150f4cf9b0ee91e1d322bbf7.jpg"
    },
    {
        "name": "Bee’s Knees",
        "ingredients": ["Gin", "Lemon juice", "Honey syrup"],
        "imageUrl": "https://www.foodandwine.com/thmb/oL9MpBW0Vg3NFLw6_3Jjf6zhpFQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Bees_Knees_Credit_Tim_Nusog_4000x2667-primary-0876667fee8a41fab42d8295eb97dbba.jpg"
    },
    {
        "name": "Bellini",
        "ingredients": ["Prosecco", "Peach purée"],
        "imageUrl": "https://media.alkotip.sk/2023/11/bellini-koktail.jpg"
    },
    {
        "name": "Boulevardier",
        "ingredients": ["Bourbon", "Campari", "Sweet Vermouth"],
        "imageUrl": "https://www.panningtheglobe.com/wp-content/uploads/2017/08/boulevardier-cocktail-recipe.jpg"
    },
    {
        "name": "Corpse Reviver ",
        "ingredients": ["Gin", "Cointreau", "Lillet Blanc", "Lemon juice", "Absinthe rinse"],
        "imageUrl": "https://d34nm4jmyicdxh.cloudfront.net/eyJidWNrZXQiOiJjaHJpc3N5LXR1eGVkby1ubzIiLCJrZXkiOiJyZWNpcGUtY29ycHNlLXJldml2ZXItMi1jb2NrdGFpbC1yZWNpcGUuanBnIiwiZWRpdHMiOnsicmVzaXplIjp7IndpZHRoIjo2MDAsImhlaWdodCI6NjAwLCJmaXQiOiJjb3ZlciJ9fX0="
    },
    {
        "name": "Dark 'N' Stormy",
        "ingredients": ["Dark rum", "Ginger beer", "Lime"],
        "imageUrl": "https://www.allrecipes.com/thmb/PJXw-uc8-DZnunRHjd3aiDyCtys=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/222547dark-n-stormy-cocktailFranceC4x3-fa7295a9367d4911ba65a7c45e4179e8.jpg"
    },
    {
        "name": "El Presidente",
        "ingredients": ["Rhum", "Orange curaçao", "Sweet Vermouth", "Grenadine"],
        "imageUrl": "https://images.getrecipekit.com/20240207170515-el-presidente.jpg?width=650&quality=90&"
    },
    {
        "name": "Espresso Martini",
        "ingredients": ["Vodka", "Coffee liqueur", "Espresso"],
        "imageUrl": "https://images.immediate.co.uk/production/volatile/sites/30/2020/08/espresso-martini-f099531.jpg"
    },
    {
        "name": "Gimlet",
        "ingredients": ["Gin", "Lime juice", "Simple syrup"],
        "imageUrl": "https://www.liquor.com/thmb/mi0oeRqiuSED3lwQOOWgjZY493s=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Gimlet-1500x1500-hero-7af9450103b9437d8d5b7206a6ddfe43.jpg"
    },
    {
        "name": "Grasshopper",
        "ingredients": ["Crème de menthe", "Crème de cacao", "Cream"],
        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ5MLuAmL4fuSSOWrqqwAW8G69eCtYSOECwFw&s"
    },
    {
        "name": "Harvey Wallbanger",
        "ingredients": ["Vodka", "Galliano", "Orange juice"],
        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRdcB3S9ODEQ20YbNOTop-2iuW_TXF9bBjDvg&s"
    },
    {
        "name": "Horse’s Neck",
        "ingredients": ["Cognac or Brandy", "Ginger ale", "Lemon peel"],
        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQfmG-oxgN8nCDTdQyxQ8UA_ccqHg-XJhf83w&s"
    },
    {
        "name": "Hugo",
        "ingredients": ["Prosecco", "Elderflower syrup", "Mint", "Lime"],
        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT64pglo2ZycZmwQYDZW1hdH2H3ADEKUNNHUQ&s"
    },
    {
        "name": "Jungle Bird",
        "ingredients": ["Dark rum", "Campari", "Pineapple juice", "Lime juice", "Simple syrup"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/5noda61589575158.jpg"
    },
    {
        "name": "Last Word",
        "ingredients": ["Gin", "Green Chartreuse", "Maraschino", "Lime juice"],
        "imageUrl": "https://www.liquor.com/thmb/phSQYzvYOOTk_P944FXheJqYND8=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/last-word-720x720-primary-c83c917809af47bf9be9a01c628bbd5e.jpg"
    },
    {
        "name": "Mary Pickford",
        "ingredients": ["White rum", "Pineapple juice", "Maraschino", "Grenadine"],
        "imageUrl": "https://www.liquor.com/thmb/CYCfDoH-iI0pdTmYivMeXGR6QKs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/mary-pickford-720x720-primary-d3a86684af4b42bfb7c90074135aec24.jpg"
    },
    {
        "name": "Mexican Firing Squad",
        "ingredients": ["Tequila", "Lime", "Grenadine", "Angostura bitters"],
        "imageUrl": "https://cdn.diffordsguide.com/cocktail/O5KEwA/lifestyle/0/1024x.webp?v=1737701602"
    },
    {
        "name": "Painkiller",
        "ingredients": ["Dark rum", "Pineapple juice", "Orange juice", "Cream of coconut"],
        "imageUrl": "https://www.foodandwine.com/thmb/FSDgdDP25Fn5KPDtazcneRPljaA=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Painkiller-FT-RECIPE0625-c76a5a28ea4045d5865953d448617e40.jpg"
    },
    {
        "name": "Paper Plane",
        "ingredients": ["Bourbon", "Aperol", "Amaro", "Lemon"],
        "imageUrl": "https://www.sipandfeast.com/wp-content/uploads/2024/12/paper-plane-cocktail-snippet-2.jpg"
    },
    {
        "name": "Pisco Sour",
        "ingredients": ["Pisco", "Lime", "Simple syrup", "Egg white"],
        "imageUrl": "https://www.liquor.com/thmb/ohTOhWrDCBdEScPNwFDmM6mrwbQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/__opt__aboutcom__coeus__resources__content_migration__liquor__2019__02__08143927__pisco-sour-720x720-recipe-9c46d52151e5445fa90bcf0394493060.jpg"
    },
    {
        "name": "Rob Roy",
        "ingredients": ["Scotch", "Sweet Vermouth", "Bitters"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/uxywyw1468877224.jpg"
    },
    {
        "name": "Sea Breeze",
        "ingredients": ["Vodka", "Cranberry juice", "Grapefruit juice"],
        "imageUrl": "https://www.liquor.com/thmb/hLHqPxEEaYhytSd5G3eIUjwJExc=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/sea-breeze-720x720-recipe-e1e39750d0fe46eeb281de64c93110dd.jpg"
    },
    {
        "name": "Stinger",
        "ingredients": ["Brandy", "White crème de menthe"],
        "imageUrl": "https://www.cocktails-road.com/images/recipe/2022/09/stinger.jpg"
    },
    {
        "name": "Tuxedo Cocktail",
        "ingredients": ["Gin", "Dry Vermouth", "Maraschino", "Absinthe"],
        "imageUrl": "https://www.liquor.com/thmb/9mUm7eBJat7QBruawQHOJP7PetY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/tuxedo-n2-1200x628-email-08b608a93a204bf8829cf53662aec2e1.jpg"
    },
    {
        "name": "Vieux Carré",
        "ingredients": ["Rye whiskey", "Cognac", "Sweet Vermouth", "Benedictine", "Bitters"],
        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQu111Q3bSl4RmF1nocPo7wbkYX1GAl6NNgFQ&s"
    },
    {
        "name": "White Lady",
        "ingredients": ["Gin", "Cointreau", "Lemon juice"],
        "imageUrl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQLnK9SnqrEBj4GRQ0NQNS9yMox8dlDYIlzDg&s"
    },
    {
        "name": "Zombie Punch",
        "ingredients": ["Light rum", "Dark rum", "Fruit juices", "Grenadine"],
        "imageUrl": "https://www.thecocktaildb.com/images/media/drink/bry4qh1582751040.jpg"
    }
]

    ...


    # DÔLEŽITÉ: 'cocktails' vľavo musí byť presne tak, ako v HTML {% for drink in cocktails %}
    return render_template("index.html", cocktails=drinks)

if __name__ == "__main__":
    app.run(debug=True)