import streamlit as st


#step 1 user input

st.title("Text Analyzer")

text= st.text_area("Enter your paragraph")

#step 2 word.character and vowel count 

if text:
    words= (text.split())
    characters= len(text)

# step  2 count vowels
    vowels=sum([1 for char in text if char in 'aeiou'])
    print(vowels)
    st.write("Total words:", len(words))
    
#  step 3 Search and replace features
    search= st.text_input("Search")
    replace= st.text_input("Replace")
    
    if st.button("Search and Replace"):
        new_text= text.replace(search,replace)
        st.write(new_text)

# step 4  Uppercase and lowercase conversion  

        st.write("Uppercase:", text.upper())
        st.write("Lowercase:", text.lower())

# step 5 use operators

check_word = st.text_input("Enter a word to check if it exists in the text")

if check_word:
    if check_word in words:
        st.write(f"Yes, the word '{check_word}' is in the text.")
    else:
        st.write(f"No, the word '{check_word}' is not in the text.")

    # step 6 average word length
    average_word_length = characters / len(words) if len(words) > 0 else 0 
    st.write(f"The average word length is {average_word_length:.2f} characters.")   
else:
    st.write("Please enter some text.")                                                                               
                               