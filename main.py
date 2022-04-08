import vision_system


vision = vision_system.vision_system()

vision.set_good_image("images/spring2.png")

vision.isolate_good_image_logo()

vision.get_good_image_features()



vision.set_input_image("images/spring2_bad2.png")

vision.isolate_input_image_logo()

vision.get_good_input_features()

print(vision.match())

