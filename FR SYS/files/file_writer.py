


def open_new_excel(name_l):
    from datetime import datetime

    #Get Current date
    current = datetime.now()
    current = current.strftime("%d/%m/%Y")
    current = current.replace("/",".")
    #All inside text
    txt = ""
    #Number of names
    len_name = len(name_l)
    #Open new file to write
    f = open("files/data/dates/"+str(current)+".xlsx","w")
    #Write the header
    txt += "Name\tTimes_Seen\tFirst_Seen\tLast_Seen\n"
    #Write the names and fill time with zeros
    for i in range(0,len_name):
        txt+=name_l[i]
        txt+="\t0\t00:00:00\t00:00:00\n"
    #write the text to the file
    f.write(txt)
    # Close the file
    f.close()
    






def found_face(name_list,new_name):
    # Importing necessary libraries
    from datetime import datetime
    import os
    import glob

    name_len = len(name_list)
    # Get current date
    now = datetime.now()
    now = now.strftime("%d/%m/%Y")
    now = now.replace("/",".")
    # Get current hours and minutes
    cur = datetime.now()
    date_0 = cur.strftime("%H:%M:%S")

    #print(date_0)
    
        
    try:
        # Open file
        f = open("files/data/dates/"+str(now)+".xlsx","r")
    except:
        # If doesnt exist, then create it and 
        open_new_excel(name_list)
        # re-open file
        f = open("files/data/dates/"+str(now)+".xlsx","r")
    # Get the full info from the file
    text = f.read()
    # Split all the words
    splitted_text = text.split()

    # Close the reading file        
    f.close()
    
    # Loop through all the words
    for i in range(3,len(splitted_text)):
        # If current word = our name
        if splitted_text[i]== new_name:
            # If the man isnt seen any time
            if splitted_text[i+2]=="00:00:00":
                # First Seen = now
                splitted_text[i+2]= date_0
            # Last Seen = now
            splitted_text[i+3] = date_0

            # How many times seen
            t_seen = int(splitted_text[i+1])
            
            # Times seen + 1
            t_seen += 1
            # Insert "times seen + 1" to the file
            splitted_text[i+1] = str(t_seen)
    
    # Open file for writing
    f = open("files/data/dates/"+str(now)+".xlsx","w")

    # Write the change "Splitted_text"
    for i in range(0,len(splitted_text)):
        # Starting from new line 
        if i%4==0:
            # If not the beginning
            if not i==0:
                # Go to the new line
                f.write("\n")
        # Write the info
        f.write(splitted_text[i])
        
        # Put the spaces between words
        f.write("\t")
    f.close()

    

    
