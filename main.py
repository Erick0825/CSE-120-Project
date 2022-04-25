import vision_system


vision = vision_system.vision_system()

# vision.set_good_image("images/Good_Images/Spring1_0.jpeg")
# vision.isolate_good_image_logo()
# vision.get_good_image_features()

# print("Bad:")
# vision.set_input_image("images/Good_Images/Spring1_0_bad.jpg")
# vision.isolate_input_image_logo()
# vision.get_input_image_features()
# print(vision.match())

# print("Bad:")
# vision.set_input_image("images/Good_Images/Spring1_1_bad.jpeg")
# vision.isolate_input_image_logo()
# vision.get_input_image_features()
# print(vision.match())
# exit()
# order = [1, 3]
# for i in order:
#     print("-------------------")
#     print(i)
#     vision.set_good_image("images/Good_Images/Spring" + str(i) + "_0.jpeg")
#     vision.isolate_good_image_logo()
#     vision.get_good_image_features()
#     for j in range(1, 5):
#         vision.set_input_image("images/Good_Images/Spring" + str(i) + "_" + str(j) + ".jpeg")
#         vision.isolate_input_image_logo()
#         vision.get_input_image_features()

#         print(vision.match())

order = [3]
correctly_guessed = 0
count = 0

for i in order:
    print("-------------------")
    print(i)
    vision.set_good_image("images/Good_Images/Spring" + str(i) + "_0.jpeg")
    vision.isolate_good_image_logo()
    vision.get_good_image_features()
    for j in range(5):
        print("image"+str(j))
        vision.set_input_image("images/Good_Images/Spring" + str(i) + "_" + str(j) + ".jpeg")
        vision.isolate_input_image_logo()
        vision.get_input_image_features()

        matched = vision.match()
        if matched[1] == True:
            correctly_guessed += 1
        count += 1
        print("good iamge: " + str(matched))
        
        for k in range(5):
            vision.set_input_image("images/Bad_Images/Spring" + str(i) + "_" + str(j) + "_bad" + str(k) + ".jpeg")
            vision.isolate_input_image_logo()
            vision.get_input_image_features()
            matched = vision.match()

            if matched[1] == False:
                correctly_guessed += 1
            count += 1
            print(matched)

print(correctly_guessed/count)