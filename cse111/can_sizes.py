#04 Team Activity: Writing Functions

#import needed libraries
import math
lists = []

def main():
    for list in range(0,12,1):
        #get radius and height from user
        radius = float(input("Enter the Radius: (cm) "))
        height = float(input("Enter the height: (cm) "))

        #calculate volume
        volume = compute_volume(radius, height)

        #calculate surface_area
        area_surface = surface_area(radius, height)

        #calculate storage_effeciency
        efficiency_storage = storage_efficiency(volume, area_surface)
        #lists.append[volume, area_surface, efficiency_storage]
        lists.append(efficiency_storage)
        list = efficiency_storage

    for list in range(0,12,1):
        print(f"The storage efficiency {lists[list]:.2f}")
    pass

def compute_volume(radius, height):
    #compute volume
    volume = math.pi *radius ** 2 * height
    #return volume 
    return volume

def surface_area(radius, height):
    #calculate Surface area
    surface_area = 2 * math.pi *radius * (radius + height)
    #return area
    return surface_area

def storage_efficiency(volume, surface_area):
    #compute storage efficiency
    storage_efficiency = volume / surface_area
    # return storage efficiency
    return storage_efficiency

#call the main function
main()