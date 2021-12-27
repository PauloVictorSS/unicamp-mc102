"""
Ainda não terminei, mas já estou enviando o resto para correção por causa da data
depois vou continuar tentando esse aqui
"""

total_ads = int(input())

total_ad_coordinates = []

for i in range(total_ads):
    ad_coordinates = []

    ad_coordinates = list(map(int, input().split()))

    total_ad_coordinates.append(ad_coordinates)

viewed_ads = 1

for i in range(1,total_ads):

    ad_x0 = total_ad_coordinates[i][0]
    ad_y0 = total_ad_coordinates[i][0]
    ad_x1 = total_ad_coordinates[i][0]
    ad_y1 = total_ad_coordinates[i][0]

    cont = 0
    for j in range(i):

        ad_comp_x0 = total_ad_coordinates[j][0]
        ad_comp_y0 = total_ad_coordinates[j][1]
        ad_comp_x1 = total_ad_coordinates[j][2]
        ad_comp_y1 = total_ad_coordinates[j][3]

        ad_x0_in_ad_comp_x = (ad_comp_x0 <= ad_x0) and (ad_x0 <= ad_comp_x1)
        ad_x1_in_ad_comp_x = (ad_comp_x0 <= ad_x1) and (ad_x1 <= ad_comp_x1)

        ad_y0_in_ad_comp_y = (ad_comp_y0 <= ad_y0) and (ad_y0 <= ad_comp_y1)
        ad_y1_in_ad_comp_y = (ad_comp_y0 <= ad_y1) and (ad_y1 <= ad_comp_y1)

        if (ad_x0 >= ad_comp_x1) or (ad_y0 >= ad_comp_y1) or (ad_x1 <= ad_comp_x0) or (ad_y1 <= ad_comp_y0):
            cont += 1
            continue

        if (ad_x0_in_ad_comp_x and ad_x1_in_ad_comp_x and ad_x1_in_ad_comp_x and ad_y1_in_ad_comp_y):
            break

        if ad_y0_in_ad_comp_y and ad_y1_in_ad_comp_y:
            if ad_x0_in_ad_comp_x:
                ad_x0 = ad_comp_x0
                cont += 1
                continue
        
            if ad_x1_in_ad_comp_x:
                ad_x1 = ad_comp_x1
                cont += 1
                continue

        if ad_x0_in_ad_comp_x and ad_x1_in_ad_comp_x:
            if ad_y0_in_ad_comp_y:
                ad_y0 = ad_comp_y1
                cont += 1
                continue
        
            if ad_y1_in_ad_comp_y:
                ad_y1 = ad_comp_y0
                cont += 1
                continue

    if(cont == i):
        viewed_ads += 1

print(f"É possível ver {viewed_ads} anúncios")