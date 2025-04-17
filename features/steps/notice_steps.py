from behave import given, when, then
from pages.notice_page import NoticePage

@given('앱이 시작 됩니다.')
def step_impl(context):
    context.notice_page = NoticePage(context.driver)

# @when('설정 탭을 클릭합니다.')
# def step_impl(context):
#     context.setting_page.tap_setting()

@then('알림 내역 화면이 보입니다.')
def step_impl(context):
    assert context.notice_page.is_notice_screen_displayed()
