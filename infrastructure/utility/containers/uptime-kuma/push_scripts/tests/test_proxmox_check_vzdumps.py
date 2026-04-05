import pytest

from unittest.mock import patch, MagicMock

from proxmox_check_vzdumps import HostType


@pytest.mark.parametrize("fixture_name,status,message,datastore_path,host_type", [
        ("pve_sample_data_excessive", "up", "", "/data_root/PROXMOX/dump", HostType.PVE,), 
        ("pve_sample_data_correct", "up", "", "/data_root/PROXMOX/dump", HostType.PVE,),
        ("pve_sample_data_missing_one", "down", "Missing [101] backups ", "/data_root/PROXMOX/dump", HostType.PVE,),
        ("pve_sample_data_missing_two", "down", "Missing [101, 103] backups ", "/data_root/PROXMOX/dump", HostType.PVE,),
        ("pbs_sample_data_correct", "up", "", "/mnt/datastore/backup_pool/vm", HostType.PBS,),
        ("pbs_sample_data_extra", "down", "Non monitored {999: 1}", "/mnt/datastore/backup_pool/vm", HostType.PBS,),
        ("pbs_sample_data_missing_one", "down", "Missing [100] backups ", "/mnt/datastore/backup_pool/vm", HostType.PBS,),
        ("pbs_sample_data_missing_two", "down", "Missing [100, 101] backups ", "/mnt/datastore/backup_pool/vm", HostType.PBS,),
    ]
)
@pytest.mark.focus
def test_proxmox_check_vzdumps_pve(request, fixture_name, status, message, datastore_path, host_type):
    from proxmox_check_vzdumps import process

    fixture_value = '\n'.join(request.getfixturevalue(fixture_name))

    execute_command_mock = MagicMock()
    execute_command_mock.return_value.returncode = 0
    execute_command_mock.return_value.stdout = fixture_value

    m=kuma_push_mock = MagicMock()

    host = "proxmox_host"
    vmids_json = '[100,101,1010,103,104,105,5010]'
    kuma_push_url = "http://kuma_push_url"
    
    with patch('proxmox_check_vzdumps.execute_command', execute_command_mock):
        with patch('proxmox_check_vzdumps.kuma_push') as kuma_push_mock:
            lookback = 24
            selector = "zst$" if host_type == HostType.PVE else "client.log.blob$"
            result = process(host, vmids_json, kuma_push_url, datastore_path, selector, lookback, host_type)

            kuma_push_mock.assert_called_once()
            args, kwargs = kuma_push_mock.call_args
            assert args[0] == kuma_push_url
            assert args[1] == status
            assert args[2] == message