from operator import itemgetter
import pygame
import math

def get_loc():
    import pygame
    pygame.init()
    crashed = False
    introScreenImage = pygame.image.load("newmap.jpg")
    screen = pygame.display.set_mode((1221, 862))
    pygame.display.set_caption("NTU map")
    mouseX = 0
    mouseY = 0
    while not crashed:
        for event in pygame.event.get():                        # get events
            if event.type == pygame.MOUSEBUTTONDOWN:                   # check whether mouse is clicked
                (mouseX, mouseY) = pygame.mouse.get_pos()               # get coordinates tuple
                crashed = True
            if event.type == pygame.QUIT:
                crashed = True                                       # check quit
            screen.blit(introScreenImage, (0, 0))
            pygame.display.flip()
    pygame.quit()
    return mouseX, mouseY


def distance_a_b(location_of_a, location_of_b):
    distance = math.sqrt((location_of_a[0] - location_of_b[0]) ** 2 + (location_of_a[1] - location_of_b[1]) ** 2)
    return distance


def sort_distance(list_location):
    location_raw = []
    final_out = {}
    for value in list_location.values():
        location_raw.append(value)
    #merge sort
    sort_info = merge_sort(location_raw)
    #convert from list of list to list of string
    for items in sort_info:
        for key,value in list_location.items():
            if items == value:
                final_out[key]=value
    return final_out


def search_by_food(foodname, foodlist_canteens):
    result_canteens = []
    for key in foodlist_canteens:
        if key[1] == foodname:
            if key[0] in result_canteens:
                continue
            else:
                result_canteens.append(key[0])
        else:
            continue
    if result_canteens == []:
        return None
    else:
        return result_canteens

def merge_sort(list_of_items):
    list_len = len(list_of_items)
    # base case
    if list_len < 2:
        return list_of_items
    left_list = list_of_items[:list_len // 2] # //
    right_list = list_of_items[list_len // 2:]  # "//" to force division
    # merge sort left and right list recursively
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return merge(left_list, right_list)

def merge(left_list, right_list):
    result_list = []
    # while left and right list has elements
    while left_list and right_list:
        if left_list[0] < right_list[0]:
            result_list.append(left_list[0])
            left_list.pop(0)
        else:
            result_list.append(right_list[0])
            right_list.pop(0)
    #left list still contain elements. Append its contents to end of the result
    if left_list:
        result_list.extend(left_list)
    else:
        #right list still contain elements. Append its contents to end of the result
        result_list.extend(right_list)
    return result_list


def rate(rate_dict):
    ranklist_canteens=[]
    final_out=[]
    for key,value in rate_dict.items():
        n = len(value)
        aver_rate=sum(value)/n
        ranklist_canteens.append((key,aver_rate))
    sort_info = sorted(ranklist_canteens, key=itemgetter(1))
    sort_info.reverse()
    for x in sort_info:
        ans = str(x[0]) + ": " + str(x[1])
        final_out.append(ans)
    return final_out




def search_by_price(price, foodlist_canteens):
    canteen_list = {}
    sort_info=[]
    final_out = []
    for key,value in foodlist_canteens.items():
        if price[0]<=value<=price[1]:
            canteen_list[key]=value
    for value in canteen_list.values():
        sort_info.append(value)
    if sort_info == []:
        return None
    else:
        sort_info = bubbleSort(sort_info)
        for items in sort_info:
            for key,value in canteen_list.items():
                if items == value:
                    ans = str(key[0]) + ", " + str(key[1])+": "+str(value)
                    final_out.append(ans)
        return final_out



def bubbleSort(list_to_sort):
    for passnum in range(len(list_to_sort)-1):
        swapped = False
        for i in range(len(list_to_sort)-1):
            if list_to_sort[i]>list_to_sort[i+1]:
                temp = list_to_sort[i]
                list_to_sort[i] = list_to_sort[i+1]
                list_to_sort[i+1] = temp
                swapped = True
        if not swapped:
            break;
    return list_to_sort