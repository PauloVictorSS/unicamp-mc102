qtd_malicious_websites = int(input())

malicious_websites = []

for i in range(qtd_malicious_websites):
    malicious_websites.append(input())

qtd_popup = int(input())

total_coordinates = []
websites_names = []

for i in range(qtd_popup):

    website_coordinates = []
    infs = input().split()

    for j in range(4):
        website_coordinates.append(int(infs[j]))
    
    total_coordinates.append(website_coordinates)
    websites_names.append(infs[4])


click1, click2 = map(int, input().split())

clicks = []

while click1 >= 0 and click2 >= 0:
    clicks_coordinates = []

    clicks_coordinates.append(click1)
    clicks_coordinates.append(click2)

    clicks.append(clicks_coordinates)

    click1, click2 = map(int, input().split())

results = []

for clicks_coordinates in clicks:

    click_x = clicks_coordinates[0]
    click_y = clicks_coordinates[1]

    c_any_click_ad = False

    for popup_coordinates in total_coordinates:
        
        ad_x0 = popup_coordinates[0]
        ad_y0 = popup_coordinates[1]
        ad_x1 = popup_coordinates[2]
        ad_y1 = popup_coordinates[3]

        c_any_click_ad = False

        if ((ad_x0 <= click_x) and  (click_x <= ad_x1)) and ((ad_y0 <= click_y) and  (click_y <= ad_y1)):

            c_any_click_ad = True
            c_malicious_website = False

            name_site = websites_names[total_coordinates.index(popup_coordinates)]

            for website in malicious_websites:
                if name_site == website:
                    results.append("malicioso")
                    c_malicious_website = True
                    break

            if not c_malicious_website:
                results.append("seguro")

            break

    if not c_any_click_ad:
        results.append("nenhum")

for result in results:
    print(result)