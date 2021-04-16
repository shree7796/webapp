import PyPDF2
import re
import nltk

from .views import DocumentView


class OpenPdfFileAndExtractFields:
    # function that will parse the resume and return the results in multiple sections
    Name = []
    Experience = []
    Education = []
    Skills = []
    Address = []
    Email = []
    Phone = []

    def __init__(self):
        path = DocumentView.file_absolute_path[0]
        DocumentView.file_absolute_path.clear()
        file = path
        open_file = open(file, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(open_file)
        results = ''
        self.lines = []
        for page in range(0, pdf_reader.getNumPages()):
            pages = pdf_reader.getPage(page)
            page_content = pages.extractText()
            result = str(page_content)
            results += result
            self.lines.append(result)

    def name(self):
        self.Name.clear()
        tokenized_doc = nltk.word_tokenize(self.lines[0][0:50])
        tagged_sentences = nltk.pos_tag(tokenized_doc)
        ne_chunked_sentences = nltk.ne_chunk(tagged_sentences)

        named_entities = []
        for tagged_tree in ne_chunked_sentences:
            if hasattr(tagged_tree, 'label'):
                entity_name = ' '.join(c[0] for c in tagged_tree.leaves())
                named_entities.append(entity_name)
                entity_type = tagged_tree.label()  # get NE category
                self.Name.append(named_entities)
        print("\nName: ", named_entities)

    def email(self):
        self.Email.clear()
        lines_index_number = 0
        for page in self.lines:
            search_email = re.findall(r"[\w+.-]+@[\w+.-]+", self.lines[lines_index_number])
            if search_email:
                print("\nEmail: ", search_email)
                self.Email.append(search_email)
                break
            lines_index_number += 1

    def mobile_no(self):
        self.Phone.clear()
        lines_index_number = 0
        for page in self.lines:
            phone_number = re.findall(r'[+][1-9][0-9 .\-]{8,}[0-9]', self.lines[lines_index_number])
            if phone_number:
                print('\nPhone number: ', phone_number)
                self.Phone.append(phone_number)
                break
            lines_index_number += 1

    def experience(self):
        self.Experience.clear()
        lines_index_number = 0

        experience_patterns = ['EXPERIENCE', 'Experience']
        final_experience_result = ''
        for page in self.lines:
            pat1 = []
            for pattern in experience_patterns:
                pat = re.findall(pattern, self.lines[lines_index_number])
                w1 = self.lines[lines_index_number]
                if pat:
                    index = self.lines[lines_index_number].index(pattern)
                    for i in w1[index:]:
                        # print(i)
                        final_experience_result += str(i)
                pat1.append(pat)
            if pat1:
                break
            lines_index_number += 1

        experience_result = ''
        list_of_words_where_loop_breaks = ['HOBBIES', 'SKILL', 'SKILLS', 'Skills', 'EDUCATION', 'PERSONAL']
        # skills_result = ''
        word_list = re.sub("[^\w]", " ", final_experience_result).split()
        for word in word_list:
            if word in list_of_words_where_loop_breaks:
                break
            experience_result += word
            experience_result += " "

        self.Experience.append(experience_result)

    def skills(self):
        self.Skills.clear()
        lines_index_number = 0
        skills_pattern = ['SKILL', 'Skills']
        final_skills_result = ''
        for page in self.lines:
            for pattern in skills_pattern:
                pat = re.findall(pattern, self.lines[lines_index_number])
                w1 = self.lines[lines_index_number]
                if pat:
                    skills_index = self.lines[lines_index_number].index(pattern)
                    for i in w1[skills_index:]:
                        final_skills_result += str(i)
                    break
            lines_index_number += 1

        list_of_words_where_loop_breaks = ['HOBBIES', 'EXPERIENCE', 'PERSONAL DETAILS', 'EDUCATION']
        skills_result = ''
        word_list = re.sub("[^\w]", " ", final_skills_result).split()
        for word in word_list:
            if word in list_of_words_where_loop_breaks:
                break
            skills_result += word
            skills_result += " "

        self.Skills.append(skills_result)

    def education(self):
        self.Education.clear()
        lines_index_number = 0
        education_pattern = ['Education', 'EDUCATION', 'Academic']
        final_education_result = ''
        for page in self.lines:
            for pattern in education_pattern:
                pat = re.findall(pattern, self.lines[lines_index_number])
                w2 = self.lines[lines_index_number]
                if pat:
                    education_index = self.lines[lines_index_number].index(pattern)
                    for i in w2[education_index:]:
                        final_education_result += str(i)
                    break
            lines_index_number += 1

        list_of_words_where_loop_breaks = ['HOBBIES', 'EXPERIENCE', 'SKILL', 'SKILLS', 'Objective', 'Achievements']
        education_result = ''
        word_list = re.sub("[^\w]", " ", final_education_result).split()
        for word in word_list:
            if word in list_of_words_where_loop_breaks:
                break
            education_result += word
            education_result += " "

        self.Education.append(education_result)

    def address(self):
        self.Address.clear()
        lines_index_number = 0
        for page in self.lines:
            search_address = re.findall(r"[\d+]+\s[\w+\s]+[,]\s[\w+]+\s[\d+]+", self.lines[0])
            if search_address:
                print("\nAddress: ", search_address)
                self.Address.append(search_address)
                break
            lines_index_number += 1

    def jsonfile(self):
        import json
        data = {}
        data['people'] = []
        data['people'].append({
            'Name': self.Name,
            'Email': self.Email,
            'Address': self.Address,
            'Experience': self.Experience,
            'Skills': self.Skills,
            'Education': self.Education,
            'Mob. no.': self.Phone,
        })

        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)


if __name__ == '__main__':
    print('Run........! ')
    obj = OpenPdfFileAndExtractFields()
    # obj.name() # Note: This will get fix i Phase-2
    obj.email()
    obj.mobile_no()
    obj.experience()
    obj.skills()
    obj.education()
    obj.address()
