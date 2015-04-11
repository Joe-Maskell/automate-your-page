
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text


def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)


def make_HTML_for_many_concepts(list_of_concepts):

    HTML_code = ''
    for concept in list_of_concepts:
        HTML_code += make_HTML(concept)
    return HTML_code


LIST_OF_CONCEPTS = [ ['Make a strategy', '''Write down the input<br>Sketch out the output<br>We want to write a function or functions to convert the input to the output<br>
                    If the probelm is too large to do in one step, break it down and do one concept at a time'''],
                    ['Structured Data', '''Lists are more powerful than strings. Sequences can be characters, strings or lists<br>
                    partial lists can be obtained in the same way partial strings are obtained<br>
                    Values of lists can be changed after they are created, unlike strings. This can be done by changing the elements of a list.<br>
                    e.g. p = ['H','e','l','l','o']<br>
                    p[0] = 'Y'<br>
                    This is called mutability'''],
                    ['Lists', 'Lists are sequences of data'] ]

print make_HTML_for_many_concepts(LIST_OF_CONCEPTS)