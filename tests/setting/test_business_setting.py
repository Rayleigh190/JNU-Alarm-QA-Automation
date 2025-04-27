import pytest

@pytest.mark.parametrize("name", [
    "소프트웨어중심대학사업단",
    "인공지능혁신융합대학사업단",
    "차세대통신혁신융합대학사업단",
    "반도체특성화대학사업단",
])
@pytest.mark.parametrize("setting_page", ["사업단 알림"], indirect=True)
def test_사업단_알림을_설정한다(setting_page, name):
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_on(name)
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_off(name)