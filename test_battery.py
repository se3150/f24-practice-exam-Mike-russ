import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b


def describe_Battery():

    def test_notify_drain_called_once():
        mock_monitor = Mock()
        battery = Battery(100, external_monitor=mock_monitor)
        battery.drain(30)
        mock_monitor.notify_drain.assert_called_once_with(70)

    def describe_recharge():
        # your test cases here
        def it_recharges_partial_charged_batteries(partially_charged_battery):
            b = partially_charged_battery
            assert b.getCharge() == 70
            #fully charge the battery.
            b.recharge(30)
            assert b.getCharge() == 100

        def it_does_not_break_if_recharge_is_more_than_capacity(partially_charged_battery):
            b = partially_charged_battery
            assert b.getCharge() == 70
            b.recharge(50)
            assert b.getCharge() == 100

        def it_does_not_break_if_charging_a_full_battery(charged_battery):
            b = charged_battery
            assert b.getCharge() == 100
            b.recharge(30)
            assert b.getCharge() == 100

        def it_does_not_recharge_negatives(partially_charged_battery):
            b = partially_charged_battery
            assert b.getCharge() == 70
            b.recharge(-10)
            assert b.getCharge() == 70

        def it_does_not_break_if_recharging_zero(partially_charged_battery):
            b = partially_charged_battery
            assert b.getCharge() == 70
            b.recharge(0)
            assert b.getCharge() == 70

        def it_can_charge_drain_then_charge_again(partially_charged_battery):
            b = partially_charged_battery
            assert b.getCharge() == 70
            b.recharge(10)
            assert b.getCharge() == 80
            b.drain(30)
            assert b.getCharge() == 50
            b.recharge(40)
            assert b.getCharge() == 90

    def describe_drain():
        # your test cases here
        def it_drains_charged_batteries(charged_battery):
            b = charged_battery
            assert b.getCharge() == 100
            b.drain(40)
            assert b.getCharge() == 60

        def it_does_not_drain_more_than_capacity(charged_battery):
            b = charged_battery
            assert b.getCharge() == 100
            b.drain(110)
            assert b.getCharge() == 0

        def it_does_not_drain_negatives(partially_charged_battery):
            b = partially_charged_battery
            assert b.getCharge() == 70
            b.drain(-10)
            assert b.getCharge() == 70
        
        def it_does_not_break_if_draining_an_uncharged_battery(charged_battery):
            b = charged_battery
            assert b.getCharge() == 100
            b.drain(100)
            assert b.getCharge() == 0
            b.drain(50)
            assert b.getCharge() == 0

        def it_does_not_break_if_drain_is_zero(charged_battery):
            b = charged_battery
            b.getCharge() == 100
            b.drain(0)
            b.getCharge == 100

        def it_can_drain_recharge_then_drain_again(partially_charged_battery):
            b = partially_charged_battery
            b.getCharge() == 70
            b.drain(30)
            b.getCharge() == 40
            b.recharge(20)
            b.getCharge() == 60
            b.drain(40)
            b.getCharge() == 20