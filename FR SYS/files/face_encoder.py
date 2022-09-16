def encoding_faces_to_database():

    # Importing necesssary libraries
    # Face encoder library
    import face_recognition

    # For image opening and reading
    import cv2

    # Mathematical operations
    import numpy as np

    # Working with directories
    import os
    import glob

    # Creating a array where we gonna store face encodings
    faces_encodings = []

    # An array where we will store the name of each encoding (Person)
    faces_names = []
    
    process_this_frame = True

    # The path of the images that should be stored in the database
    direc = 'files/data/faces\\'

    
    # Unused variable, skip it
    file_name = open("namelist.txt","w")
   
    
    # Getting current working directory
    cur_direc = os.getcwd()

    # Path = the whole path to the images
    path = os.path.join(cur_direc, direc)

    # Gets the name of each image (each .jpg file in the path)
    list_of_files = [f for f in glob.glob(path+'*.jpg')]

    # Number of files in the path
    number_files = len(list_of_files)

    names = list_of_files.copy()

    for i in range(number_files):
        # Reading the images, and finding face
        globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])

        # Encoding the face
        globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]

        # adding the face into an array
        faces_encodings.append(globals()['image_encoding_{}'.format(i)])

        # known names - Cleaning from unuseful symbols
        names[i] = names[i].replace(cur_direc, "")  
        names[i] = names[i].replace(direc,'')
        names[i] = names[i].replace("\\",'')
        names[i] = names[i].replace(".jpg",'')

        # Adding to Name list cleaned names
        faces_names.append(names[i])
        print(names[i])
        file_name.write(names[i]+"\n")
        

    # Declaring empty text
    text = ""
    # Open for writing 
    f = open("files/data/facial Data.txt","w")
    # Number many faces
    n_faces = number_files
    # Entering name and encodings
    for i in range(0,n_faces):
        # Inserting name
        text += str(names[i])
        # Going to the next line
        text += "\n"
        # Inserting Face Encodings
        for j in range(0,128):
            # Inserting encoding
            text += str(faces_encodings[i][j])
            # Going to the next line
            text += "\n"
    # Removing brackets    
    text = text.replace("[",'')
    text = text.replace("]",'')

    # Writing the full info about the faces
    f.write(text)
    f.close()





