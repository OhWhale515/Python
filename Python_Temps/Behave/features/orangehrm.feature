Feature: OrangeHRM Logo

    Scenario: Logo presence on OrangeHRM home page
        Given launch chrome browser
        When open OrangeHRM home page
        Then verify that the Logo present on page
        And close browser
    