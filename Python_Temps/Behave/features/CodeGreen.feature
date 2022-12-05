Feature: CodeGreen Logo

    Scenario: Logo presence on CodeGreen home page
        Given launch chrome browser
        When open CodeGreen home page
        Then verify that the Logo present on page
        And close browser
    