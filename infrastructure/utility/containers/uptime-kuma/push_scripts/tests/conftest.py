import pytest


@pytest.fixture
def pve_sample_data_missing_two():
    return [

        "/data_root/PROXMOX/dump/vzdump-qemu-100-2026_04_02-11_44_53.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-1010-2026_04_02-00_02_10.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-104-2026_04_02-00_00_02.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-105-2026_04_02-05_01_08.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-5010-2026_04_02-00_06_36.vma.zst",
    ]

@pytest.fixture
def pve_sample_data_missing_one():
    return [

        "/data_root/PROXMOX/dump/vzdump-qemu-100-2026_04_02-11_44_53.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-1010-2026_04_02-00_02_10.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-103-2026_04_02-05_00_05.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-104-2026_04_02-00_00_02.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-105-2026_04_02-05_01_08.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-5010-2026_04_02-00_06_36.vma.zst",
    ]

@pytest.fixture
def pve_sample_data_correct():
    return [

        "/data_root/PROXMOX/dump/vzdump-qemu-100-2026_04_02-11_44_53.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-101-2026_04_02-11_45_02.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-1010-2026_04_02-00_02_10.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-103-2026_04_02-05_00_05.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-104-2026_04_02-00_00_02.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-105-2026_04_02-05_01_08.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-5010-2026_04_02-00_06_36.vma.zst",
    ]

@pytest.fixture
def pve_sample_data_excessive():
    return [
        "/data_root/PROXMOX/dump/vzdump-qemu-100-2026_03_29-01_00_01.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-100-2026_03_30-01_00_00.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-100-2026_03_31-01_00_04.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-100-2026_04_01-01_00_00.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-100-2026_04_02-01_00_00.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-100-2026_04_02-11_44_53.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-101-2026_03_29-10_21_29.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-101-2026_03_30-05_00_01.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-101-2026_03_31-05_00_04.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-101-2026_04_01-05_00_00.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-101-2026_04_02-05_00_00.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-101-2026_04_02-11_45_02.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-101-2026_04_02-11_55_12.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-1010-2026_03_29-00_02_06.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-1010-2026_03_30-00_02_08.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-1010-2026_03_31-00_02_05.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-1010-2026_04_01-00_02_05.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-1010-2026_04_02-00_02_10.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-103-2026_03_29-05_00_01.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-103-2026_03_30-05_00_00.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-103-2026_03_31-05_00_00.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-103-2026_04_01-05_00_04.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-103-2026_04_02-05_00_05.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-104-2026_03_29-00_00_03.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-104-2026_03_30-00_00_05.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-104-2026_03_31-00_00_02.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-104-2026_04_01-00_00_01.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-104-2026_04_02-00_00_02.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-105-2026_03_29-05_01_03.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-105-2026_03_30-05_01_02.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-105-2026_03_31-05_01_02.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-105-2026_04_01-05_01_06.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-105-2026_04_02-05_01_08.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-5010-2026_03_29-00_06_29.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-5010-2026_03_30-00_06_29.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-5010-2026_03_31-00_06_26.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-5010-2026_04_01-00_06_26.vma.zst",
        "/data_root/PROXMOX/dump/vzdump-qemu-5010-2026_04_02-00_06_36.vma.zst",
    ]

@pytest.fixture
def pbs_sample_data_correct():
    return [
        "/mnt/datastore/backup_pool/vm/100/2026-04-03T06:00:06Z/client.log.blob",
        "/mnt/datastore/backup_pool/vm/101/2026-04-03T10:00:00Z/client.log.blob",
        "/mnt/datastore/backup_pool/vm/1010/2026-04-03T05:00:06Z/client.log.blob",
        "/mnt/datastore/backup_pool/vm/103/2026-04-03T10:00:02Z/client.log.blob",
        "/mnt/datastore/backup_pool/vm/104/2026-04-03T05:00:02Z/client.log.blob",
        "/mnt/datastore/backup_pool/vm/105/2026-04-03T10:00:07Z/client.log.blob",
        "/mnt/datastore/backup_pool/vm/5010/2026-04-03T05:00:20Z/client.log.blob",
    ]

