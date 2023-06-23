from selene import browser, have, be  #модуль.файлы с набором методов
#from selene_in_action1.conditions import match
import os


def test_success_registration():
    browser.open('/automation-practice-form')

    #Preconditions
    browser.element('#firstName').type('Ольга')
    browser.element('#lastName').type('Иванова')
    browser.element('#userEmail').type('ya@mail.ru')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('1234567890').click()
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker-ignore-onclickoutside').click()
    browser.element('.react-datepicker__month-select').type('April')
    browser.element('.react-datepicker__year-select').type('1982')
    browser.element('[class="react-datepicker__day react-datepicker__day--001"]').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element( '#currentAddress').type('Lenina str 1')
    browser.element('#uploadPicture').send_keys(os.path.abspath('documents/doc.jpg'))
    browser.element('#state').click()
    browser.element('//*[.="NCR"]').click()
    browser.element('#city').click()
    browser.element('//*[.="Delhi"]').click()

    #Button "Submit" is visible on the registration page
    browser.element('#submit').should(be.visible).click()

    #Check the header  of response form
    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))

    #Check  data in the response form
    browser.all('.table-dark tr th')[0].should(have.exact_text('Label'))
    browser.all('.table-dark tr th')[1].should(have.exact_text('Values'))
    browser.all('.table-responsive tr td')[0].should(have.exact_text('Student Name'))
    browser.all('.table-responsive tr td')[1].should(have.exact_text('Ольга Иванова'))
    browser.all('.table-responsive tr td')[2].should(have.exact_text('Student Email'))
    browser.all('.table-responsive tr td')[3].should(have.exact_text('ya@mail.ru'))
    browser.all('.table-responsive tr td')[4].should(have.exact_text('Gender'))
    browser.all('.table-responsive tr td')[5].should(have.exact_text('Female'))
    browser.all('.table-responsive tr td')[6].should(have.exact_text('Mobile'))
    browser.all('.table-responsive tr td')[7].should(have.exact_text('1234567890'))
    browser.all('.table-responsive tr td')[8].should(have.exact_text('Date of Birth'))
    browser.all('.table-responsive tr td')[9].should(have.exact_text('01 April,1982'))
    browser.all('.table-responsive tr td')[10].should(have.exact_text('Subjects'))
    browser.all('.table-responsive tr td')[11].should(have.exact_text('Maths'))
    browser.all('.table-responsive tr td')[12].should(have.exact_text('Hobbies'))
    browser.all('.table-responsive tr td')[13].should(have.exact_text('Reading, Music'))
    browser.all('.table-responsive tr td')[14].should(have.exact_text('Picture'))
    browser.all('.table-responsive tr td')[15].should(have.exact_text('doc.jpg'))
    browser.all('.table-responsive tr td')[16].should(have.exact_text('Address'))
    browser.all('.table-responsive tr td')[17].should(have.exact_text('Lenina str 1'))
    browser.all('.table-responsive tr td')[18].should(have.exact_text('State and City'))
    browser.all('.table-responsive tr td')[19].should(have.exact_text('NCR Delhi'))

    #Button "Close" is visible on the respond form
    browser.element('//button[@id="closeLargeModal"]').should(be.visible).click()

    #Form is absent after click "Close"
    browser.element('.modal-content').should(be.absent)


