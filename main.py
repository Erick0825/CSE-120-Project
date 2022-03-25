import vision_system


vision = vision_system.vision_system()

vision.set_good_image("images/spring2.jpg")

vision.isolate_good_image_logo()

vision.get_good_image_features()


