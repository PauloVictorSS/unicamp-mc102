player_x0, player_y0, player_x1, player_y1 = map(int, input().split())

n_ads = int(input())
total_ads_coordinates = []

for i in range(n_ads):
    ads_coordinates = []

    ad_x0, ad_y0, ad_x1, ad_y1 = map(int, input().split())

    ads_coordinates.append(ad_x0)
    ads_coordinates.append(ad_y0)
    ads_coordinates.append(ad_x1)
    ads_coordinates.append(ad_y1)

    total_ads_coordinates.append(ads_coordinates)

n_closed_ads = 0

for ads_coordinates in total_ads_coordinates:

    ad_x0 = ads_coordinates[0]
    ad_y0 = ads_coordinates[1]
    ad_x1 = ads_coordinates[2]
    ad_y1 = ads_coordinates[3]

    if not ((ad_x0 >= player_x1) or (ad_x1 <= player_x0) or (ad_y0 >= player_y1) or (ad_y1 <= player_y0)):
        n_closed_ads += 1

print(f"Devem ser fechados {n_closed_ads} anúncios")