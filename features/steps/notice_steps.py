from behave import given, when, then
from pages.setting_page import SettingPage

# GIVEN
@given('앱이 시작 되고')
def step_impl(context):
  context.setting_page = SettingPage(context.driver)

@given('학사 알림이 구독된 상태이고')
def step_impl(context):
  context.setting_page = SettingPage(context.driver)
  assert context.setting_page.is_academic_switch_on()

# WHEN
@when('설정 탭을 클릭한다')
def step_impl(context):
  context.setting_page.click_setting_button()

@when('학사/장학 알림 메뉴를 클릭한다')
def step_impl(context):
  context.setting_page.click_academic_setting_menu()

@when('학사 알림 스위치를 클릭하면')
def step_impl(context):
  context.setting_page.toggle_academic_switch()

# THEN
@then('학사 알림이 On 된다')
def step_impl(context):
  assert context.setting_page.is_academic_switch_on()

@then('학사 알림이 Off 된다')
def step_impl(context):
  assert context.setting_page.is_academic_switch_off()