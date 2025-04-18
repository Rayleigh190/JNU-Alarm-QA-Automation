Feature: 학사 알림 구독
  Scenario: 사용자가 학사 알림을 구독한다
    Given 앱이 시작 되고
    When 설정 탭을 클릭한다
    And 학사/장학 알림 메뉴를 클릭한다
    And 학사 알림 스위치를 클릭하면
    Then 학사 알림이 On 된다
  
  Scenario: 사용자가 학사 알림을 구독 취소한다
    Given 학사 알림이 구독된 상태이고
    When 학사 알림 스위치를 클릭하면
    Then 학사 알림이 Off 된다
