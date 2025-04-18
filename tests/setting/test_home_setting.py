import pytest

@pytest.mark.parametrize("name", [
    "학사 알림",
    "장학 알림",
    "학사 | 타 대학교 교류학생 알림",
])
def test_홈_알림을_설정한다(setting_page, name):
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_on(name)
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_off(name)