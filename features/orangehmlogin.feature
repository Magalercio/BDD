Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid parameters
    Given launch chrome
    When open orange hrm login homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page


  Scenario Outline: Login to OrangeHRM with Multiples parameters
    Given launch chrome
    When open orange hrm login homepage
    And Enter username "<username>" and password "<password>"
    And Click on login button
    Then User must successfully login to the Dashboard page

    Examples:
      | username | password |
      | admin    | admin123 |
      | admin123 | admin    |
      | adminxyz | admin123 |
      | admin    | adminxyz |
