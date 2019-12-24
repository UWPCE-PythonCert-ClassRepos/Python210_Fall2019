import mailroom04 as mr
import os

#initiate donor list for test
mr.donors= {'FirstName LastName': [100, 2500]}
letter_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\n Sed viverra tellus in hac habitasse platea dictumst vestibulum. Duis at tellus at urna. Urna neque viverra justo nec.\n Rutrum tellus pellentesque eu tincidunt. Felis eget nunc lobortis mattis aliquam faucibus purus."



def test_create_thankYou():
    output=mr.create_thankYou("NAME", 1234)
    compare="Dear NAME,\n \n Thanks for the $1234.00 sucker.\n\n                          -Your Fave Charity"
    assert output == compare

def test_create_report():
    output=mr.create_report()
    report_expected = ['FirstName LastName             2600.00               2              1300.00']
    assert output == report_expected

def test_thanks_all():
    output=mr.thanks_all()
    output_expected = ['Dear FirstName LastName,\n \n Thanks for the $2500.00 sucker.\n\n                          -Your Fave Charity']
    assert output == output_expected

#check if the TY_LETTERS folder gets created
def test_write_file_folder_creation():
    #construct the path
    file_path = os.getcwd() + "/TY_LETTERS"
    file_name = "TEST_FILENAME_000_thank_you_letter.txt"
    os.system("rm -rf {}".format(file_path))
    #create file
    mr.write_file("TEST_FILENAME_000","content")
    #check if file xists
    assert os.path.isfile(file_path+"/"+file_name)

#check if another file is created
def test_write_file_creation():
    #construct the path
    file_path = os.getcwd() + "/TY_LETTERS"
    file_name = "TEST_FILENAME_001_thank_you_letter.txt"
    #create file
    mr.write_file("TEST_FILENAME_001",letter_content)
    #check if file xists
    assert os.path.isfile(file_path+"/"+file_name)

#check the content of the file from the last test
def test_write_file_content():
    #construct the path
    file_path = os.getcwd() + "/TY_LETTERS"
    file_name = "TEST_FILENAME_001_thank_you_letter.txt"
    full_path = file_path + "/" + file_name
    content = open(full_path, 'r').read()
    #check if file xists
    assert content == letter_content

