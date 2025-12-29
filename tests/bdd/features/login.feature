Feature: Login

  Scenario: Successful login
    Given user opens login page
    When user enters credentials
    Then user should be logged in
