import pytest

@pytest.mark.parametrize("name", [
    "경영전문대학원",
    "문화전문대학원",
    "치의학전문대학원",
    "법학전문대학원",
    "데이터사이언스대학원",
])
@pytest.mark.parametrize("setting_page", ["전문대학원 알림"], indirect=True)
def test_전문대학원_알림을_설정한다(setting_page, name):
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_on(name)
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_off(name)