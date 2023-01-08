import spacy
nlp = spacy.load('en_core_web_md')

description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# function "recommendation" takes parameter "description"
# opens "movies.txt" file
# "lines_split" stores each line of "movies.txt" in a nested list
# "similarity_list" stores the similarity score for every movie description
# for loop gets the similarity score of every line's description
# "highest_sim_index" gets the index of the highest similarity score within "similarity_list"
# returns the movie name from "lines_split" list using the "highest_sim_index"
def recommendation(description):
    
    file = open("movies.txt", "r")

    compare_sentence = nlp(description)
    lines_split = []
    similarity_list = []

    for line in file:
        lines_split.append(line.split(":"))

    for i in range(0, len(lines_split)):
        similarity_list.append(nlp(lines_split[i][1]).similarity(compare_sentence))
        
    highest_sim_index = similarity_list.index(max(similarity_list))

    return lines_split[highest_sim_index][0]
        
print("Your next recommended movie is: " + recommendation(description))        
        
