def run_fr():
    # Importing all necessary libraries
    import face_recognition
    # cv2 for image manipulation
    import cv2
    # numpy for mathematical actions
    import numpy as np
    # os for finding file locations
    import os
    import glob
    # file_writer is external library that we wrote ourselves
    from file_writer import open_new_excel,found_face

    # Declaring an empty list (array) for reading face encodings from database (txt file)
    faces_encodings = []
    # Declaring an empty list (array) for reading names from database
    faces_names = []

    # While this variable is True - the Camera window will open
    process_this_frame = True

    # Location of the face images 
    direc = 'files/data/faces\\'

    # Get current path of the code
    cur_direc = os.getcwd()

    # Reading the database (txt file)
    f = open("files/data/facial Data.txt","r")

    # Color codes (RGB)
    orange_color = (255,165,0)
    red_color = (0,0,255)
    green_color = (0,255,0)
    black_color = (0,0,0)
    white_color = (255,255,255)

    # Declaring path variable for further reading of all the images
    path = os.path.join(cur_direc, direc)

    # Getting the names of images
    list_of_files = [f for f in glob.glob(path+'*.jpg')]

    # The lengh of the list
    number_files = len(list_of_files)

    # The number of faces in the database
    n_faces = number_files

    #
    names = list_of_files.copy()


    
    for i in range(0,n_faces):
        # Reading the name from the TXT file
        faces_names.append(f.readline())

        # Declaring empty array
        temp = []

        # Reading other 128 encodings of the face
        for j in range(0,128):

            # Reading current line
            cur = f.readline()
            if not len(cur)==0:
                # Changing the type of the readed line from STR to number
                cur = float(cur)

                # adding that number to the temporary array
                temp.append(cur)

        # adding that temporary array to the whole face encoding list
        faces_encodings.append(temp)
            

    print(faces_names)
    #print(names)

    # It get camera source
    video_capture = cv2.VideoCapture(0)

    while True:
        # Setting our color to red (Red is declared above in the code)
        color = red_color

        # We are getting every frame of the video as FRAME variable
        ret, frame = video_capture.read()

        # Resizing the taken image from the frame by 4 times (0.25 means that it is reduced in size by 4 times)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # We are converting the color range in order to better recognize faces
        rgb_small_frame = small_frame[:, :, ::-1]

        # All the main code is here - here we will encode the faces in the Video Window
        if process_this_frame:

            # Finding face locations on the image (Video)
            face_locations = face_recognition.face_locations(rgb_small_frame,1)

            # Encoding the found face locations into an array
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            # Variable for storing the names of people found in the image 
            face_names=[]

            # If many faces found - go through each face
            for face_encoding in face_encodings:

                # faces_encodings = The encoded faces from the database;  face encoding = encoded face in the video
                matches = face_recognition.compare_faces(faces_encodings, face_encoding)

                # Setting default name as Unknown
                name = 'Unknown'

                # faces_encodings = The encoded faces from the database;  face encoding = encoded face in the video

                # face_distances = the distance of the new face from the video to all faces in the database
                face_distances = face_recognition.face_distance( faces_encodings, face_encoding)

                # Getting the position of the minimum value in the array of face distances
                best_match_index = np.argmin(face_distances)

                # Getting the name
                if matches[best_match_index]:

                    # getting the name of the person with lowest distance value 
                    name = faces_names[best_match_index]
                    
                    print(name)
                    print(face_distances[best_match_index])

                # Adding the name into the list of found names
                face_names.append(name)

        process_this_frame = not process_this_frame

        
        # showing result - drawing the box and the name on the actual video
        for(top, right, bottom, left), name in zip(face_locations, face_names):
            # We are getting the locations of the positions of the face in the top,right,bottom,left variables
            # we are multiplying all these by 4 because previously reduced the size by 4
            # in order to make the frame to the normal size we make it X4 
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            
            # Setting the color of the box as Green
            color = green_color

            # Our threshold is 0.44, if the distance is more than 0.44 than it will show that the face is Unknown
            if face_distances[best_match_index] > 0.44:
                # If distance is more than threshold than name= "unknonwn"
                name = "Unknown"

                # Setting the color of the box as red
                color = red_color
                

            
            
                
            # Drawing a box (Rectangle) at the place where the face was detected
            # INput parameters --> image itself, point1, point2, and the color of the box
            cv2.rectangle(frame, (left, top), (right, bottom), color )

            # inserting the Place for the Name inside that Box where the face is located
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255,255,255,0.5), cv2.FILLED)

            # Setting the font type to write the Name 
            font = cv2.FONT_HERSHEY_DUPLEX

            # Clearing out the Name if it has some unappropriate symbols
            name = name.replace(direc,'')
            name = name.replace("\\",'')
            name = name.replace(".jpg",'')
            name = name.replace("\n",'')

            # Setting name color as orange
            name_color = orange_color

            
            if face_distances[best_match_index] > 0.44:
                name = "Unknown"
                color = red_color
                name_color = red_color
                
            
            found_face(face_names, name)

            # Putting the name to the place on the image
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0,name_color , 1)

        # showing final image
        cv2.imshow('Video', frame)
       
        # press "q" to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

