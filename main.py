import vision_system


vision = vision_system.vision_system()

order = [2, 3]
correctly_guessed = 0
count = 0


for spring_number in order:
    print("-------------------")
    print(spring_number)
    vision.set_good_image('images/Good_Images/Spring' + str(spring_number) + '_cropped.jpeg')

    # calculate a good image range
    goodImageRange = []
    for i in range(1, 3):
        vision.set_input_image("images/Good_Images/Spring" + str(spring_number) + "_" + str(i) + ".jpeg")
        goodImageRange.append(vision.match())
    minRange = min(goodImageRange)
    maxRange = max(goodImageRange)

    for i in range(1, 5):
        print("image "+str(i))
        vision.set_input_image("images/Good_Images/Spring" + str(spring_number) + "_" + str(i) + ".jpeg")
        matched = minRange <= vision.match() <= maxRange
        print("good image: " + str(matched))

        count+= 1
        if matched == True:
            correctly_guessed += 1
        for bad_number in range(5):
            vision.set_input_image('images/Bad_Images/Spring' + str(spring_number) + '_' + str(i) + '_bad' + str(bad_number) + '.jpeg')
            matched = minRange <= vision.match() <= maxRange
            print(matched)
            count+= 1
            if matched == False:
                correctly_guessed += 1
            
print(correctly_guessed/count)