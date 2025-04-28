import pytest

@pytest.mark.parametrize("name", [
    "교육대학원",
    "산업대학원",
    "정책대학원",
    "식물방역대학원",
    "산학협력대학원",
    "수산해양대학원",
])
@pytest.mark.parametrize("setting_page", ["특수대학원 알림"], indirect=True)
def test_특수대학원_알림을_설정한다(setting_page, name):
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_on(name)
    setting_page.toggle_switch(name)
    assert setting_page.is_switch_off(name)